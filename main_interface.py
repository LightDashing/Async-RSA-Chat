# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
                            QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QRegExp)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
                           QPixmap, QRadialGradient, QRegExpValidator)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(583, 659)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setFixedSize(578, 659)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setStyleSheet(u"")
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(False)

        self.tab_user = QWidget()
        self.tab_user.setObjectName(u"tab_user")
        self.verticalLayout_4 = QVBoxLayout(self.tab_user)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_registration = QGroupBox(self.tab_user)
        self.groupBox_registration.setObjectName(u"groupBox_registration")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_registration)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label_username = QLabel(self.groupBox_registration)
        self.label_username.setObjectName(u"label_username")
        self.label_username.setTextFormat(Qt.AutoText)
        self.label_username.setScaledContents(False)
        self.label_username.setWordWrap(False)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_username)

        self.username_input = QLineEdit(self.groupBox_registration)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.username_input.setClearButtonEnabled(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.username_input)

        self.label_password = QLabel(self.groupBox_registration)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setTextFormat(Qt.AutoText)
        self.label_password.setScaledContents(False)
        self.label_password.setWordWrap(False)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_password)

        self.password_input = QLineEdit(self.groupBox_registration)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setClearButtonEnabled(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.password_input)

        self.label_email = QLabel(self.groupBox_registration)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setTextFormat(Qt.AutoText)
        self.label_email.setScaledContents(False)
        self.label_email.setWordWrap(False)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_email)

        self.email_input = QLineEdit(self.groupBox_registration)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setClearButtonEnabled(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.email_input)

        self.label_color = QLabel(self.groupBox_registration)
        self.label_color.setObjectName(u"label_color")
        self.label_color.setTextFormat(Qt.AutoText)
        self.label_color.setScaledContents(False)
        self.label_color.setWordWrap(False)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_color)

        self.color_input = QLineEdit(self.groupBox_registration)
        self.color_input.setObjectName(u"color_input")
        self.color_input.setClearButtonEnabled(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.color_input)

        self.save_user_button = QPushButton(self.groupBox_registration)
        self.save_user_button.setObjectName(u"save_user_button")

        self.formLayout.setWidget(4, QFormLayout.SpanningRole, self.save_user_button)

        self.verticalLayout_5.addLayout(self.formLayout)


        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.label_logo_image = QLabel(self.groupBox_registration)
        self.label_logo_image.setObjectName(u"label_logo_image")
        self.label_logo_image.setPixmap(QPixmap(u"logo_image.png"))
        self.label_logo_image.setScaledContents(False)
        self.label_logo_image.setAlignment(Qt.AlignCenter)
        self.label_logo_image.setWordWrap(False)
        self.label_logo_image.setOpenExternalLinks(False)

        self.verticalLayout_5.addWidget(self.label_logo_image)

        self.verticalLayout_4.addWidget(self.groupBox_registration)

        self.groupBox_app_settings = QGroupBox(self.tab_user)
        self.groupBox_app_settings.setObjectName(u"groupBox_app_settings")
        self.verticalLayout_8 = QVBoxLayout(self.groupBox_app_settings)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")

        self.theme_button = QPushButton(self.groupBox_app_settings)
        self.theme_button.setObjectName(u"theme_button")

        self.verticalLayout_8.addWidget(self.theme_button)

        self.verticalLayout_4.addWidget(self.groupBox_app_settings)


        self.tabWidget.addTab(self.tab_user, "")
        self.tab_servers = QWidget()
        self.tab_servers.setObjectName(u"tab_servers")
        self.verticalLayout_7 = QVBoxLayout(self.tab_servers)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_addserver = QGroupBox(self.tab_servers)
        self.groupBox_addserver.setObjectName(u"groupBox_addserver")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_addserver)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_server = QLabel(self.groupBox_addserver)
        self.label_server.setObjectName(u"label_server")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_server)

        self.ip_servername = QLineEdit(self.groupBox_addserver)
        self.ip_servername.setObjectName(u"ip_servername")
        self.ip_servername.setClearButtonEnabled(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.ip_servername)

        self.label_ip = QLabel(self.groupBox_addserver)
        self.label_ip.setObjectName(u"label_ip")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_ip)

        self.ip_input = QLineEdit(self.groupBox_addserver)
        self.ip_input.setObjectName(u"ip_input")
        self.ip_input.setAutoFillBackground(False)
        self.ip_input.setMaxLength(15)
        self.ip_input.setFrame(True)
        self.ip_input.setInputMask("^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
                                   "\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
        self.ip_input.setValidator(QRegExpValidator(self.ip_input.inputMask()))

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.ip_input)

        self.add_server_button = QPushButton(self.groupBox_addserver)
        self.add_server_button.setObjectName(u"add_server_button")

        self.formLayout_2.setWidget(3, QFormLayout.SpanningRole, self.add_server_button)

        self.port_input = QSpinBox(self.groupBox_addserver)
        self.port_input.setObjectName(u"port_input")
        self.port_input.setMinimum(1000)
        self.port_input.setMaximum(65536)
        self.port_input.setSingleStep(1)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.port_input)

        self.label_port = QLabel(self.groupBox_addserver)
        self.label_port.setObjectName(u"label_port")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_port)


        self.verticalLayout_6.addLayout(self.formLayout_2)


        self.horizontalLayout.addWidget(self.groupBox_addserver)

        self.groupBox_serverlist = QGroupBox(self.tab_servers)
        self.groupBox_serverlist.setObjectName(u"groupBox_serverlist")
        self.groupBox_serverlist.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.groupBox_serverlist)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.server_list = QListView(self.groupBox_serverlist)
        self.server_list.setObjectName(u"server_list")

        self.gridLayout.addWidget(self.server_list, 0, 0, 1, 2)

        self.delete_server_button = QPushButton(self.groupBox_serverlist)
        self.delete_server_button.setObjectName(u"delete_server_button")

        self.gridLayout.addWidget(self.delete_server_button, 1, 0, 1, 1)

        self.connect_server_button = QPushButton(self.groupBox_serverlist)
        self.connect_server_button.setObjectName(u"connect_server_button")

        self.gridLayout.addWidget(self.connect_server_button, 1, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.horizontalLayout.addWidget(self.groupBox_serverlist)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.tabWidget.addTab(self.tab_servers, "")
        self.tab_chat = QWidget()
        self.tab_chat.setObjectName(u"tab_chat")
        self.tab_chat.setEnabled(True)
        self.verticalLayout_3 = QVBoxLayout(self.tab_chat)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.disconnect_server_button = QPushButton(self.tab_chat)
        self.disconnect_server_button.setObjectName(u"disconnect_server_button")

        self.gridLayout_2.addWidget(self.disconnect_server_button, 0, 0, 1, 1)

        self.reconnect_server_button = QPushButton(self.tab_chat)
        self.reconnect_server_button.setObjectName(u"reconnect_server_button")

        self.gridLayout_2.addWidget(self.reconnect_server_button, 0, 1, 1, 1)

        self.clean_chat_button = QPushButton(self.tab_chat)
        self.clean_chat_button.setObjectName(u"clean_chat_button")

        self.gridLayout_2.addWidget(self.clean_chat_button, 0, 2, 1, 1)

        self.message_box = QTextBrowser(self.tab_chat)
        self.message_box.setObjectName(u"message_box")
        self.message_box.setFrameShape(QFrame.StyledPanel)
        self.message_box.setReadOnly(True)
        self.message_box.setOpenExternalLinks(False)
        self.message_box.setOpenLinks(False)
        self.message_box.setAcceptRichText(True)

        self.gridLayout_2.addWidget(self.message_box, 1, 0, 1, 3)

        self.message_input = QLineEdit(self.tab_chat)
        self.message_input.setObjectName(u"message_input")

        self.gridLayout_2.addWidget(self.message_input, 2, 0, 1, 3)

        self.send_file_button = QPushButton(self.tab_chat)
        self.send_file_button.setObjectName(u"send_file_button")

        self.gridLayout_2.addWidget(self.send_file_button, 3, 2, 1, 1)

        self.send_message_button = QPushButton(self.tab_chat)
        self.send_message_button.setObjectName(u"send_message_button")

        self.gridLayout_2.addWidget(self.send_message_button, 3, 0, 1, 2)


        self.verticalLayout_3.addLayout(self.gridLayout_2)

        self.tabWidget.addTab(self.tab_chat, "")

        self.tab_settings = QWidget()
        self.tab_settings.setObjectName(u"tab_settings")
        self.tabWidget.addTab(self.tab_settings, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"RSA Chat", None))
        self.groupBox_registration.setTitle(QCoreApplication.translate("MainWindow", u"User registration", None))
        self.label_username.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.username_input.setText("")
        # self.username_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        # self.password_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password (at least 6 characters)", None))
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        # self.email_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.label_color.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.save_user_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.groupBox_app_settings.setTitle(QCoreApplication.translate("MainWindow", u"App settings", None))
        self.theme_button.setText(QCoreApplication.translate("MainWindow", u"Dark theme", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_user), QCoreApplication.translate("MainWindow", u"User", None))
        self.groupBox_addserver.setTitle(QCoreApplication.translate("MainWindow", u"New server", None))
        self.label_server.setText(QCoreApplication.translate("MainWindow", u"Server's name", None))
        self.label_ip.setText(QCoreApplication.translate("MainWindow", u"IP adress", None))
        self.ip_input.setInputMask("")
        self.ip_input.setText("")
        self.add_server_button.setText(QCoreApplication.translate("MainWindow", u"Add server", None))
        self.label_port.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.groupBox_serverlist.setTitle(QCoreApplication.translate("MainWindow", u"Servers list", None))
        self.delete_server_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.connect_server_button.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_servers), QCoreApplication.translate("MainWindow", u"Servers", None))
        self.disconnect_server_button.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.send_message_button.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_chat), QCoreApplication.translate("MainWindow", u"Chat", None))
    #if QT_CONFIG(shortcut)
        self.delete_server_button.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
    #endif // QT_CONFIG(shortcut)
        self.connect_server_button.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
    #if QT_CONFIG(shortcut)
        self.connect_server_button.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
    #endif // QT_CONFIG(shortcut)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_servers), QCoreApplication.translate("MainWindow", u"Servers", None))
        self.disconnect_server_button.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.reconnect_server_button.setText(QCoreApplication.translate("MainWindow", u"Reconnect", None))
        self.clean_chat_button.setText(QCoreApplication.translate("MainWindow", u"Clean", None))
        self.send_file_button.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.send_message_button.setText(QCoreApplication.translate("MainWindow", u"Send", None))
    #if QT_CONFIG(shortcut)
        self.send_message_button.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings),
                                  QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

