# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
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
from ext_interface import FileLineEdit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(578, 659)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setFixedSize(578, 659)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
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
        self.tab_user.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.tab_user)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.formLayout_user = QFormLayout()
        self.formLayout_user.setObjectName(u"formLayout_user")
        self.groupBox_registration = QGroupBox(self.tab_user)
        self.groupBox_registration.setObjectName(u"groupBox_registration")
        self.groupBox_registration.setAlignment(Qt.AlignCenter)
        self.groupBox_registration.setFlat(False)
        self.groupBox_registration.setCheckable(False)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_registration)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.formLayout_user_registration = QFormLayout()
        self.formLayout_user_registration.setObjectName(u"formLayout_user_registration")
        self.label_username = QLabel(self.groupBox_registration)
        self.label_username.setObjectName(u"label_username")
        self.label_username.setTextFormat(Qt.AutoText)
        self.label_username.setScaledContents(False)
        self.label_username.setWordWrap(False)

        self.formLayout_user_registration.setWidget(0, QFormLayout.LabelRole, self.label_username)

        self.username_input = QLineEdit(self.groupBox_registration)
        self.username_input.setObjectName(u"username_input")
        self.username_input.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.username_input.setClearButtonEnabled(True)

        self.formLayout_user_registration.setWidget(0, QFormLayout.FieldRole, self.username_input)

        self.label_password = QLabel(self.groupBox_registration)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setTextFormat(Qt.AutoText)
        self.label_password.setScaledContents(False)
        self.label_password.setWordWrap(False)

        self.formLayout_user_registration.setWidget(1, QFormLayout.LabelRole, self.label_password)

        self.password_input = QLineEdit(self.groupBox_registration)
        self.password_input.setObjectName(u"password_input")
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setClearButtonEnabled(True)

        self.formLayout_user_registration.setWidget(1, QFormLayout.FieldRole, self.password_input)

        self.label_email = QLabel(self.groupBox_registration)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setTextFormat(Qt.AutoText)
        self.label_email.setScaledContents(False)
        self.label_email.setWordWrap(False)

        self.formLayout_user_registration.setWidget(2, QFormLayout.LabelRole, self.label_email)

        self.email_input = QLineEdit(self.groupBox_registration)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setClearButtonEnabled(True)

        self.formLayout_user_registration.setWidget(2, QFormLayout.FieldRole, self.email_input)

        self.label_color = QLabel(self.groupBox_registration)
        self.label_color.setObjectName(u"label_color")
        self.label_color.setTextFormat(Qt.AutoText)
        self.label_color.setScaledContents(False)
        self.label_color.setWordWrap(False)

        self.formLayout_user_registration.setWidget(3, QFormLayout.LabelRole, self.label_color)

        self.color_input = QLineEdit(self.groupBox_registration)
        self.color_input.setObjectName(u"color_input")
        self.color_input.setClearButtonEnabled(True)

        self.formLayout_user_registration.setWidget(3, QFormLayout.FieldRole, self.color_input)

        self.save_user_button = QPushButton(self.groupBox_registration)
        self.save_user_button.setObjectName(u"save_user_button")

        self.formLayout_user_registration.setWidget(4, QFormLayout.SpanningRole, self.save_user_button)


        self.verticalLayout_4.addLayout(self.formLayout_user_registration)


        self.formLayout_user.setWidget(0, QFormLayout.SpanningRole, self.groupBox_registration)

        self.label_logo_image = QLabel(self.tab_user)
        self.label_logo_image.setObjectName(u"label_logo_image")
        self.label_logo_image.setPixmap(QPixmap(u"logo_image.png"))
        self.label_logo_image.setScaledContents(False)
        self.label_logo_image.setAlignment(Qt.AlignCenter)
        self.label_logo_image.setWordWrap(False)
        self.label_logo_image.setOpenExternalLinks(False)

        self.formLayout_user.setWidget(2, QFormLayout.SpanningRole, self.label_logo_image)

        self.verticalSpacer_logo_image = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout_user.setItem(1, QFormLayout.SpanningRole, self.verticalSpacer_logo_image)


        self.verticalLayout_8.addLayout(self.formLayout_user)

        self.label_version = QLabel(self.tab_user)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_8.addWidget(self.label_version)

        self.tabWidget.addTab(self.tab_user, "")
        self.tab_servers = QWidget()
        self.tab_servers.setObjectName(u"tab_servers")
        self.verticalLayout_7 = QVBoxLayout(self.tab_servers)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_servers = QHBoxLayout()
        self.horizontalLayout_servers.setObjectName(u"horizontalLayout_servers")
        self.groupBox_addserver = QGroupBox(self.tab_servers)
        self.groupBox_addserver.setObjectName(u"groupBox_addserver")
        self.groupBox_addserver.setAlignment(Qt.AlignCenter)
        self.verticalLayout_6 = QVBoxLayout(self.groupBox_addserver)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.formLayout_new_server = QFormLayout()
        self.formLayout_new_server.setObjectName(u"formLayout_new_server")
        self.label_server = QLabel(self.groupBox_addserver)
        self.label_server.setObjectName(u"label_server")

        self.formLayout_new_server.setWidget(0, QFormLayout.LabelRole, self.label_server)

        self.ip_servername = QLineEdit(self.groupBox_addserver)
        self.ip_servername.setObjectName(u"ip_servername")
        self.ip_servername.setClearButtonEnabled(True)

        self.formLayout_new_server.setWidget(0, QFormLayout.FieldRole, self.ip_servername)

        self.label_ip = QLabel(self.groupBox_addserver)
        self.label_ip.setObjectName(u"label_ip")

        self.formLayout_new_server.setWidget(1, QFormLayout.LabelRole, self.label_ip)

        self.ip_input = QLineEdit(self.groupBox_addserver)
        self.ip_input.setObjectName(u"ip_input")
        self.ip_input.setAutoFillBackground(False)
        self.ip_input.setMaxLength(15)
        self.ip_input.setFrame(True)
        self.ip_input.setInputMask("^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"
                                   "\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
        self.ip_input.setValidator(QRegExpValidator(self.ip_input.inputMask()))
        self.ip_input.setEchoMode(QLineEdit.Normal)

        self.formLayout_new_server.setWidget(1, QFormLayout.FieldRole, self.ip_input)

        self.add_server_button = QPushButton(self.groupBox_addserver)
        self.add_server_button.setObjectName(u"add_server_button")

        self.formLayout_new_server.setWidget(3, QFormLayout.SpanningRole, self.add_server_button)

        self.port_input = QSpinBox(self.groupBox_addserver)
        self.port_input.setObjectName(u"port_input")
        self.port_input.setMinimum(1000)
        self.port_input.setMaximum(65536)
        self.port_input.setSingleStep(1)

        self.formLayout_new_server.setWidget(2, QFormLayout.FieldRole, self.port_input)

        self.label_port = QLabel(self.groupBox_addserver)
        self.label_port.setObjectName(u"label_port")

        self.formLayout_new_server.setWidget(2, QFormLayout.LabelRole, self.label_port)


        self.verticalLayout_6.addLayout(self.formLayout_new_server)


        self.horizontalLayout_servers.addWidget(self.groupBox_addserver)

        self.groupBox_serverlist = QGroupBox(self.tab_servers)
        self.groupBox_serverlist.setObjectName(u"groupBox_serverlist")
        self.groupBox_serverlist.setStyleSheet(u"")
        self.groupBox_serverlist.setAlignment(Qt.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.groupBox_serverlist)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_servers_list = QGridLayout()
        self.gridLayout_servers_list.setObjectName(u"gridLayout_servers_list")
        self.delete_server_button = QPushButton(self.groupBox_serverlist)
        self.delete_server_button.setObjectName(u"delete_server_button")

        self.gridLayout_servers_list.addWidget(self.delete_server_button, 1, 0, 1, 1)

        self.connect_server_button = QPushButton(self.groupBox_serverlist)
        self.connect_server_button.setObjectName(u"connect_server_button")

        self.gridLayout_servers_list.addWidget(self.connect_server_button, 1, 1, 1, 1)

        self.server_list = QListView(self.groupBox_serverlist)
        self.server_list.setObjectName(u"server_list")

        self.gridLayout_servers_list.addWidget(self.server_list, 0, 0, 1, 2)


        self.verticalLayout.addLayout(self.gridLayout_servers_list)


        self.horizontalLayout_servers.addWidget(self.groupBox_serverlist)


        self.verticalLayout_7.addLayout(self.horizontalLayout_servers)

        self.tabWidget.addTab(self.tab_servers, "")
        self.tab_chat = QWidget()
        self.tab_chat.setObjectName(u"tab_chat")
        self.tab_chat.setEnabled(True)
        self.verticalLayout_3 = QVBoxLayout(self.tab_chat)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_chat = QGridLayout()
        self.gridLayout_chat.setObjectName(u"gridLayout_chat")
        self.clean_chat_button = QPushButton(self.tab_chat)
        self.clean_chat_button.setObjectName(u"clean_chat_button")

        self.gridLayout_chat.addWidget(self.clean_chat_button, 0, 2, 1, 1)

        self.send_file_button = QPushButton(self.tab_chat)
        self.send_file_button.setObjectName(u"send_file_button")

        self.gridLayout_chat.addWidget(self.send_file_button, 3, 2, 1, 1)

        self.message_box = QTextBrowser(self.tab_chat)
        self.message_box.setObjectName(u"message_box")
        self.message_box.setFrameShape(QFrame.StyledPanel)
        self.message_box.setReadOnly(True)
        self.message_box.setAcceptRichText(True)
        self.message_box.setOpenLinks(False)

        self.gridLayout_chat.addWidget(self.message_box, 1, 0, 1, 3)

        self.message_input = FileLineEdit(self.tab_chat)
        self.message_input.setObjectName(u"message_input")
        self.message_input.setDragEnabled(True)

        self.gridLayout_chat.addWidget(self.message_input, 2, 0, 1, 3)

        self.reconnect_server_button = QPushButton(self.tab_chat)
        self.reconnect_server_button.setObjectName(u"reconnect_server_button")

        self.gridLayout_chat.addWidget(self.reconnect_server_button, 0, 1, 1, 1)

        self.disconnect_server_button = QPushButton(self.tab_chat)
        self.disconnect_server_button.setObjectName(u"disconnect_server_button")

        self.gridLayout_chat.addWidget(self.disconnect_server_button, 0, 0, 1, 1)

        self.send_message_button = QPushButton(self.tab_chat)
        self.send_message_button.setObjectName(u"send_message_button")

        self.gridLayout_chat.addWidget(self.send_message_button, 3, 0, 1, 2)


        self.verticalLayout_3.addLayout(self.gridLayout_chat)

        self.tabWidget.addTab(self.tab_chat, "")
        self.tab_settings = QWidget()
        self.tab_settings.setObjectName(u"tab_settings")
        self.formLayout_5 = QFormLayout(self.tab_settings)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.verticalLayout_settings = QVBoxLayout()
        self.verticalLayout_settings.setObjectName(u"verticalLayout_settings")
        self.groupBox_theme = QGroupBox(self.tab_settings)
        self.groupBox_theme.setObjectName(u"groupBox_theme")
        self.groupBox_theme.setLayoutDirection(Qt.LeftToRight)
        self.groupBox_theme.setAlignment(Qt.AlignCenter)
        self.groupBox_theme.setFlat(False)
        self.groupBox_theme.setCheckable(False)
        self.verticalLayout_10 = QVBoxLayout(self.groupBox_theme)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.theme_button = QPushButton(self.groupBox_theme)
        self.theme_button.setObjectName(u"theme_button")

        self.verticalLayout_10.addWidget(self.theme_button)


        self.verticalLayout_settings.addWidget(self.groupBox_theme)

        self.groupBox_font = QGroupBox(self.tab_settings)
        self.groupBox_font.setObjectName(u"groupBox_font")
        self.groupBox_font.setAlignment(Qt.AlignCenter)
        self.groupBox_font.setFlat(False)
        self.groupBox_font.setCheckable(False)
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_font)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.formLayout_font_settings = QFormLayout()
        self.formLayout_font_settings.setObjectName(u"formLayout_font_settings")
        self.label_font_style = QLabel(self.groupBox_font)
        self.label_font_style.setObjectName(u"label_font_style")
        self.label_font_style.setTextFormat(Qt.AutoText)
        self.label_font_style.setScaledContents(False)
        self.label_font_style.setWordWrap(False)

        self.formLayout_font_settings.setWidget(0, QFormLayout.LabelRole, self.label_font_style)

        self.font_style_input = QLineEdit(self.groupBox_font)
        self.font_style_input.setObjectName(u"font_style_input")
        self.font_style_input.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.font_style_input.setClearButtonEnabled(True)

        self.formLayout_font_settings.setWidget(0, QFormLayout.FieldRole, self.font_style_input)

        self.label_font_size = QLabel(self.groupBox_font)
        self.label_font_size.setObjectName(u"label_font_size")
        self.label_font_size.setTextFormat(Qt.AutoText)
        self.label_font_size.setScaledContents(False)
        self.label_font_size.setWordWrap(False)

        self.formLayout_font_settings.setWidget(1, QFormLayout.LabelRole, self.label_font_size)

        self.font_size_input = QLineEdit(self.groupBox_font)
        self.font_size_input.setObjectName(u"font_size_input")
        self.font_size_input.setEchoMode(QLineEdit.Password)
        self.font_size_input.setClearButtonEnabled(True)

        self.formLayout_font_settings.setWidget(1, QFormLayout.FieldRole, self.font_size_input)

        self.label_font_color = QLabel(self.groupBox_font)
        self.label_font_color.setObjectName(u"label_font_color")
        self.label_font_color.setTextFormat(Qt.AutoText)
        self.label_font_color.setScaledContents(False)
        self.label_font_color.setWordWrap(False)

        self.formLayout_font_settings.setWidget(2, QFormLayout.LabelRole, self.label_font_color)

        self.font_color_input = QLineEdit(self.groupBox_font)
        self.font_color_input.setObjectName(u"font_color_input")
        self.font_color_input.setClearButtonEnabled(True)

        self.formLayout_font_settings.setWidget(2, QFormLayout.FieldRole, self.font_color_input)


        self.verticalLayout_9.addLayout(self.formLayout_font_settings)


        self.verticalLayout_settings.addWidget(self.groupBox_font)

        self.groupBox_cache = QGroupBox(self.tab_settings)
        self.groupBox_cache.setObjectName(u"groupBox_cache")
        self.groupBox_cache.setLayoutDirection(Qt.LeftToRight)
        self.groupBox_cache.setAlignment(Qt.AlignCenter)
        self.groupBox_cache.setFlat(False)
        self.groupBox_cache.setCheckable(False)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_cache)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.open_cache_button = QPushButton(self.groupBox_cache)
        self.open_cache_button.setObjectName(u"open_cache_button")

        self.horizontalLayout_2.addWidget(self.open_cache_button)

        self.clear_cache_button = QPushButton(self.groupBox_cache)
        self.clear_cache_button.setObjectName(u"clear_cache_button")

        self.horizontalLayout_2.addWidget(self.clear_cache_button)


        self.verticalLayout_settings.addWidget(self.groupBox_cache)


        self.formLayout_5.setLayout(0, QFormLayout.SpanningRole, self.verticalLayout_settings)

        self.save_settings_button = QPushButton(self.tab_settings)
        self.save_settings_button.setObjectName(u"save_settings_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.save_settings_button.sizePolicy().hasHeightForWidth())
        self.save_settings_button.setSizePolicy(sizePolicy2)

        self.formLayout_5.setWidget(1, QFormLayout.SpanningRole, self.save_settings_button)

        self.tabWidget.addTab(self.tab_settings, "")

        self.verticalLayout_2.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Async RSA Chat", None))
        self.groupBox_registration.setTitle(QCoreApplication.translate("MainWindow", u"User registration", None))
        self.label_username.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.username_input.setText("")
        self.username_input.setPlaceholderText("")
        self.label_password.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.password_input.setPlaceholderText("")
        self.label_email.setText(QCoreApplication.translate("MainWindow", u"E-mail", None))
        self.email_input.setPlaceholderText("")
        self.label_color.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.color_input.setText("")
        self.color_input.setPlaceholderText("")
        self.save_user_button.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.save_user_button.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.label_logo_image.setText("")
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"1.15 beta", None))
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
#if QT_CONFIG(shortcut)
        self.delete_server_button.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
#endif // QT_CONFIG(shortcut)
        self.connect_server_button.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
#if QT_CONFIG(shortcut)
        self.connect_server_button.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_servers), QCoreApplication.translate("MainWindow", u"Servers", None))
        self.clean_chat_button.setText(QCoreApplication.translate("MainWindow", u"Clean", None))
        self.send_file_button.setText(QCoreApplication.translate("MainWindow", u"File", None))
        self.reconnect_server_button.setText(QCoreApplication.translate("MainWindow", u"Reconnect", None))
        self.disconnect_server_button.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.send_message_button.setText(QCoreApplication.translate("MainWindow", u"Send", None))
#if QT_CONFIG(shortcut)
        self.send_message_button.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_chat), QCoreApplication.translate("MainWindow", u"Chat", None))
        self.groupBox_theme.setTitle(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.theme_button.setText(QCoreApplication.translate("MainWindow", u"Dark theme", None))
        self.groupBox_font.setTitle(QCoreApplication.translate("MainWindow", u"Font", None))
        self.label_font_style.setText(QCoreApplication.translate("MainWindow", u"Style", None))
        self.font_style_input.setText("")
        self.font_style_input.setPlaceholderText("")
        self.label_font_size.setText(QCoreApplication.translate("MainWindow", u"Size", None))
        self.font_size_input.setPlaceholderText("")
        self.label_font_color.setText(QCoreApplication.translate("MainWindow", u"Color", None))
        self.font_color_input.setPlaceholderText("")
        self.groupBox_cache.setTitle(QCoreApplication.translate("MainWindow", u"Cache", None))
        self.open_cache_button.setText(QCoreApplication.translate("MainWindow", u"Open cache directory", None))
        self.clear_cache_button.setText(QCoreApplication.translate("MainWindow", u"Clear cache", None))
        self.save_settings_button.setText(QCoreApplication.translate("MainWindow", u"Save changes", None))
#if QT_CONFIG(shortcut)
        self.save_settings_button.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_settings), QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

