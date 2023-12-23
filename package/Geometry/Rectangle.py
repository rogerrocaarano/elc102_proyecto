from PySide6.QtGui import QPolygonF
from PySide6.QtCore import QPointF


class Rectangle(QPolygonF):
    def __init__(self, top_left: QPointF, bottom_right: QPointF):
        super().__init__()
        bottom_left = QPointF(top_left.x(), bottom_right.y())
        top_right = QPointF(bottom_right.x(), top_left.y())
        self.append(top_left)
        self.append(top_right)
        self.append(bottom_right)
        self.append(bottom_left)
        self.append(top_left)
