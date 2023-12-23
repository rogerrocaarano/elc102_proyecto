from PySide6.QtGui import QPolygonF
from PySide6.QtCore import QPointF


class Square(QPolygonF):
    def __init__(self, top_left: QPointF, size: float):
        super().__init__()
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
