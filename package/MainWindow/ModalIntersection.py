from PySide6.QtWidgets import QMessageBox


class ModalIntersection(QMessageBox):
    def __init__(self, parent=None):
        super(ModalIntersection, self).__init__(parent)
        self.setIcon(QMessageBox.Information)
        self.setWindowTitle('Coalición detectada')
        self.setText('Se detectó una coalición entre las figuras.')
        self.setStandardButtons(QMessageBox.Ok)
