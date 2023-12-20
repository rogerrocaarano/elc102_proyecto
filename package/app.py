from PySide6.QtWidgets import QApplication

from package.MainWindow.MainWindow import MainWindow


def create_ui():
    app = QApplication()
    window = MainWindow()
    app.exec()

