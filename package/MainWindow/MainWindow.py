from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow

from package.Canvas.Canvas import Canvas
from package.Canvas.DrawEvent import DrawEvent
from package.MainWindow.MenuBar import MenuBar
from package.MainWindow.StatusBar import StatusBar


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.canvas = Canvas(self, 1280, 720)
        self.draw_events = DrawEvent(self.canvas)
        self.menu_bar = MenuBar(self.draw_events)
        self.status_bar = StatusBar()

        # Create window
        self.setWindowTitle("Proyecto ELC102")
        self.setStatusBar(self.status_bar)
        self.setMenuBar(self.menu_bar)
        self.setCentralWidget(self.canvas)
        self.show()

    def update_canvas_pos(self, pos_x: int, pos_y: int):
        self.status_bar.update_pos(pos_x, pos_y)

    def keyPressEvent(self, event):
        self.canvas.keyPressEvent(event)
