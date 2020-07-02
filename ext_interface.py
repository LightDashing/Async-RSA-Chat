from PySide2.QtWidgets import QLineEdit
from PySide2.QtGui import QImage
from PySide2.QtGui import QKeySequence
import PySide2
import uuid
import os


class FileLineEdit(QLineEdit):
    filepath = None
    window = None

    def __init__(self, parent):
        super(FileLineEdit, self).__init__(parent)
        # self.window = parent

        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            event.acceptProposedAction()

    def dropEvent(self, event):
        data = event.mimeData()
        if event.mimeData().hasImage():
            image = QImage(event.mimeData().imageData())
            self.filepath = f"{os.getcwd()}/cache/{str(uuid.uuid4())}.jpg"
            image.save(self.filepath)
            return
        urls = data.urls()
        if urls and urls[0].scheme() == 'file':
            # for some reason, this doubles up the intro slash
            self.filepath = str(urls[0].path())[1:]

    def keyPressEvent(self, arg__1: PySide2.QtGui.QKeyEvent):
        if arg__1.matches(QKeySequence.Paste):
            self.window.paste()
        else:
            super(FileLineEdit, self).keyPressEvent(arg__1)
