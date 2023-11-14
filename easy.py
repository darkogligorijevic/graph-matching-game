import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QOpenGLWidget, QSizePolicy
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective

class AxisWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super(AxisWidget, self).__init__(parent)
        self.x_angle = 0
        self.y_angle = 0
        self.z_angle = 0
        self.initializeGL()

    def resizeGL(self, w, h):
        glViewport(0, 0, w, h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, w / h, 1, 100)
        glMatrixMode(GL_MODELVIEW)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(0.0, 0.0, -6.0)
        glRotatef(self.x_angle, 1, 0, 0)
        glRotatef(self.y_angle, 0, 1, 0)
        glRotatef(self.z_angle, 0, 0, 1)

        # X-axis (Red)
        glBegin(GL_LINES)
        glColor3f(1, 0, 0)
        glVertex3f(0, 0, 0)
        glVertex3f(1, 0, 0)
        glEnd()  

        # Y-axis (Green)
        glBegin(GL_LINES)
        glColor3f(0, 1, 0)
        glVertex3f(0, 0, 0)
        glVertex3f(0, 1, 0) 
        glEnd()

        # Z-axis (blue)
        glBegin(GL_LINES)
        glColor3f(0, 0, 1)
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, 1) 
        glEnd()

    def generate_random_angles(self):
        self.x_angle = random.choice([-360, -180, -90, 0, 90, 180, 360])
        self.y_angle = random.choice([-360, -180, -90, 0, 90, 180, 360])
        self.z_angle = random.choice([-360, -180, -90, 0, 90, 180, 360])
        self.update()

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.axis_widget1 = AxisWidget(self)
        self.axis_widget1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.axis_widget2 = AxisWidget(self)
        self.axis_widget2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.generate_button = QPushButton("Generate Random Graph")
        self.generate_button.clicked.connect(self.generate_random_graph)

        self.x2_label = QLabel("X (Crvena):")
        self.y2_label = QLabel("Y (Zelena):")
        self.z2_label = QLabel("Z (Plava):")

        self.x2_input = QLineEdit()
        self.y2_input = QLineEdit()
        self.z2_input = QLineEdit()

        self.x2_input.textChanged.connect(self.updateX2Angle)
        self.y2_input.textChanged.connect(self.updateY2Angle)
        self.z2_input.textChanged.connect(self.updateZ2Angle)

        layout = QVBoxLayout()

        layout1 = QVBoxLayout()
        layout1.addWidget(self.axis_widget1, stretch=1)
        layout1.addWidget(self.axis_widget2, stretch=1)

        layout2 = QVBoxLayout()
        layout2.addWidget(self.x2_label)
        layout2.addWidget(self.x2_input)
        layout2.addWidget(self.y2_label)
        layout2.addWidget(self.y2_input)
        layout2.addWidget(self.z2_label)
        layout2.addWidget(self.z2_input)
        layout2.addWidget(self.generate_button)

        layout.addLayout(layout1)
        layout.addLayout(layout2)

        self.setLayout(layout)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Uvod u robotiku")

    def generate_random_graph(self):
        self.axis_widget1.update()
        self.axis_widget1.generate_random_angles()

    def updateX2Angle(self, value):
        try:
            self.axis_widget2.x_angle = float(value)
        except ValueError:
            pass
        self.axis_widget2.update()

    def updateY2Angle(self, value):
        try:
            self.axis_widget2.y_angle = float(value)
        except ValueError:
            pass
        self.axis_widget2.update()

    def updateZ2Angle(self, value):
        try:
            self.axis_widget2.z_angle = float(value)
        except ValueError:
            pass
        self.axis_widget2.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
