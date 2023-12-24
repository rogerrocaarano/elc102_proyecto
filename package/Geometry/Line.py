from PySide6.QtCore import QLineF
from PySide6.QtGui import QColor, QPainter


class Line(QLineF):
    def __init__(self, p1, p2, color=QColor("white")):
        super().__init__(p1, p2)
        self.color = color

    def draw(self, canvas):
        painter = QPainter(canvas.pixmap)
        painter.setPen(self.color)
        painter.drawLine(self)
        canvas.setPixmap(canvas.pixmap)
