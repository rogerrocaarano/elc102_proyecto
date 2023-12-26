from PySide6.QtWidgets import QLabel, QColorDialog, QMenuBar, QMenu
from PySide6.QtGui import QPixmap, QColor
from PySide6.QtCore import Qt
from icecream import ic

import package.globals as gl
from package.Geometry.Line import Line
from package.Geometry.Polygon import Polygon
from package.Geometry.Rectangle import Rectangle
from package.Geometry.Square import Square
from package.Geometry.Triangle import Triangle
from package.Interface.MenuAction import MenuAction
from package.Interface.ModalIntersection import ModalIntersection


class Canvas(QLabel):
    def __init__(self, parent_window, width: int, height: int):
        super().__init__()
        # Canvas attributes
        self.pixmap = QPixmap(width, height)
        self.bg_color = QColor("black")
        self.draw_color = QColor("white")
        self.window = parent_window
        self.drawed_objects = []
        self.temp_drawing_object = []
        self.drawing = None
        self.points = []

        # Initialize canvas
        self.pixmap.fill(self.bg_color)
        self.setPixmap(self.pixmap)
        self.setMouseTracking(True)

    def add_canvas_actions(self, menu_bar: QMenuBar, menu: QMenu):
        """
        Add canvas actions to the menu bar
        :param menu_bar:
        :param menu:
        :return:
        """
        MenuAction("Limpiar lienzo", menu_bar, menu, self.clean_action_triggered)
        MenuAction("Cambiar color de fondo", menu_bar, menu, self.change_bg_color_action_triggered)
        MenuAction("Cambiar color del pincel", menu_bar, menu, self.change_brush_color_action_triggered)

    def add_draw_actions(self, menu_bar: QMenuBar, menu: QMenu):
        MenuAction("Línea", menu_bar, menu, self.draw_line_action_triggered)
        MenuAction("Cuadrado", menu_bar, menu, self.draw_square_action_triggered)
        MenuAction("Rectángulo", menu_bar, menu, self.draw_rectangle_action_triggered)
        MenuAction("Triángulo", menu_bar, menu, self.draw_triangle_action_triggered)
        MenuAction("Polígono", menu_bar, menu, self.draw_polygon_action_triggered)

    def clean(self):
        """
        Clean the canvas
        :return:
        """
        self.clear()
        self.drawed_objects = []
        self.temp_drawing_object = []
        self.pixmap.fill(self.bg_color)
        self.setPixmap(self.pixmap)

    def redraw_objects(self):
        """
        Redraw all objects in the canvas
        :return:
        """
        self.pixmap.fill(self.bg_color)
        self.setPixmap(self.pixmap)
        for obj in self.drawed_objects:
            obj.draw(self)

    def mousePressEvent(self, ev):
        if gl.debug:
            ic("Canvas::mousePressEvent", ev.pos())
        if self.drawing == "line":
            self.draw_line_mousePressEvent(ev)
        elif self.drawing == "square":
            self.draw_square_mousePressEvent(ev)
        elif self.drawing == "rectangle":
            self.draw_rectangle_mousePressEvent(ev)
        elif self.drawing == "triangle":
            self.draw_triangle_mousePressEvent(ev)
        elif self.drawing == "polygon":
            self.draw_polygon_mousePressEvent(ev)

    def contextMenuEvent(self, ev):
        if gl.debug:
            ic("Canvas::contextMenuEvent", ev.pos())
        if self.drawing == "polygon":
            self.draw_polygon_mousePressEvent(ev, True)

    def mouseMoveEvent(self, ev):
        pos = ev.pos()
        self.window.update_canvas_pos(pos.x(), pos.y())
        if self.drawing == "line" and self.points != []:
            self.draw_line_mouseMoveEvent(ev)
        elif self.drawing == "square" and self.points != []:
            self.draw_square_mouseMoveEvent(ev)
        elif self.drawing == "rectangle" and self.points != []:
            self.draw_rectangle_mouseMoveEvent(ev)
        elif self.drawing == "triangle" and self.points != []:
            self.draw_triangle_mouseMoveEvent(ev)
        elif self.drawing == "polygon" and self.points != []:
            self.draw_polygon_mouseMoveEvent(ev)

    def keyPressEvent(self, ev):
        if gl.debug:
            ic("Canvas::keyPressEvent", ev.key())
        # Move last object
        if ev.key() == Qt.Key_W:
            self.drawed_objects[-1].translate(0, -1)
        elif ev.key() == Qt.Key_S:
            self.drawed_objects[-1].translate(0, 1)
        elif ev.key() == Qt.Key_A:
            self.drawed_objects[-1].translate(-1, 0)
        elif ev.key() == Qt.Key_D:
            self.drawed_objects[-1].translate(1, 0)
        # Move previous object
        elif ev.key() == Qt.Key_Up:
            self.drawed_objects[-2].translate(0, -1)
        elif ev.key() == Qt.Key_Down:
            self.drawed_objects[-2].translate(0, 1)
        elif ev.key() == Qt.Key_Left:
            self.drawed_objects[-2].translate(-1, 0)
        elif ev.key() == Qt.Key_Right:
            self.drawed_objects[-2].translate(1, 0)
        self.redraw_objects()
        if len(self.drawed_objects) > 1:
            object1 = self.drawed_objects[-1]
            object2 = self.drawed_objects[-2]
            if object1.intersects(object2):
                ic("Intersects")
                modal = ModalIntersection()
                modal.exec()

    def clean_action_triggered(self):
        """
        Triggered when the user clicks on the clean action
        :return:
        """
        self.clean()

    def change_bg_color_action_triggered(self):
        """
        Triggered when the user clicks on the change background color action
        :return:
        """
        color = QColorDialog.getColor()
        if color.isValid():
            self.bg_color = color
            self.redraw_objects()

    def change_brush_color_action_triggered(self):
        """
        Triggered when the user clicks on the change brush color action
        :return:
        """
        color = QColorDialog.getColor()
        if color.isValid():
            self.draw_color = color

    def draw_line_action_triggered(self):
        """
        Triggered when the user clicks on the draw line action
        :return:
        """
        self.drawing = "line"
        self.points = []

    def draw_line_mousePressEvent(self, ev, polyline=False):
        """
        Triggered when the user clicks on the canvas while drawing a line
        :param polyline:
        :param ev: Event object
        :return:
        """
        self.points.append(ev.pos())
        if len(self.points) > 1:
            line = Line(self.points[-2], self.points[-1], self.draw_color)
            self.temp_drawing_object.append(line)
            if not polyline:
                line.draw(self)
                self.drawed_objects.append(line)
                self.drawing = None
                self.temp_drawing_object = []

    def draw_line_mouseMoveEvent(self, ev):
        """
        Triggered when the user moves the mouse on the canvas while drawing a line
        :param ev: Event object
        :return:
        """
        self.redraw_objects()
        for obj in self.temp_drawing_object:
            obj.draw(self)
        line = Line(self.points[-1], ev.pos(), self.draw_color)
        line.draw(self)

    def draw_square_action_triggered(self):
        """
        Triggered when the user clicks on the draw square action
        :return:
        """
        self.drawing = "square"
        self.points = []

    def draw_square_mouseMoveEvent(self, ev):
        """
        Triggered when the user moves the mouse on the canvas while drawing a square
        :param ev: Event object
        :return:
        """
        self.redraw_objects()
        size = ev.pos().x() - self.points[0].x()
        square = Square(self.points[0], size, self.draw_color)
        square.draw(self)
        self.temp_drawing_object = [square]

    def draw_square_mousePressEvent(self, ev):
        """
        Triggered when the user clicks on the canvas while drawing a square
        :param ev: Event object
        :return:
        """
        if not self.points:
            self.points.append(ev.pos())
        else:
            size = ev.pos().x() - self.points[0].x()
            square = Square(self.points[0], size, self.draw_color)
            square.draw(self)
            self.drawed_objects.append(square)
            self.drawing = None

    def draw_rectangle_action_triggered(self):
        """
        Triggered when the user clicks on the draw rectangle action
        :return:
        """
        self.drawing = "rectangle"
        self.points = []

    def draw_rectangle_mouseMoveEvent(self, ev):
        """
        Triggered when the user moves the mouse on the canvas while drawing a rectangle
        :param ev: Event object
        :return:
        """
        self.redraw_objects()
        rectangle = Rectangle(self.points[0], ev.pos(), self.draw_color)
        rectangle.draw(self)
        self.temp_drawing_object = [rectangle]

    def draw_rectangle_mousePressEvent(self, ev):
        """
        Triggered when the user clicks on the canvas while drawing a rectangle
        :param ev: Event object
        :return:
        """
        if not self.points:
            self.points.append(ev.pos())
        else:
            rectangle = Rectangle(self.points[0], ev.pos(), self.draw_color)
            rectangle.draw(self)
            self.drawed_objects.append(rectangle)
            self.drawing = None

    def draw_triangle_action_triggered(self):
        """
        Triggered when the user clicks on the draw triangle action
        :return:
        """
        self.drawing = "triangle"
        self.points = []

    def draw_triangle_mouseMoveEvent(self, ev):
        """
        Triggered when the user moves the mouse on the canvas while drawing a triangle
        :param ev: Event object
        :return:
        """
        self.draw_line_mouseMoveEvent(ev)

    def draw_triangle_mousePressEvent(self, ev):
        """
        Triggered when the user clicks on the canvas while drawing a triangle
        :param ev: Event object
        :return:
        """
        self.draw_line_mousePressEvent(ev, True)
        if len(self.points) == 3:
            triangle = Triangle(self.points[0], self.points[1], self.points[2], self.draw_color)
            triangle.draw(self)
            self.drawed_objects.append(triangle)
            self.drawing = None

    def draw_polygon_action_triggered(self):
        """
        Triggered when the user clicks on the draw polygon action
        :return:
        """
        self.drawing = "polygon"
        self.points = []

    def draw_polygon_mouseMoveEvent(self, ev):
        """
        Triggered when the user moves the mouse on the canvas while drawing a polygon
        :param ev: Event object
        :return:
        """
        self.draw_line_mouseMoveEvent(ev)

    def draw_polygon_mousePressEvent(self, ev, close_signal=False):
        """
        Triggered when the user clicks on the canvas while drawing a polygon
        :param ev: Event object
        :param close_signal: If True, the polygon will be closed
        :return:
        """
        if close_signal and len(self.points) > 4:
            self.points.pop(-1)
            self.temp_drawing_object = []
            self.redraw_objects()
            self.points.append(self.points[0])
            polygon = Polygon(self.points)
            polygon.draw(self)
            self.drawed_objects.append(polygon)
            self.drawing = None
            self.points = []
        else:
            self.draw_line_mousePressEvent(ev, True)
