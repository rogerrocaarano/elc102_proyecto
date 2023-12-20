from PySide6.QtGui import QPolygonF
from PySide6.QtCore import QPointF


class Triangle(QPolygonF):
    def __init__(self, p1: QPointF, p2: QPointF, p3: QPointF):
        super().__init__()
        self << p1 << p2 << p3 << p1
