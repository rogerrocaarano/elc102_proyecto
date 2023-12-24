from PySide6.QtGui import QPolygonF, QPainter, QColor
from PySide6.QtCore import QPointF


class Square(QPolygonF):
    def __init__(self, top_left: QPointF, size: float, outline_color=QColor("white")):
        super().__init__()
        self.outline_color = outline_color
        x = top_left.x()
        y = top_left.y()
        bottom_left = QPointF(x, y + size)
        top_right = QPointF(x + size, y)
        bottom_right = QPointF(x + size, y + size)
        self.append(top_left)
        self.append(top_right)
        self.append(bottom_right)
        self.append(bottom_left)
        self.append(top_left)

    def draw(self, canvas):
        painter = QPainter(canvas.pixmap)
        painter.setPen(self.outline_color)
        painter.drawPolygon(self)
        canvas.setPixmap(canvas.pixmap)
