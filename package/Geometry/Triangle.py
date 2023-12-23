from PySide6.QtGui import QPolygonF
from PySide6.QtCore import QPointF


class Triangle(QPolygonF):
    def __init__(self, p1: QPointF, p2: QPointF, p3: QPointF):
        super().__init__()
        self.append(p1)
        self.append(p2)
        self.append(p3)
        self.append(p1)
