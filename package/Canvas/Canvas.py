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
        self.temp_drawing_object = []
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
        """
        Redraw all objects in the canvas
        :return:
        """
        self.clear()
        for obj in self.drawed_objects:
            obj.draw(self)

    def mousePressEvent(self, ev):
        if gl.debug:
            ic("Canvas::mousePressEvent", ev.pos())
        if self.window.draw_events.drawing == "line":
            self.window.draw_events.draw_line_mousePressEvent(self, ev)
        elif self.window.draw_events.drawing == "square":
            self.window.draw_events.draw_square_mousePressEvent(self, ev)
        elif self.window.draw_events.drawing == "rectangle":
            self.window.draw_events.draw_rectangle_mousePressEvent(self, ev)
        elif self.window.draw_events.drawing == "triangle":
            self.window.draw_events.draw_triangle_mousePressEvent(self, ev)
        elif self.window.draw_events.drawing == "polygon":
            self.window.draw_events.draw_polygon_mousePressEvent(self, ev)

    def contextMenuEvent(self, ev):
        if gl.debug:
            ic("Canvas::contextMenuEvent", ev.pos())
        if self.window.draw_events.drawing == "polygon":
            self.window.draw_events.draw_polygon_mousePressEvent(self, ev, True)

    def mouseMoveEvent(self, ev):
        if gl.debug:
            ic("Canvas::mouseMoveEvent", ev.pos())
        pos = ev.pos()
        self.window.update_canvas_pos(pos.x(), pos.y())
        if self.window.draw_events.drawing == "line" and self.window.draw_events.points != []:
            self.window.draw_events.draw_line_mouseMoveEvent(self, ev)
        elif self.window.draw_events.drawing == "square" and self.window.draw_events.points != []:
            self.window.draw_events.draw_square_mouseMoveEvent(self, ev)
        elif self.window.draw_events.drawing == "rectangle" and self.window.draw_events.points != []:
            self.window.draw_events.draw_rectangle_mouseMoveEvent(self, ev)
        elif self.window.draw_events.drawing == "triangle" and self.window.draw_events.points != []:
            self.window.draw_events.draw_triangle_mouseMoveEvent(self, ev)
        elif self.window.draw_events.drawing == "polygon" and self.window.draw_events.points != []:
            self.window.draw_events.draw_polygon_mouseMoveEvent(self, ev)
