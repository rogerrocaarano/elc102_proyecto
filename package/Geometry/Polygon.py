from PySide6.QtGui import QPolygonF


class Polygon(QPolygonF):
    def __init__(self, point_list: list):
        super().__init__()
        for point in point_list:
            self.append(point)
