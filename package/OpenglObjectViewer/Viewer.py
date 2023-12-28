from math import inf
import numpy as np

from PySide6.QtOpenGLWidgets import QOpenGLWidget
from pywavefront import Wavefront
from OpenGL.GL import *
from OpenGL.GLU import *


class Viewer(QOpenGLWidget):
    def __init__(self, model_path, parent=None):
        super().__init__(parent)
        self.setFixedSize(800, 800)
        self.model: Wavefront = Wavefront(model_path, collect_faces=True)
        self.normals = self.calculate_normals()
        self.min_point, self.max_point = self.calculate_extreme_points()
        self.center_x, self.center_y, self.center_z = self.get_model_center()
        self.camera_position_multiplier_x = 1.2
        self.camera_position_multiplier_y = 2
        self.camera_position_multiplier_z = 3

    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        # Ilumination settings
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_POSITION, [1, 1, 1, 0])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 1, 1, 1])
        glLightfv(GL_LIGHT0, GL_SPECULAR, [1, 1, 1, 1])
        # Material settings
        glEnable(GL_COLOR_MATERIAL)
        glMaterialfv(GL_FRONT, GL_AMBIENT, [0.2, 0.2, 0.2, 1])
        glMaterialfv(GL_FRONT, GL_DIFFUSE, [0.8, 0.8, 0.8, 1])
        glMaterialfv(GL_FRONT, GL_SPECULAR, [1, 1, 1, 1])
        glMaterialfv(GL_FRONT, GL_SHININESS, 100)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        self.set_camera_position(
            self.camera_position_multiplier_x,
            self.camera_position_multiplier_y,
            self.camera_position_multiplier_z
        )
        self.draw_model()

    def draw_model(self):
        glBegin(GL_TRIANGLES)
        for face in self.model.mesh_list[0].faces:
            v1 = np.array(self.model.vertices[face[0]])
            v2 = np.array(self.model.vertices[face[1]])
            v3 = np.array(self.model.vertices[face[2]])
            normal = np.cross(v2 - v1, v3 - v1)
            normal /= np.linalg.norm(normal)
            for vertex_id in face:
                vertex = self.model.vertices[vertex_id]
                glNormal3fv(normal)
                glVertex3fv(vertex)
        glEnd()

    def get_model_center(self):
        x_values = [vertex[0] for vertex in self.model.vertices]
        y_values = [vertex[1] for vertex in self.model.vertices]
        z_values = [vertex[2] for vertex in self.model.vertices]

        center_x = sum(x_values) / len(x_values)
        center_y = sum(y_values) / len(y_values)
        center_z = sum(z_values) / len(z_values)

        return center_x, center_y, center_z

    def set_camera_position_multiplier(self, x, y, z):
        self.camera_position_multiplier_x = x
        self.camera_position_multiplier_y = y
        self.camera_position_multiplier_z = z

    def set_camera_position(self, x_multiplier, y_multiplier, z_multiplier):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluPerspective(45, 1, 0.001, 1000000)
        size_x = self.max_point[0] - self.min_point[0]
        size_y = self.max_point[1] - self.min_point[1]
        size_z = self.max_point[2] - self.min_point[2]
        gluLookAt(
            # Camera position
            self.center_x - size_x * x_multiplier,
            self.center_y + size_y * y_multiplier,
            self.center_z + size_z * z_multiplier,
            # Camera viewing point
            self.center_x,
            self.center_y,
            self.center_z,
            # Camera orientation
            0,
            1,
            0
        )

    def calculate_extreme_points(self):
        min_x, min_y, min_z = inf, inf, inf
        max_x, max_y, max_z = -inf, -inf, -inf

        for vertex in self.model.vertices:
            min_x = min(min_x, vertex[0])
            min_y = min(min_y, vertex[1])
            min_z = min(min_z, vertex[2])

            max_x = max(max_x, vertex[0])
            max_y = max(max_y, vertex[1])
            max_z = max(max_z, vertex[2])

        return (min_x, min_y, min_z), (max_x, max_y, max_z)

    def calculate_normals(self):
        face_normals = []
        for face in self.model.mesh_list[0].faces:
            v1 = np.array(self.model.vertices[face[0]])
            v2 = np.array(self.model.vertices[face[1]])
            v3 = np.array(self.model.vertices[face[2]])
            normal = np.cross(v2 - v1, v3 - v1)
            normal /= np.linalg.norm(normal)
            face_normals.append(normal)
        return face_normals
