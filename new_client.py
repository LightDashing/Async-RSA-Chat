#
# Клиентское приложение с интерфейсом
#
import asyncio
import sys,time
from asyncio import transports
from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox
from PySide2 import QtGui, QtWidgets
from asyncqt import QEventLoop
from main_interface import Ui_MainWindow
from Settings import Settings
import pickle
from Crypto.PublicKey import RSA
from Encryption import encrypt, decrypt
from PySide2.QtGui import QIcon


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
        self.color = data['color']

    def data_received(self, data: bytes):
        pack = pickle.loads(data)

        if pack['state'] == 1:
            self.public = pack['public']
            self.public = RSA.import_key(self.public)
            return

        if pack['state'] == 3 or pack['state'] == 4 or pack['state'] == 2:
            self.window.append_text(pack['message'])
            return
        if pack['state'] == 5:
            yellowtext = "<span style=\" font-weight:600; color:#540099;\" >"
            yellowtext += decrypt(self.private, pack['message'])
            yellowtext += "</span>"
            self.window.append_text(yellowtext)
            return

        if pack['state'] == 6:
            blue = ""
            message = decrypt(self.private, pack['message'])
            message = f'<span style=\" font-weight: 400; font-style: normal; color:white; font-size: 11px;\" >{time.strftime("%H:%M", time.localtime())}</span> ' \
                      f'<span style=\"color: {pack["color"]}; font-weight: 400; font-style: normal;\">  {pack["login"]}: </span>{message} '
            blue += f"<span style=\" font-weight: 400; font-style: italic; color: orange;\" > {message}</span>"
            self.window.append_text(blue)
            return

        if pack['state'] == 7:
            yellowtext = "<span style=\" font-weight: 600; color: #540099;\" >"
            yellowtext += decrypt(self.private, pack['message'])
            yellowtext += "</span>"
            self.window.append_text(yellowtext)
            return

        message = decrypt(self.private, pack['message'])
        message = f'<span style=\" font-weight: 400; color: white; font-size: 11px;\" >{time.strftime("%H:%M", time.localtime())}</span>' \
                  f'<span style=\"color: {pack["color"]}\">  {pack["login"]}: </span> {message}'
        message = "<span style=\" font-size: 13px; color: white;\" >" + message
        self.window.append_text(message)

    def send_data(self, message: str):
        message = encrypt(self.public, message)
        pack = {'login': self.login, 'email': self.email, 'message': message, 'state': None, 'color': self.color}
        pack = pickle.dumps(pack)
        self.transport.write(pack)

    def send_pm(self, message: str, to: str = None, state: int = 2):
        msg = message
        if message != 'Empty':
            message = encrypt(self.public, message)
            pack = {"login": self.login, 'email': self.email, 'message': message, 'to': to, 'state': state,
                    'color': self.color}
            blue = f'<span style=\"font-weight: 400; font-size: 11px;\" >{time.strftime("%H:%M", time.localtime())}</span>'
            blue += f'<span style=\"color: {pack["color"]}\"> {pack["login"]}: </span> <span style=\"' \
                    f'font-weight: 400; font-style: italic; color: orange;\" > {msg}</span>'
            self.window.append_text(blue)
            pack = pickle.dumps(pack)
        else:
            message = encrypt(self.public, message)
            pack = {"login": self.login, 'email': self.email, 'message': message, 'state': state, "color": self.color}
            pack = pickle.dumps(pack)
        self.transport.write(pack)

    def connection_made(self, transport: transports.Transport):
        redText = "<span style=\" font-weight: 600; color: #00e600;\" >"
        redText += "Connected!"
        redText += "</span>"
        self.window.append_text(redText)
        self.transport = transport
        pack = {'login': self.login, 'password': self.password, 'email': self.email,
                'public_key': self.keys.publickey().export_key()}
        pack = pickle.dumps(pack)
        self.transport.write(pack)

    def connection_lost(self, exception):
        greenText = "<span style=\" font-weight: 600; color: #ff0000;\" >"
        greenText += "Disconnected!"
        greenText += "</span>"
        self.window.running = False
        self.window.append_text(greenText)


class MainWindow(QMainWindow, Ui_MainWindow):
    protocol: ClientProtocol

    def closeEvent(self, event):
        print(event)
        close = QMessageBox.question(self,
                                     "QUIT",
                                     "Are you sure want to stop process?",
                                     QMessageBox.Yes | QMessageBox.No)
        if close == QMessageBox.Yes:
            event.accept()
            sys.exit(0)
        else:
            event.ignore()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # self.setStyleSheet(open('./style.css').read())
        self.setStyleSheet(open('./dark_theme.css').read())

        self.settings = Settings()
        self.user_settings = self.settings.get_settings()
        self.username_input.setText(self.user_settings['login'])
        self.password_input.setText(self.user_settings['password'])
        self.email_input.setText(self.user_settings['email'])
        self.color_input.setText(self.user_settings['color'])
        self.user_settings = self.settings.get_settings()
        self.ip = None
        self.port = None
        self.running = False

        self.s_list_model = QtGui.QStandardItemModel()
        self.server_list.setModel(self.s_list_model)

        self.save_user_button.clicked.connect(self.save_user)
        self.servers: dict = self.user_settings['servers']
        for k, v in self.servers.items():
            row = f'{k} {v["ip"]}:{v["port"]}'
            row = QtGui.QStandardItem(row)
            self.s_list_model.appendRow(row)

        self.server_list.clicked.connect(self.make_buttons_active)
        self.send_message_button.clicked.connect(self.send_button_handler)
        self.connect_server_button.clicked.connect(self.connect_button_handler)
        self.connect_server_button.setEnabled(False)
        self.disconnect_server_button.clicked.connect(self.disconnect_button_handler)
        self.delete_server_button.clicked.connect(self.delete_server)
        self.delete_server_button.setEnabled(False)
        self.add_server_button.clicked.connect(self.add_server)
        self.reconnect_server_button.clicked.connect(self.reconnect)
        self.clean_chat_button.clicked.connect(self.clean_chat)
        self.show()


    def create_error(self, error: str):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(error)
        msg.setWindowTitle("Error")
        msg.exec_()

    def clean_chat(self):
        self.message_box.clear()

    def servers_changed(self):
        self.user_settings['servers'] = self.servers
        self.settings.set_settings(self.user_settings)

    def make_buttons_active(self):
        self.connect_server_button.setEnabled(True)
        self.delete_server_button.setEnabled(True)

    # def spacestr(str):
    def send_button_handler(self):
        message_text = self.message_input.text()
        if message_text == "":
            return
        count = 0
        for i in message_text:
            if i.isspace():
                count+=1
        if count == len(message_text):
            return

        if message_text[:3] == "!pm":
            user_login = message_text[4:message_text.rfind(":")]
            message_text = message_text[message_text.rfind(":") + 1:]
            self.protocol.send_pm(message_text, user_login)
            self.message_input.clear()
            return
        if message_text.lower() == "!list":
            self.protocol.send_pm(state=3, message='Empty')
            self.message_input.clear()
            return

        self.message_input.clear()
        self.protocol.send_data(message_text)

    def add_server(self):
        name = self.ip_servername.text()
        ip = self.ip_input.text()
        if not ip or not name:
            self.create_error('You need to add server IP address and name')
            return
        port = self.port_input.text()
        server = f'{name} {ip}:{port}'
        server = QtGui.QStandardItem(server)
        self.s_list_model.appendRow(server)
        self.servers[name] = {'ip': ip, 'port': port}
        self.servers_changed()

    def reconnect(self):
        event_loop = asyncio.get_running_loop()
        self.protocol.transport.close()
        event_loop.create_task(self.start(self.ip, self.port))

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
        self.ip = item[item.find(" ") + 1:item.rfind(":")]
        self.port = item[item.find(":") + 1:]
        if self.running:
            self.create_error('You need to disconnect from server first!')
            return
        event_loop.create_task(self.start(self.ip, self.port))
        self.tabWidget.setCurrentWidget(self.tab_chat)

    def disconnect_button_handler(self):
        self.protocol.transport.close()

    def append_text(self, content: str):
        self.message_box.append(content)

    def save_user(self):
        username = self.username_input.text()
        password = self.password_input.text()
        email = self.email_input.text()
        color = self.color_input.text()
        if not username or not password or not email:
            self.create_error('all fields must not be empty')
            return
        self.user_settings['login'] = username
        self.user_settings['password'] = password
        self.user_settings['email'] = email
        self.user_settings['color'] = color
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
        try:
            await asyncio.wait_for(coroutine, 5)
            self.running = True
        except (ConnectionRefusedError, ConnectionError, OSError):
            self.create_error('Connection Error')


# dark_stylesheet = qdarkstyle.load_stylesheet_pyside2()
app = QApplication()
app.setWindowIcon(QIcon("icon.png"))
# app.setStyleSheet("dark_theme.css")
loop = QEventLoop(app)
asyncio.set_event_loop(loop)

window = MainWindow()

# loop.create_task(window.start()
loop.run_forever()
