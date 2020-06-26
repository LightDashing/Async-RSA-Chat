#
# Серверное приложение для соединений
#
import asyncio
from asyncio import transports
from ServerSettings import ServerSettings
from aioconsole import ainput
import pickle
from DataBase import ServerDB
from Crypto.PublicKey import RSA
from Encryption import encrypt, decrypt, encrypt_bytes, decrypt_bytes
from cache import get_bytes, save_bytes
import uuid

class ServerProtocol(asyncio.Protocol):
    login: str = None
    logged_in = False
    public_key = None
    server: 'Server'
    transport: transports.Transport

    def __init__(self, server: 'Server'):
        self.server = server
        self.key_pair = RSA.generate(2048)
        self.private_key = self.key_pair.export_key()
        self.private_key = RSA.import_key(self.private_key)

    def data_received(self, data: bytes):
        pack = pickle.loads(data)
        if not self.logged_in:
            for user in self.server.clients:
                if user.login == pack['login']:
                    message = {'login': 'Server',
                               'message': 'The user with this nickname already exists on the server!',
                               'state': 4}
                    message = pickle.dumps(message)
                    self.transport.write(message)
                    self.transport.close()
                    self.server.clients.remove(self)
            if self.server.whitelistmode and not self.server.MainBD.is_user_exist(pack['login']):
                message = {'login': 'Server',
                           'message': 'WhiteList is active now! You are not registered on the server. '
                                      '\t Wait until this mode is turned off!',
                           'state': 3}
                message = pickle.dumps(message)
                self.transport.write(message)
                self.transport.close()
                self.server.clients.remove(self)
            elif not self.server.whitelistmode:
                if not self.server.MainBD.is_user_exist(pack['login']):
                    message = {'login': 'Server',
                               'message': f"Welcome to the server, {pack['login']}! \t By entering here, "
                                          f"you are automatically registered!", 'state': 1}
                    message = pickle.dumps(message)
                    self.transport.write(message)
                    self.server.MainBD.sign_in(pack["login"], pack['password'], pack['email'])
            if not self.server.MainBD.login(pack['login'], pack['password']):
                message = {'login': 'Server', 'message': 'Wrong combination of login and password \t Change them in'
                                                         'the settings and reconnect to the server!', 'state': 2}
                message = pickle.dumps(message)
                self.transport.write(message)
                self.transport.close()
                self.server.clients.remove(self)
            self.public_key = pack['public_key']
            self.public_key = RSA.import_key(self.public_key)
            message = {'login': 'Server', 'message': 'You have successfully entered the server!',
                       'public': self.key_pair.publickey().export_key(), 'state': 1}
            message = pickle.dumps(message)
            self.transport.write(message)
            self.logged_in = True
            self.login = pack['login']
            pack = {'login': '', 'color': None}
            message = f'User {self.login} is connected!'
            self.send_message(pack, message, 5)
            return

        message = decrypt(self.private_key, pack['message'])
        if pack['state'] == 2:
            self.send_pm(pack, message, pack['to'])
            return
        elif pack['state'] == 3:
            self.send_pm(state=7)
            return
        elif pack['state'] == 4:
            file = decrypt_bytes(self.private_key, pack['attach'])
            filename = str(uuid.uuid4())
            save_bytes(b=file, file=f'{filename}.{pack["ext"]}')
            pack['attach'] = file
            self.send_message(pack, message, attach=True)
            return
        print(message)
        self.send_message(pack, message)

    def connection_made(self, transport: transports.Transport):
        self.server.clients.append(self)
        self.transport = transport
        print("A new user has arrived.")

    def connection_lost(self, exception):
        pack = {'login': '', 'color':'red'}
        message = f'User {self.login} is disconnected!'
        self.send_message(pack, message, 5)
        for user in self.server.clients:
            if user.login == self.login:
                print(user)
                self.server.clients.remove(user)
        print("The user is out now.")

    def send_message(self, content: dict, message: str, state: int = None, attach=False):
        for user in self.server.clients:
            msg = encrypt(user.public_key, message)
            pack = {'login': content['login'], 'message': msg, 'state': state, 'color': content['color']}
            if attach:
                pack['attach'] = encrypt_bytes(self.public_key, content['attach'])
                pack['ext'] = content['ext']
                pack['state'] = 8
            pack = pickle.dumps(pack)
            user.transport.write(pack)

    def send_pm(self, content: dict = None, message: str = None, to: str = None, state: int = 6):
        if state == 7:
            users = "Users list:"
            for user in self.server.clients:
                users += f' {user.login},'
            msg = encrypt(self.public_key, users)
            pack = {'message': msg, 'state': 7}
            pack = pickle.dumps(pack)
            self.transport.write(pack)
            return
        for user in self.server.clients:
            if user.login == to:
                msg = encrypt(user.public_key, message)
                pack = {'login': content['login'], 'message': msg, 'state': state, 'color': content['color']}
                pack = pickle.dumps(pack)
                user.transport.write(pack)
                return


class Server:
    clients: list

    def __init__(self):
        self.clients = []
        self.MainBD = ServerDB()
        self.settings = ServerSettings()
        self.server_settings = self.settings.get_settings()
        self.whitelistmode = self.server_settings['whitelist']
        self.coroutine = None

    def build_protocol(self):
        return ServerProtocol(self)

    async def listening(self):
        command = ''
        while True:
            if command.lower() == 'users':
                print(f'On the server {len(self.clients)} users now.')
            elif command.lower() == 'list':
                logins = ''
                for user in self.clients:
                    logins += f'{user.login} '
                print('Users list: ', logins)
            elif command.lower()[:4] == 'kick':
                for user in self.clients:
                    if user.login == command[5:]:
                        user.transport.close()
                        print(f'User {command[5:]} has been kicked.')
                    else:
                        print(f'There is no user with a nickname {command[5:]}.')
            elif command.lower() == 'allkick':
                for user in self.clients:
                    user.transport.close()
            elif command.lower() == 'close':
                self.coroutine.close()
                print('Server has been shutdown.')
                exit()
            elif command.lower() == 'soft restart':
                pass

            command = await ainput()

    async def start(self):
        loop = asyncio.get_running_loop()
        self.coroutine = await loop.create_server(
            self.build_protocol,
            '192.168.1.35',
            25332
        )

        print("The server is running ...")

        await self.coroutine.serve_forever()


process = Server()


async def main():
    await asyncio.gather(process.start(), process.listening())

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("The server is stopped manually.")
