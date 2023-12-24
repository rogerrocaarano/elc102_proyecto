from PySide6.QtCore import QPointF
from PySide6.QtWidgets import QColorDialog
from package.Geometry.Line import Line
from package.Geometry.Polygon import Polygon
from package.Geometry.Rectangle import Rectangle
from package.Geometry.Square import Square
from package.Geometry.Triangle import Triangle


class DrawEvent:
    def __init__(self, canvas):
        self.canvas = canvas
        self.drawing = None
        self.points = []

    def clean_action_triggered(self):
        """
        Triggered when the user clicks on the clean action
        :return:
        """
        self.canvas.clean()

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
        self.points = []

    def draw_line_mousePressEvent(self, canvas, ev, polyline=False):
        """
        Triggered when the user clicks on the canvas while drawing a line
        :param polyline:
        :param canvas: Canvas object where the line will be drawn
        :param ev: Event object
        :return:
        """
        self.points.append(ev.pos())
        if len(self.points) > 1:
            line = Line(self.points[-2], self.points[-1], canvas.draw_color)
            canvas.temp_drawing_object.append(line)
            if not polyline:
                line.draw(canvas)
                canvas.drawed_objects.append(line)
                self.drawing = None
                canvas.temp_drawing_object = []

    def draw_line_mouseMoveEvent(self, canvas, ev):
        """
        Triggered when the user moves the mouse on the canvas while drawing a line
        :param canvas: Canvas object where the line will be drawn
        :param ev: Event object
        :return:
        """
        canvas.redraw_objects()
        for obj in canvas.temp_drawing_object:
            obj.draw(canvas)
        line = Line(self.points[-1], ev.pos(), canvas.draw_color)
        line.draw(canvas)

    def draw_square_action_triggered(self):
        """
        Triggered when the user clicks on the draw square action
        :return:
        """
        self.drawing = "square"
        self.points = []

    def draw_square_mouseMoveEvent(self, canvas, ev):
        """
        Triggered when the user moves the mouse on the canvas while drawing a square
        :param canvas: Canvas object where the square will be drawn
        :param ev: Event object
        :return:
        """
        canvas.redraw_objects()
        size = ev.pos().x() - self.points[0].x()
        square = Square(self.points[0], size, canvas.draw_color)
        square.draw(canvas)
        canvas.temp_drawing_object = [square]

    def draw_square_mousePressEvent(self, canvas, ev):
        """
        Triggered when the user clicks on the canvas while drawing a square
        :param canvas: Canvas object where the square will be drawn
        :param ev: Event object
        :return:
        """
        if not self.points:
            self.points.append(ev.pos())
        else:
            size = ev.pos().x() - self.points[0].x()
            square = Square(self.points[0], size, canvas.draw_color)
            square.draw(canvas)
            canvas.drawed_objects.append(square)
            self.drawing = None

    def draw_rectangle_action_triggered(self):
        """
        Triggered when the user clicks on the draw rectangle action
        :return:
        """
        self.drawing = "rectangle"
        self.points = []

    def draw_rectangle_mouseMoveEvent(self, canvas, ev):
        """
        Triggered when the user moves the mouse on the canvas while drawing a rectangle
        :param canvas: Canvas object where the rectangle will be drawn
        :param ev: Event object
        :return:
        """
        canvas.redraw_objects()
        rectangle = Rectangle(self.points[0], ev.pos(), canvas.draw_color)
        rectangle.draw(canvas)
        canvas.temp_drawing_object = [rectangle]

    def draw_rectangle_mousePressEvent(self, canvas, ev):
        """
        Triggered when the user clicks on the canvas while drawing a rectangle
        :param canvas: Canvas object where the rectangle will be drawn
        :param ev: Event object
        :return:
        """
        if not self.points:
            self.points.append(ev.pos())
        else:
            rectangle = Rectangle(self.points[0], ev.pos(), canvas.draw_color)
            rectangle.draw(canvas)
            canvas.drawed_objects.append(rectangle)
            self.drawing = None

    def draw_triangle_action_triggered(self):
        """
        Triggered when the user clicks on the draw triangle action
        :return:
        """
        self.drawing = "triangle"
        self.points = []

    def draw_triangle_mouseMoveEvent(self, canvas, ev):
        """
        Triggered when the user moves the mouse on the canvas while drawing a triangle
        :param canvas: Canvas object where the triangle will be drawn
        :param ev: Event object
        :return:
        """
        self.draw_line_mouseMoveEvent(canvas, ev)

    def draw_triangle_mousePressEvent(self, canvas, ev):
        """
        Triggered when the user clicks on the canvas while drawing a triangle
        :param canvas: Canvas object where the triangle will be drawn
        :param ev: Event object
        :return:
        """
        self.draw_line_mousePressEvent(canvas, ev, True)
        if len(self.points) == 3:
            triangle = Triangle(self.points[0], self.points[1], self.points[2], canvas.draw_color)
            triangle.draw(canvas)
            canvas.drawed_objects.append(triangle)
            self.drawing = None

    def draw_polygon_action_triggered(self):
        """
        Triggered when the user clicks on the draw polygon action
        :return:
        """
        self.drawing = "polygon"
        self.points = []

    def draw_polygon_mouseMoveEvent(self, canvas, ev):
        """
        Triggered when the user moves the mouse on the canvas while drawing a polygon
        :param canvas: Canvas object where the polygon will be drawn
        :param ev: Event object
        :return:
        """
        self.draw_line_mouseMoveEvent(canvas, ev)

    def draw_polygon_mousePressEvent(self, canvas, ev, close_signal=False):
        """
        Triggered when the user clicks on the canvas while drawing a polygon
        :param canvas: Canvas object where the polygon will be drawn
        :param ev: Event object
        :param close_signal: If True, the polygon will be closed
        :return:
        """
        if close_signal and len(self.points) > 4:
            self.points.pop(-1)
            canvas.temp_drawing_object = []
            canvas.redraw_objects()
            self.points.append(self.points[0])
            polygon = Polygon(self.points)
            polygon.draw(canvas)
            canvas.drawed_objects.append(polygon)
            self.drawing = None
            self.points = []
        else:
            self.draw_line_mousePressEvent(canvas, ev, True)
