from PySide6.QtWidgets import QApplication

from package.Interface.MainWindow import MainWindow


def create_ui():
    app = QApplication()
    MainWindow()
    app.exec()

