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
from Encryption import encrypt, decrypt


class ServerProtocol(asyncio.Protocol):
    login: str = None
    logged_in = False
    public_key = None
    server: 'Server'
    transport: transports.Transport

    def __init__(self, server: 'Server'):
        self.server = server
        # self.ServerSettings = ServerSettings()
        # serverdata = self.ServerSettings.get_settings()
        # self.whitelistmode = serverdata['whitelist']
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
                                                         'the settings and reboot to the server!', 'state': 2}
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
            return

        message = decrypt(self.private_key, pack['message'])
        print(message)
        self.send_message(pack, message)

    def connection_made(self, transport: transports.Transport):
        self.server.clients.append(self)
        self.transport = transport
        print("A new user has arrived.")

    def connection_lost(self, exception):
        self.server.clients.remove(self)
        print("The user is out now.")

    def send_message(self, content: dict, message: str):
        message = encrypt(self.public_key, message)
        pack = {'login': content['login'], 'message': message, 'state': 'None'}
        pack = pickle.dumps(pack)

        for user in self.server.clients:
            user.transport.write(pack)


class Server:
    clients: list

    def __init__(self):
        self.clients = []
        self.MainBD = ServerDB()  # TODO: Добавить конфигурацию сервера через JSON
        self.settings = ServerSettings()
        self.server_settings = self.settings.get_settings()
        self.whitelistmode = self.server_settings['whitelist']

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
                        print(f'User {command[5:]} has been banned.')
                    else:
                        print(f'There is no user with a nickname {command[5:]}.')
            elif command.lower() == 'kickall':
                for user in self.clients:
                    user.transport.close()

            command = await ainput()

    async def start(self):
        loop = asyncio.get_running_loop()
        coroutine = await loop.create_server(
            self.build_protocol,
            '127.0.0.1',
            8888
        )

        print("The server is running ...")

        await coroutine.serve_forever()


process = Server()


async def main():
    await asyncio.gather(process.start(), process.listening())


try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("The server is stopped manually.")
