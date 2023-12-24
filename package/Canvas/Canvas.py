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
        self.temp_drawing_object = None
        self.bg_color = color
        self.draw_color = QColor("white")

        self.pixmap.fill(self.bg_color)
        self.setPixmap(self.pixmap)
        self.setMouseTracking(True)

    def clear(self):
        """
        Clear the canvas
        :return:
        """
        self.pixmap.fill(self.bg_color)
        self.setPixmap(self.pixmap)

    def redraw_objects(self):
        pass

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
        if self.window.draw_events.drawing == "line" and self.window.draw_events.first_point is not None:
            self.window.draw_events.draw_line_temp_event(self, ev)
