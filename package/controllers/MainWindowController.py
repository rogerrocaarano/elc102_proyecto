from package.views.components.StatusBar import StatusBar


class MainWindowController:
    def __init__(self, view):
        self.__view = view

    def update_canvas_pos(self, pos_x: int, pos_y: int):
        status_bar: StatusBar = self.__view.statusBar()
        status_bar.update_pos(pos_x, pos_y)
