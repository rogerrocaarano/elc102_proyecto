from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QMainWindow

from package.Canvas.Canvas import Canvas
from package.Canvas.DrawEvent import DrawEvent
from package.MainWindow.MenuBar import MenuBar
from package.MainWindow.StatusBar import StatusBar


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.canvas = Canvas(self, 1024, 768)
        self.draw_events = DrawEvent(self.canvas)
        self.menu_bar = MenuBar(self.draw_events)
        self.status_bar = StatusBar()

        # Create window
        self.setWindowTitle("Proyecto ELC102")
        self.setStatusBar(self.status_bar)
        self.setMenuBar(self.menu_bar)
        self.setCentralWidget(self.canvas)

        # Impedir que la ventana sea redimensionada
        self.setFixedSize(self.sizeHint())
        self.center_on_screen()
        self.show()

    def update_canvas_pos(self, pos_x: int, pos_y: int):
        self.status_bar.update_pos(pos_x, pos_y)

    def keyPressEvent(self, event):
        self.canvas.keyPressEvent(event)

    def center_on_screen(self):
        # Obtener la pantalla principal
        screen = QGuiApplication.primaryScreen()
        # Obtener la geometría de la pantalla
        screen_geometry = screen.availableGeometry()
        # Obtener la geometría de la ventana
        window_geometry = self.frameGeometry()
        # Centrar la ventana en la pantalla
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())
