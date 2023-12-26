from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QMainWindow, QMenuBar

from package.Canvas.Canvas import Canvas
from package.Interface.StatusBar import StatusBar
from package.OpenGlWindow.OpenglWindow import OpenglWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.canvas = Canvas(self, 1024, 768)
        self.menu_bar = QMenuBar(self)
        self.status_bar = StatusBar()
        self.opengl_window = None

        # Create window
        self.setWindowTitle("Proyecto ELC102")
        self.setStatusBar(self.status_bar)
        self.setMenuBar(self.menu_bar)
        self.setCentralWidget(self.canvas)
        self.add_menu()

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

    def add_menu(self):
        canvas_menu = self.menu_bar.addMenu("Lienzo")
        self.canvas.add_canvas_actions(self.menu_bar, canvas_menu)
        draw_menu = self.menu_bar.addMenu("Dibujar")
        self.canvas.add_draw_actions(self.menu_bar, draw_menu)
        opengl_menu_action = self.menu_bar.addAction("3D Viewer")
        opengl_menu_action.triggered.connect(self.open_opengl_window)

    def open_opengl_window(self):
        opengl_window = OpenglWindow()
        opengl_window.setFixedSize(800, 600)
        opengl_window.center_on_screen()
        self.opengl_window = opengl_window
        self.opengl_window.show()

