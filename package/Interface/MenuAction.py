from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenuBar, QMenu


class MenuAction(QAction):
    def __init__(self, text: str, menu_bar: QMenuBar, menu: QMenu, action):
        super().__init__(text, menu_bar)
        self.triggered.connect(action)
        menu.addAction(self)
