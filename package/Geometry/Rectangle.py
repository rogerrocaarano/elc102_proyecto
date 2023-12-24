from PySide6.QtGui import QPolygonF, QColor, QPainter
from PySide6.QtCore import QPointF


class Rectangle(QPolygonF):
    def __init__(self, top_left: QPointF, bottom_right: QPointF, outline_color=QColor("white")):
        super().__init__()
        self.outline_color = outline_color
        bottom_left = QPointF(top_left.x(), bottom_right.y())
        top_right = QPointF(bottom_right.x(), top_left.y())
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
