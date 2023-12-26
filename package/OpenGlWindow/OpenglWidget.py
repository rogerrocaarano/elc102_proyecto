from PySide6.QtOpenGLWidgets import QOpenGLWidget
from OpenGL import GL


class OpenglWidget(QOpenGLWidget):
    def __init__(self):
        super().__init__()
        self.model = None

    def initializeGL(self):
        GL.glClearColor(0.5, 0.5, 0.5, 1)

    def paintGL(self):
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)
