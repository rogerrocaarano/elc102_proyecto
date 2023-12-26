from PySide6.QtWidgets import QStatusBar, QLabel


class StatusBar(QStatusBar):
    def __init__(self):
        super().__init__()
        self.widgets = {
            "pos_x": QLabel("X"),
            "pos_y": QLabel("Y")
        }
        for widget in self.widgets.values():
            self.addWidget(widget)

    def update_pos(self, pos_x: int, pos_y: int):
        label_x: QLabel = self.widgets["pos_x"]
        label_y: QLabel = self.widgets["pos_y"]

        label_x.setText("X: " + str(pos_x))
        label_x.update()
        label_y.setText("Y: " + str(pos_y))
        label_y.update()
