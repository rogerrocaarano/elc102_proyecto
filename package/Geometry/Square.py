from PySide6.QtGui import QPolygonF
from PySide6.QtCore import QPointF


class Square(QPolygonF):
    def __init__(self, x: float, y: float, size: float):
        super().__init__()
        top_left = QPointF(x, y)
        bottom_left = QPointF(x, y + size)
        top_right = QPointF(x + size, y)
        bottom_right = QPointF(x + size, y + size)
        self << top_left << top_right << bottom_right << bottom_left << top_left
