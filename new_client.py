#
# Клиентское приложение с интерфейсом
#
import asyncio
import sys
import time
from asyncio import transports
import subprocess, os, platform

from cache import get_bytes, save_bytes, clear_cache
import webbrowser as wb
from PySide2 import QtGui, QtWidgets
from PySide2.QtCore import QUrl, Qt
from PySide2.QtGui import QIcon, QDesktopServices, QImage
from PySide2.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog, QShortcut
from asyncqt import QEventLoop
from interface import Ui_MainWindow
from Settings import Settings
import pickle
from Crypto.PublicKey import RSA
from Encryption import encrypt, decrypt, encrypt_bytes, decrypt_bytes
import uuid


class ClientProtocol(asyncio.Protocol):
    transport: transports.Transport
    window: 'MainWindow'
    public = None

    def __init__(self, chat_window: 'MainWindow'):
        self.window = chat_window
        self.Settings = Settings()
        self.settings = self.Settings.get_settings()
        self.keys = RSA.generate(2048)
        self.private = self.keys.export_key()
        self.private = RSA.import_key(self.private)
        self.login = self.settings['login']
        self.password = self.settings['password']
        self.email = self.settings['email']
        self.color = self.settings['color']
        self.file_to_send = None
        self.data = []
        self.start_time = None

    def data_received(self, data: bytes):
        filepath = None
        ext = None
        images = ['.png', '.jpg', '.gif', 'jpeg']

        try:
            pack = pickle.loads(data)
            if type(pack) != dict:
                raise Exception
        except Exception:
            self.data.append(data)
            try:
                pack = pickle.loads(b''.join(self.data))
                self.data.clear()
            except pickle.UnpicklingError:
                return
        if pack['state'] == 1:
            self.public = pack['public']
            self.public = RSA.import_key(self.public)
            return

        if pack['state'] == 3 or pack['state'] == 4 or pack['state'] == 2:
            self.window.append_text(pack['message'])
            return
        if pack['state'] == 5:
            yellowtext = f'<span style=\" font-weight:600;font-size:{self.settings["font-size"]}; color:#540099;\" >'
            yellowtext += decrypt(self.private, pack['message'])
            yellowtext += "</span>"
            self.window.append_text(yellowtext)
            return

        if pack['state'] == 6:
            blue = ""
            message = decrypt(self.private, pack['message'])
            message = f'<span style=\" font-weight: 400; font-style: normal; color:{self.window.text_color}; font-size: ' \
                      f'{self.settings["font-size"]};\" >{time.strftime("%H:%M", time.localtime())}</span> ' \
                      f'<span style=\"color: {pack["color"]}; font-weight: 400; font-style: ' \
                      f'{self.settings["font"]};\">  {pack["login"]}: </span>{message} '
            blue += f'<span style=\" font-weight: 400;font-size: {self.settings["font-size"]}; ' \
                    f'font-style: italic; color: orange;\" > {message}</span>'
            self.window.append_text(blue)
            return

        if pack['state'] == 7:
            yellowtext = "<span style=\" font-weight: 600; color: #540099;\" >"
            yellowtext += decrypt(self.private, pack['message'])
            yellowtext += "</span>"
            self.window.append_text(yellowtext)
            return

        if pack['state'] == 8:
            file = decrypt_bytes(self.private, pack['attach'])
            ext = pack["fname"][pack["fname"].rfind("."):]
            if ext in images:
                pack["fname"] = f'{str(uuid.uuid4())}{ext}'
            save_bytes(b=file, file=pack["fname"])
            filepath = f'{os.getcwd()}/cache/{pack["fname"]}'

        if pack['state'] == 14:
            blue = ""
            message = decrypt(self.private, pack['message'])
            message = f'<span style=\" font-weight: 400; font-style: normal; color:{self.window.text_color}; font-size: ' \
                      f'{self.settings["font-size"]};\" >{time.strftime("%H:%M", time.localtime())}</span> ' \
                      f'<span style=\"color: {pack["color"]}; font-weight: 400; font-style: ' \
                      f'{self.settings["font"]};\">  {pack["login"]}: </span>{message} '
            blue += f'<span style=\" font-weight: 400;font-size: {self.settings["font-size"]}; ' \
                    f'font-style: italic; color: orange;\" > {message}</span>'
            file = decrypt_bytes(self.private, pack['attach'])
            ext = pack["fname"][pack["fname"].rfind("."):]
            filepath = f'{os.getcwd()}/cache/{pack["fname"]}'
            if ext in images:
                pack["fname"] = f'{str(uuid.uuid4())}{ext}'
                filepath = f'{os.getcwd()}/cache/{pack["fname"]}'
                blue += f'<br> <a href="{filepath}"><img src="{filepath}" width="200" style=' \
                        f'"position: absolute; top: 0px; right: 0px;"></a><br>'
            else:
                blue += f' ||| <a href="{filepath}">{pack["fname"]}</a>'
            save_bytes(b=file, file=pack["fname"])
            self.window.append_text(blue)
            print('private picture')
            return

        message = decrypt(self.private, pack['message'])
        message = f'<span style=\" font-weight: 400; color:{self.window.text_color}; font-size: {self.settings["font-size"]};\" >{time.strftime("%H:%M", time.localtime())}</span>' \
                  f'<span style=\"color: {pack["color"]}\">  {pack["login"]}: </span> {message}'
        message = f'<span style=\" font-size: {self.settings["font-size"]}+2px; color:{self.window.text_color};\" >' + message
        if ext in images:
            message = message + f'<br> <a href="{filepath}"><img src="{filepath}" width="200" style="' \
                                f'position: absolute; top: 0px; right: 0px;"></a><br>'
        elif filepath is not None:
            message = message + f' ||| <a href="{filepath}">{pack["fname"]}</a> '
            # TODO: Сделать ссылку на файл картинкой
        self.window.append_text(message)

    def send_data(self, message: str, state=None):
        message = encrypt(self.public, message)
        pack = {'login': self.login, 'email': self.email, 'message': message, 'state': state, 'color': self.color}
        self.send_file(pack)
        pack = pickle.dumps(pack)
        self.transport.write(pack)

    def send_file(self, content: dict):
        if self.file_to_send is not None:
            filename = self.file_to_send
            self.file_to_send = get_bytes(self.file_to_send)
            enc_file = encrypt_bytes(self.public, self.file_to_send)
            content['attach'] = enc_file
            content['fname'] = filename[filename.rfind("/") + 1:]
            print(content['fname'])
            content['state'] = 4
            self.start_time = time.time()
            self.file_to_send = None

    def send_pm(self, message: str, to: str = None, state: int = 2):
        msg = message
        if state == 2:
            message = encrypt(self.public, message)
            pack = {"login": self.login, 'email': self.email, 'message': message, 'to': to, 'state': state,
                        'color': self.color}
            self.send_file(pack)
            if pack['state'] == 4:
                pack['state'] = 6
            print(pack['state'])
            blue = f'<span style=\"font-weight: 400; color:{self.window.text_color}; font-size: ' \
                   f'{self.settings["font-size"]};\" >{time.strftime("%H:%M", time.localtime())}</span>'
            blue += f'<span style=\"color: {self.settings["color"]}\"> {pack["login"]}: </span> <span style=\"' \
                    f'font-weight: 400; font-style: italic; color: orange;\" > {msg}</span>'
            self.window.append_text(blue)
            pack = pickle.dumps(pack)
        elif state == 3:
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
                'public_key': self.keys.publickey().export_key(), 'color': self.color}
        print(self.color)
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
        self.settings = Settings()
        self.user_settings = self.settings.get_settings()
        self.username_input.setText(self.user_settings['login'])
        self.password_input.setText(self.user_settings['password'])
        self.email_input.setText(self.user_settings['email'])
        if self.user_settings['app_theme'] == 'light':
            self.text_color = 'color:#000000'
        else:
            self.text_color = 'color:#ffffff'
        self.theme = f"./{self.user_settings['app_theme']}_theme.css"
        self.setStyleSheet(open(self.theme).read())

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

        self.message_input.window = self
        self.paste_bind = QShortcut(QtGui.QKeySequence(Qt.CTRL + Qt.Key_V), self.tab_chat)
        self.paste_bind.activated.connect(self.paste)
        self.paste_bind.setEnabled(True)
        self.color_input.setText(self.user_settings['color'])
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
        self.theme_button.clicked.connect(self.theme_changer)
        self.send_file_button.clicked.connect(self.send_file)
        self.message_box.anchorClicked.connect(self.file_onAnchorClicked)
        self.open_cache_button.clicked.connect(lambda: wb.open(f'{os.getcwd()}/cache/'))
        self.clear_cache_button.clicked.connect(clear_cache)
        self.show()

    def file_onAnchorClicked(self, url):
        if platform.system() == 'Darwin':       # macOS
            subprocess.call(('open', url.path()))
        elif platform.system() == 'Windows':    # Windows
            os.startfile(url.path())
        else:                                   # linux variants
            subprocess.call(('xdg-open', url.path()))

    def save_settings(self):
        font = self.font_input.text()
        font_size = self.font_size_input.text()
        theme = self.theme_input().text()
        color = self.color_input.text()
        if not font or not font_size or not color or not theme:
            self.create_error('All fields must not be empty.')
            return
        self.user_settings['font'] = font
        self.user_settings['font_size'] = font_size
        self.user_settings['app_theme'] = theme
        self.user_settings['color'] = color
        self.settings.set_settings(self.user_settings)

    def theme_changer(self):
        if self.user_settings['app_theme'] == 'light':
            self.user_settings['app_theme'] = 'dark'
            text = self.message_box.toHtml()
            text = text.replace('color:#000000', 'color:#ffffff')
            self.message_box.clear()
            self.message_box.insertHtml(text)
            self.theme_button.setText('Light theme')
        else:
            self.user_settings['app_theme'] = 'light'
            text = self.message_box.toHtml()
            text = text.replace('color:#ffffff', 'color:#000000')
            self.message_box.clear()
            self.message_box.insertHtml(text)
            self.theme_button.setText('Dark theme')
        self.settings.set_settings(self.user_settings)
        self.theme = f"./{self.user_settings['app_theme']}_theme.css"
        self.setStyleSheet(open(self.theme).read())
        self.update()

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

    def send_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "All files (*.*)")
        if fname[0] != '':
            self.protocol.file_to_send = fname[0]

    def send_button_handler(self):
        message_text = self.message_input.text()
        if self.message_input.filepath is not None:
            self.protocol.file_to_send = self.message_input.filepath
            self.message_input.filepath = None
        if message_text == "":
            return
        count = 0
        for i in message_text:
            if i.isspace():
                count += 1
        if count == len(message_text):
            return

        if message_text[:3].lower() == "!pm":
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
            self.create_error('All fields must not be empty.')
            return
        self.user_settings['login'] = username
        self.user_settings['password'] = password
        self.user_settings['email'] = email
        self.user_settings['color'] = color
        self.settings.set_settings(self.user_settings)

    def paste(self):
        clipboard = QApplication.clipboard()
        data = clipboard.mimeData()
        if data.hasImage():
            image = QImage(data.imageData())
            try:
                self.protocol.file_to_send = f"{os.getcwd()}/cache/{str(uuid.uuid4())}.jpg"
            except AttributeError:
                return
            image.save(self.protocol.file_to_send)
        elif data.hasText():
            self.message_input.insert(data.text())

    def build_protocol(self):
        self.protocol = ClientProtocol(self)
        return self.protocol

    # TODO: реализовать поиск серверов
    # Пока что это небольшая заглушка, но должна работать в теории
    async def ping_server(self, ip, port):
        event_loop = asyncio.get_running_loop()
        coroutine = event_loop.create_connection(
            self.build_protocol,
            ip,
            port
        )
        try:
            await asyncio.wait_for(coroutine, 5)
            coroutine.close()
            return ip, port
        except (ConnectionRefusedError, ConnectionError, OSError):
            return

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


app = QApplication()
app.setWindowIcon(QtGui.QIcon("logo.png"))
loop = QEventLoop(app)
asyncio.set_event_loop(loop)

window = MainWindow()

loop.run_forever()
