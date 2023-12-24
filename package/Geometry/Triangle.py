from PySide6.QtGui import QPolygonF, QPainter, QColor
from PySide6.QtCore import QPointF


class Triangle(QPolygonF):
    def __init__(self, p1: QPointF, p2: QPointF, p3: QPointF, outline_color=QColor("white")):
        super().__init__()
        self.outline_color = outline_color
        self.append(p1)
        self.append(p2)
        self.append(p3)
        self.append(p1)

    def draw(self, canvas):
        painter = QPainter(canvas.pixmap)
        painter.setPen(self.outline_color)
        painter.drawPolygon(self)
        canvas.setPixmap(canvas.pixmap)
