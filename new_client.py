#
# Клиентское приложение с интерфейсом
#
import asyncio
from asyncio import transports
from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2 import QtGui
from asyncqt import QEventLoop
from main_interface import Ui_MainWindow
from Settings import Settings
import pickle
from Crypto.PublicKey import RSA
from Encryption import encrypt, decrypt


class ClientProtocol(asyncio.Protocol):
    transport: transports.Transport
    window: 'MainWindow'
    public = None

    def __init__(self, chat_window: 'MainWindow'):
        self.window = chat_window
        self.Settings = Settings()
        data = self.Settings.get_settings()
        self.keys = RSA.generate(2048)
        self.private = self.keys.export_key()
        self.private = RSA.import_key(self.private)
        self.login = data['login']
        self.password = data['password']
        self.email = data['email']

    def data_received(self, data: bytes):
        pack = pickle.loads(data)

        if pack['state'] == 1:
            self.public = pack['public']
            self.public = RSA.import_key(self.public)
            return

        message = decrypt(self.private, pack['message'])
        message = f'{pack["login"]}: {message}'
        self.window.append_text(message)

    def send_data(self, message: str):
        message = encrypt(self.public, message)

        pack = {'login': self.login, 'password': self.password, 'email': self.email, 'message': message, 'state': None}
        pack = pickle.dumps(pack)
        self.transport.write(pack)

    def connection_made(self, transport: transports.Transport):
        self.window.append_text("Подключено")
        self.transport = transport
        pack = {'login': self.login, 'password': self.password, 'email': self.email,
                'public_key': self.keys.publickey().export_key()}
        pack = pickle.dumps(pack)
        self.transport.write(pack)

    def connection_lost(self, exception):
        self.window.append_text("Отключено")


class MainWindow(QMainWindow, Ui_MainWindow):
    protocol: ClientProtocol

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.settings = Settings()
        self.user_settings = self.settings.get_settings()
        self.username_input.setText(self.user_settings['login'])
        self.password_input.setText(self.user_settings['password'])
        self.email_input.setText(self.user_settings['email'])
        self.user_settings = self.settings.get_settings()
        self.ip = None
        self.port = None

        self.s_list_model = QtGui.QStandardItemModel()
        self.server_list.setModel(self.s_list_model)

        self.send_message_button.clicked.connect(self.button_handler)
        self.save_user_button.clicked.connect(self.save_user)
        self.servers: dict = self.user_settings['servers']
        for k, v in self.servers.items():
            row = f'{k} {v["ip"]}:{v["port"]}'
            row = QtGui.QStandardItem(row)
            self.s_list_model.appendRow(row)

        self.send_message_button.clicked.connect(self.send_button_handler)
        self.connect_server_button.clicked.connect(self.connect_button_handler)
        self.disconnect_server_button.clicked.connect(self.disconnect_button_handler)
        self.delete_server_button.clicked.connect(self.delete_server)
        self.add_server_button.clicked.connect(self.add_server)
        self.show()

    def servers_changed(self):
        self.user_settings['servers'] = self.servers
        self.settings.set_settings(self.user_settings)

    def send_button_handler(self):
        message_text = self.message_input.text()
        self.message_input.clear()
        self.protocol.send_data(message_text)

    def add_server(self):
        name = self.ip_servername.text()
        ip = self.ip_input.text()
        port = self.port_input.text()
        server = f'{name} {ip}:{port}'
        server = QtGui.QStandardItem(server)
        self.s_list_model.appendRow(server)
        self.servers[name] = {'ip': ip, 'port': port}
        self.servers_changed()

    def delete_server(self):
        item = self.server_list.selectedIndexes()[0]

        server = str(item.data())
        server = server[:server.find(" ")]
        for k in self.servers.keys():
            if k == server:
                self.servers.pop(k)
                self.server_list.model().removeRow(item.row())
                break
        self.servers_changed()

    def connect_button_handler(self):
        item = self.server_list.selectedIndexes()[0]
        item = str(item.data())
        event_loop = asyncio.get_running_loop()
        event_loop.create_task(self.start(item[item.find(" ") + 1:item.rfind(":")], item[item.find(":") + 1:]))

    def disconnect_button_handler(self):
        self.protocol.transport.close()

    def append_text(self, content: str):
        self.message_box.appendPlainText(content)

    def save_user(self):
        username = self.username_input.text()
        password = self.password_input.text()
        email = self.email_input.text()
        self.user_settings['login'] = username
        self.user_settings['password'] = password
        self.user_settings['email'] = email
        self.settings.set_settings(self.user_settings)

    def build_protocol(self):
        self.protocol = ClientProtocol(self)
        return self.protocol

    async def start(self, ip, port):

        event_loop = asyncio.get_running_loop()

        coroutine = event_loop.create_connection(
            self.build_protocol,
            ip,
            port
        )
        await asyncio.wait_for(coroutine, 1000)


app = QApplication()
loop = QEventLoop(app)
asyncio.set_event_loop(loop)

window = MainWindow()

# loop.create_task(window.start()
loop.run_forever()