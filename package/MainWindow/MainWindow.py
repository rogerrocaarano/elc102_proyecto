from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QEvent
from icecream import ic

from package.Canvas.Canvas import Canvas
from package.MainWindow.MenuBar import MenuBar
from package.MainWindow.StatusBar import StatusBar

from package.MainWindow.MainWindowController import MainWindowController

import package.globals as gl

debug = True


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Proyecto ELC102")
        self.controller = MainWindowController(self)
        canvas = Canvas(self.controller, 1280, 720)
        self.setStatusBar(StatusBar(self.controller))
        self.setMenuBar(MenuBar(self.controller))
        self.setCentralWidget(canvas)
        self.show()

    def resizeEvent(self, event: QEvent):
        if gl.debug:
            ic("MainWindow::resizeEvent", self.width(), self.height())
