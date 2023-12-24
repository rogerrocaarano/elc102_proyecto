from PySide6.QtGui import QPolygonF, QColor, QPainter


class Polygon(QPolygonF):
    def __init__(self, point_list: list, outline_color=QColor("white")):
        super().__init__()
        self.outline_color = outline_color
        for point in point_list:
            self.append(point)

    def draw(self, canvas, outline_color=None):
        painter = QPainter(canvas.pixmap)
        if outline_color is not None:
            painter.setPen(outline_color)
        else:
            painter.setPen(self.outline_color)
        painter.drawPolygon(self)
        canvas.setPixmap(canvas.pixmap)
