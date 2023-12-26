from PySide6.QtGui import QGuiApplication
from PySide6.QtOpenGL import QOpenGLWindow
from OpenGL import GL as gl
from PySide6.QtWidgets import QMenuBar, QMenu, QMainWindow
from pywavefront import Wavefront as wf

from package.OpenGlWindow.OpenglWidget import OpenglWidget


class OpenglWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu_bar = QMenuBar(self)

        # Create window
        self.setWindowTitle("3D Viewer")
        self.setMenuBar(self.menu_bar)
        self.setCentralWidget(OpenglWidget())

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
