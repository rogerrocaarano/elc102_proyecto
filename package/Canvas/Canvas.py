from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap, QColor
from icecream import ic

from package.MainWindow.MainWindowController import MainWindowController
import package.globals as gl


class Canvas(QLabel):
    def __init__(self, controller, width, height, color=QColor("black")):
        super().__init__()
        self.controller = controller
        self.pixmap = QPixmap(width, height)
        self.pixmap.fill(color)
        self.setPixmap(self.pixmap)
        # Habilitar seguimiento del mouse
        self.setMouseTracking(True)

    def mousePressEvent(self, ev):
        if gl.debug:
            ic("Canvas::mousePressEvent", ev.pos())

    def mouseMoveEvent(self, ev):
        if gl.debug:
            ic("Canvas::mouseMoveEvent", ev.pos())
        pos = ev.pos()
        controller: MainWindowController = self.controller
        controller.update_canvas_pos(pos.x(), pos.y())


