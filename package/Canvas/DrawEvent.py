from PySide6.QtGui import QPolygonF

from package.Geometry.Polygon import Polygon
from package.Geometry.Rectangle import Rectangle
from package.Geometry.Square import Square
from package.Geometry.Triangle import Triangle


class DrawEvent:
    def __init__(self):
        self.drawing = None
        self.initial_point = None
        self.points = []

    def draw_line_action_triggered(self):
        """
        Triggered when the user clicks on the draw line action
        :return:
        """
        self.drawing = "line"
        self.initial_point = None

    def draw_line_event(self, canvas, ev):
        """
        Triggered when the user clicks on the canvas while drawing a line
        :param canvas: Canvas object where the line will be drawn
        :param ev: Event object
        :return:
        """
        if self.initial_point is None:
            self.initial_point = ev.pos()
        else:
            point_b = ev.pos()
            canvas.draw_line(self.initial_point, point_b)
            self.drawing = None

    def draw_square_action_triggered(self):
        """
        Triggered when the user clicks on the draw square action
        :return:
        """
        self.drawing = "square"
        self.initial_point = None

    def draw_square_event(self, canvas, ev):
        """
        Triggered when the user clicks on the canvas while drawing a square
        :param canvas: Canvas object where the square will be drawn
        :param ev: Event object
        :return:
        """
        if self.initial_point is None:
            self.initial_point = ev.pos()
        else:
            size = ev.pos().x() - self.initial_point.x()
            square = Square(self.initial_point, size)
            canvas.draw_polygon(square)
            self.drawing = None

    def draw_rectangle_action_triggered(self):
        """
        Triggered when the user clicks on the draw rectangle action
        :return:
        """
        self.drawing = "rectangle"
        self.initial_point = None

    def draw_rectangle_event(self, canvas, ev):
        """
        Triggered when the user clicks on the canvas while drawing a rectangle
        :param canvas: Canvas object where the rectangle will be drawn
        :param ev: Event object
        :return:
        """
        if self.initial_point is None:
            self.initial_point = ev.pos()
        else:
            bottom_right = ev.pos()
            rectangle = Rectangle(self.initial_point, bottom_right)
            canvas.draw_polygon(rectangle)
            self.drawing = None

    def draw_triangle_action_triggered(self):
        """
        Triggered when the user clicks on the draw triangle action
        :return:
        """
        self.drawing = "triangle"
        self.initial_point = None

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
            triangle = Triangle(self.points[0], self.points[1], ev.pos())
            canvas.draw_polygon(triangle)
            self.drawing = None
            self.points = []

    def draw_polygon_action_triggered(self):
        """
        Triggered when the user clicks on the draw polygon action
        :return:
        """
        self.drawing = "polygon"
        self.initial_point = None

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
            canvas.draw_polygon(polygon)
            self.drawing = None
            self.points = []
        else:
            self.points.append(ev.pos())
