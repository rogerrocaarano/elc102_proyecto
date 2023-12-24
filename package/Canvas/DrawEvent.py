from PySide6.QtWidgets import QColorDialog
from PySide6.QtCore import QLineF

from package.Geometry.Polygon import Polygon
from package.Geometry.Rectangle import Rectangle
from package.Geometry.Square import Square
from package.Geometry.Triangle import Triangle


class DrawEvent:
    def __init__(self, canvas):
        self.canvas = canvas
        self.drawing = None
        self.first_point = None
        self.points = []

    def clear_action_triggered(self):
        """
        Triggered when the user clicks on the clear action
        :return:
        """
        self.canvas.clear()

    def change_bg_color_action_triggered(self):
        """
        Triggered when the user clicks on the change background color action
        :return:
        """
        color = QColorDialog.getColor()
        if color.isValid():
            self.canvas.bg_color = color

    def change_brush_color_action_triggered(self):
        """
        Triggered when the user clicks on the change brush color action
        :return:
        """
        color = QColorDialog.getColor()
        if color.isValid():
            self.canvas.draw_color = color

    def draw_line_action_triggered(self):
        """
        Triggered when the user clicks on the draw line action
        :return:
        """
        self.drawing = "line"
        self.first_point = None

    def draw_line_event(self, canvas, ev, polyline=False):
        """
        Triggered when the user clicks on the canvas while drawing a line
        :param polyline:
        :param canvas: Canvas object where the line will be drawn
        :param ev: Event object
        :return:
        """
        if self.first_point is None:
            self.first_point = ev.pos()
        else:
            point_b = ev.pos()
            line = QLineF(self.first_point, point_b)
            canvas.draw_line(line)
            self.first_point = None
            self.drawing = None
            if not polyline:
                canvas.temp_drawing_object = None

    def draw_line_temp_event(self, canvas, ev):
        """
        Triggered when the user moves the mouse on the canvas while drawing a line
        :param canvas: Canvas object where the line will be drawn
        :param ev: Event object
        :return:
        """
        if canvas.temp_drawing_object is not None:
            canvas.clear()
        canvas.temp_drawing_object = QLineF(self.first_point, ev.pos())
        canvas.draw_line(canvas.temp_drawing_object)

    def draw_square_action_triggered(self):
        """
        Triggered when the user clicks on the draw square action
        :return:
        """
        self.drawing = "square"
        self.first_point = None

    def draw_square_event(self, canvas, ev):
        """
        Triggered when the user clicks on the canvas while drawing a square
        :param canvas: Canvas object where the square will be drawn
        :param ev: Event object
        :return:
        """
        if self.first_point is None:
            self.first_point = ev.pos()
        else:
            size = ev.pos().x() - self.first_point.x()
            square = Square(self.first_point, size, canvas.draw_color)
            square.draw(canvas)
            self.drawing = None

    def draw_rectangle_action_triggered(self):
        """
        Triggered when the user clicks on the draw rectangle action
        :return:
        """
        self.drawing = "rectangle"
        self.first_point = None

    def draw_rectangle_event(self, canvas, ev):
        """
        Triggered when the user clicks on the canvas while drawing a rectangle
        :param canvas: Canvas object where the rectangle will be drawn
        :param ev: Event object
        :return:
        """
        if self.first_point is None:
            self.first_point = ev.pos()
        else:
            bottom_right = ev.pos()
            rectangle = Rectangle(self.first_point, bottom_right, canvas.draw_color)
            rectangle.draw(canvas)
            self.drawing = None

    def draw_triangle_action_triggered(self):
        """
        Triggered when the user clicks on the draw triangle action
        :return:
        """
        self.drawing = "triangle"
        self.first_point = None

    def draw_triangle_event(self, canvas, ev):
        """
        Triggered when the user clicks on the canvas while drawing a triangle
        :param canvas: Canvas object where the triangle will be drawn
        :param ev: Event object
        :return:
        """
        if not self.points:
            self.points.append(ev.pos())
        elif len(self.points) < 2:
            self.points.append(ev.pos())
        else:
            triangle = Triangle(self.points[0], self.points[1], ev.pos(), canvas.draw_color)
            triangle.draw(canvas)
            self.drawing = None
            self.points = []

    def draw_polygon_action_triggered(self):
        """
        Triggered when the user clicks on the draw polygon action
        :return:
        """
        self.drawing = "polygon"
        self.first_point = None

    def draw_polygon_event(self, canvas, ev, close_signal=False):
        """
        Triggered when the user clicks on the canvas while drawing a polygon
        :param canvas: Canvas object where the polygon will be drawn
        :param ev: Event object
        :param close_signal: If True, the polygon will be closed
        :return:
        """
        if close_signal and len(self.points) > 2:
            self.points.append(self.points[0])
            polygon = Polygon(self.points)
            polygon.draw(canvas)
            self.drawing = None
            self.points = []
        else:
            self.points.append(ev.pos())
