from PySide6.QtWidgets import QMenuBar
from PySide6.QtGui import QAction

from package.Canvas.DrawEvent import DrawEvent


class MenuBar(QMenuBar):
    def __init__(self, draw_event: DrawEvent):
        super().__init__()
        # Window
        self.draw_events = draw_event
        # Canvas menu
        canvas_menu = self.addMenu("Lienzo")
        # Actions
        clean_action = QAction("Limpiar lienzo", self)
        clean_action.triggered.connect(self.draw_events.clean_action_triggered)
        canvas_menu.addAction(clean_action)

        change_bg_color_action = QAction("Cambiar color de fondo", self)
        change_bg_color_action.triggered.connect(self.draw_events.change_bg_color_action_triggered)
        canvas_menu.addAction(change_bg_color_action)

        change_brush_color_action = QAction("Cambiar color del pincel", self)
        change_brush_color_action.triggered.connect(self.draw_events.change_brush_color_action_triggered)
        canvas_menu.addAction(change_brush_color_action)

        # Draw menu
        draw_menu = self.addMenu("Dibujar")
        # Actions
        draw_line_action = QAction("Línea", self)
        draw_line_action.triggered.connect(self.draw_events.draw_line_action_triggered)
        draw_menu.addAction(draw_line_action)

        draw_square_action = QAction("Cuadrado", self)
        draw_square_action.triggered.connect(self.draw_events.draw_square_action_triggered)
        draw_menu.addAction(draw_square_action)

        draw_rectangle_action = QAction("Rectángulo", self)
        draw_rectangle_action.triggered.connect(self.draw_events.draw_rectangle_action_triggered)
        draw_menu.addAction(draw_rectangle_action)

        draw_triangle_action = QAction("Triángulo", self)
        draw_triangle_action.triggered.connect(self.draw_events.draw_triangle_action_triggered)
        draw_menu.addAction(draw_triangle_action)

        draw_polygon_action = QAction("Polígono", self)
        draw_menu.addAction(draw_polygon_action)
        draw_polygon_action.triggered.connect(self.draw_events.draw_polygon_action_triggered)
