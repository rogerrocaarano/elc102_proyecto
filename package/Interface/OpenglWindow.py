from PySide6.QtGui import QGuiApplication
from PySide6.QtWidgets import QMenuBar, QMenu, QMainWindow

from package.Interface.MenuAction import MenuAction
from package.OpenglObjectViewer.Viewer import Viewer


class OpenglWindow(QMainWindow):
    def __init__(self, file_path):
        super().__init__()
        self.menu_bar = QMenuBar(self)
        camera_menu = QMenu("Cámaras", self)
        self.menu_bar.addMenu(camera_menu)
        self.add_menu_camera(self.menu_bar, camera_menu)

        self.viewer = Viewer(file_path)

        # Create window
        self.setWindowTitle("3D Viewer")
        self.setMenuBar(self.menu_bar)
        self.setCentralWidget(self.viewer)
        self.center_on_screen()

    def center_on_screen(self):
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

    def add_menu_camera(self, menu_bar: QMenuBar, menu: QMenu):
        MenuAction("Ángulo 1", menu_bar, menu, self.set_angle_1)
        MenuAction("Ángulo 2", menu_bar, menu, self.set_angle_2)

    def set_angle_1(self):
        self.viewer.set_camera_position_multiplier(1.2, 2, 3)
        self.viewer.update()

    def set_angle_2(self):
        self.viewer.set_camera_position_multiplier(0, 0, 3)
        self.viewer.update()
