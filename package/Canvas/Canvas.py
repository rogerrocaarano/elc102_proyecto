from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap, QColor, QPolygonF, QPainter
from PySide6.QtCore import QLineF, QPointF
from icecream import ic

import package.globals as gl


class Canvas(QLabel):
    def __init__(self, window, width, height, color=QColor("black")):
        super().__init__()
        # Canvas properties
        self.window = window
        self.pixmap = QPixmap(width, height)
        self.drawed_objects = []
        self.bg_color = color

        self.pixmap.fill(self.bg_color)
        self.setPixmap(self.pixmap)
        self.setMouseTracking(True)

    def clear(self):
        """
        Clear the canvas
        :return:
        """
        self.pixmap.fill(QColor("black"))
        self.setPixmap(self.pixmap)

    def draw_polygon(self, polygon: QPolygonF, color=QColor("white")):
        """
        Draw a polygon on the canvas
        :param polygon: Polygon to be drawn
        :param color: Color of the polygon
        :return:
        """
        painter = QPainter(self.pixmap)
        painter.setPen(color)
        painter.drawPolygon(polygon)
        self.setPixmap(self.pixmap)

    def draw_line(self, point_a: QPointF, point_b: QPointF, color=QColor("white")):
        """
        Draw a line on the canvas
        :param point_a: Point A
        :param point_b: Point B
        :param color: Color of the line
        :return:
        """
        line = QLineF(point_a, point_b)
        painter = QPainter(self.pixmap)
        painter.setPen(color)
        painter.drawLine(line)
        self.setPixmap(self.pixmap)

    def mousePressEvent(self, ev):
        if gl.debug:
            ic("Canvas::mousePressEvent", ev.pos())
        if self.window.draw_events.drawing == "line":
            self.window.draw_events.draw_line_event(self, ev)
        elif self.window.draw_events.drawing == "square":
            self.window.draw_events.draw_square_event(self, ev)
        elif self.window.draw_events.drawing == "rectangle":
            self.window.draw_events.draw_rectangle_event(self, ev)
        elif self.window.draw_events.drawing == "triangle":
            self.window.draw_events.draw_triangle_event(self, ev)
        elif self.window.draw_events.drawing == "polygon":
            self.window.draw_events.draw_polygon_event(self, ev)

    def contextMenuEvent(self, ev):
        if gl.debug:
            ic("Canvas::contextMenuEvent", ev.pos())
        if self.window.draw_events.drawing == "polygon":
            self.window.draw_events.draw_polygon_event(self, ev, True)

    def mouseMoveEvent(self, ev):
        if gl.debug:
            ic("Canvas::mouseMoveEvent", ev.pos())
        pos = ev.pos()
        self.window.update_canvas_pos(pos.x(), pos.y())
