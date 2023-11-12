import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QOpenGLWidget, QSizePolicy
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective
from OpenGL.GLUT import *

class AxisWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super(AxisWidget, self).__init__(parent)
        self.x_angle = 0
        self.y_angle = 0
        self.z_angle = 0

    def initializeGL(self):
        glEnable(GL_DEPTH_TEST)

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

        glBegin(GL_LINES)
        glColor3f(1, 0, 0)
        glVertex3f(0, 0, 0)
        glVertex3f(1, 0, 0)  # X-axis

        glColor3f(0, 1, 0)
        glVertex3f(0, 0, 0)
        glVertex3f(0, 1, 0)  # Y-axis

        glColor3f(0, 0, 1)
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, 1)  # Z-axis
        glEnd()
        

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.axis_widget = AxisWidget(self)
        self.axis_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.x_label = QLabel("X (Crvena):")
        self.y_label = QLabel("Y (Zelena):")
        self.z_label = QLabel("Z (Plava):")

        self.x_input = QLineEdit()
        self.y_input = QLineEdit()
        self.z_input = QLineEdit()

        self.x_input.textChanged.connect(self.updateXAngle)
        self.y_input.textChanged.connect(self.updateYAngle)
        self.z_input.textChanged.connect(self.updateZAngle)

        layout = QVBoxLayout()
        layout.addWidget(self.axis_widget, stretch=1)
        layout.addWidget(self.x_label)
        layout.addWidget(self.x_input)
        layout.addWidget(self.y_label)
        layout.addWidget(self.y_input)
        layout.addWidget(self.z_label)
        layout.addWidget(self.z_input)

        self.setLayout(layout)
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Uvod u robotiku")

    def updateXAngle(self, value):
        try:
            self.axis_widget.x_angle = float(value)
        except ValueError:
            pass
        self.axis_widget.update()

    def updateYAngle(self, value):
        try:
            self.axis_widget.y_angle = float(value)
        except ValueError:
            pass
        self.axis_widget.update()

    def updateZAngle(self, value):
        try:
            self.axis_widget.z_angle = float(value)
        except ValueError:
            pass
        self.axis_widget.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
