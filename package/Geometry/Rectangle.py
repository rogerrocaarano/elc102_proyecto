from PySide6.QtGui import QPolygonF
from PySide6.QtCore import QPointF


class Rectangle(QPolygonF):
    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        super().__init__()
        top_left = QPointF(x1, y1)
        bottom_left = QPointF(x1, y2)
        top_right = QPointF(x2, y1)
        bottom_right = QPointF(x2, y2)
        self << top_left << top_right << bottom_right << bottom_left << top_left
