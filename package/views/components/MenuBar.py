from PySide6.QtWidgets import QMenuBar
from PySide6.QtGui import QAction

from package.controllers.MainWindowController import MainWindowController as Controller


class MenuBar(QMenuBar):
    def __init__(self, controller: Controller):
        super().__init__()
        self.controller = controller
        menu_draw = [
            QAction("Línea", self),
            QAction("Cuadrado", self),
            QAction("Rectángulo", self),
            QAction("Triángulo", self),
            QAction("Polígono", self)
        ]
        menu_canvas = [
            QAction("Clear", self),
            QAction("Change background Color", self),
            QAction("Change brush Color", self)
        ]
        menu_bar = {
            "Dibujar": menu_draw,
            "Canvas": menu_canvas
        }
        for title, actions in menu_bar.items():
            menu = self.addMenu(title)
            for action in actions:
                menu.addAction(action)
