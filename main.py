import math

import pygame
import self as self
from OpenGL.GLUT import *
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glClearColor(0.3, 0.3, 0.3, 1.0)
    glTranslatef(0, 0, -2)
    glRotatef(-90, 1, 0, 0)
    glEnable(GL_DEPTH_TEST)


    while True:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Очищаем экран и заливаем серым цветом

        # нога правая перед
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((15-20)/40, (15-20)/40, -0.5)
        glVertex3f((18-20)/40, (15-20)/40, -0.5)
        glVertex3f((18-20)/40, (15-20)/40, (3-20)/40)
        glVertex3f((15-20)/40, (15-20)/40, (3-20)/40)
        glEnd()

        # нога правая зад
        glBegin(GL_POLYGON)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f((15 - 20) / 40, (20 - 20) / 40, -0.5)
        glVertex3f((18 - 20) / 40, (20 - 20) / 40, -0.5)
        glVertex3f((18 - 20) / 40, (20 - 20) / 40, (3 - 20) / 40)
        glVertex3f((15 - 20) / 40, (20 - 20) / 40, (3 - 20) / 40)
        glEnd()

        # нога правая верх
        glBegin(GL_POLYGON)
        glVertex3f((15 - 20) / 40, (20 - 20) / 40, (3 - 20) / 40)
        glVertex3f((18 - 20) / 40, (20 - 20) / 40, (3 - 20) / 40)
        glVertex3f((18 - 20) / 40, (16 - 20) / 40, (3 - 20) / 40)
        glVertex3f((15 - 20) / 40, (16 - 20) / 40, (3 - 20) / 40)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((15 - 20) / 40, (16 - 20) / 40, (3 - 20) / 40)
        glVertex3f((18 - 20) / 40, (16 - 20) / 40, (3 - 20) / 40)
        glVertex3f((18 - 20) / 40, (15 - 20) / 40, (3 - 20) / 40)
        glVertex3f((15 - 20) / 40, (15 - 20) / 40, (3 - 20) / 40)
        glColor3f(0.0, 0.0, 0.0)
        glEnd()


        # нога правая низ
        glBegin(GL_POLYGON)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f((15 - 20) / 40, (20 - 20) / 40, -0.5)
        glVertex3f((18 - 20) / 40, (20 - 20) / 40, -0.5)
        glVertex3f((18 - 20) / 40, (16 - 20) / 40, -0.5)
        glVertex3f((15 - 20) / 40, (16 - 20) / 40, -0.5)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((15 - 20) / 40, (16 - 20) / 40, -0.5)
        glVertex3f((18 - 20) / 40, (16 - 20) / 40, -0.5)
        glVertex3f((18 - 20) / 40, (15 - 20) / 40, -0.5)
        glVertex3f((15 - 20) / 40, (15 - 20) / 40, -0.5)
        glColor3f(0.0, 0.0, 0.0)
        glEnd()

        # нога правая правая
        glBegin(GL_POLYGON)
        glVertex3f((18 - 20) / 40, (16 - 20) / 40, (3 - 20) / 40)
        glVertex3f((18 - 20) / 40, (20 - 20) / 40, (3 - 20) / 40)
        glVertex3f((18 - 20) / 40, (20 - 20) / 40, -0.5)
        glVertex3f((18 - 20) / 40, (16 - 20) / 40, -0.5)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((18 - 20) / 40, (15 - 20) / 40, (3 - 20) / 40)
        glVertex3f((18 - 20) / 40, (16 - 20) / 40, (3 - 20) / 40)
        glVertex3f((18 - 20) / 40, (16 - 20) / 40, -0.5)
        glVertex3f((18 - 20) / 40, (15 - 20) / 40, -0.5)
        glColor3f(0.0, 0.0, 0.0)
        glEnd()

        # нога правая левая
        glBegin(GL_POLYGON)
        glVertex3f((15 - 20) / 40, (16 - 20) / 40, (3 - 20) / 40)
        glVertex3f((15 - 20) / 40, (20 - 20) / 40, (3 - 20) / 40)
        glVertex3f((15 - 20) / 40, (20 - 20) / 40, -0.5)
        glVertex3f((15 - 20) / 40, (16 - 20) / 40, -0.5)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((15 - 20) / 40, (15 - 20) / 40, (3 - 20) / 40)
        glVertex3f((15 - 20) / 40, (16 - 20) / 40, (3 - 20) / 40)
        glVertex3f((15 - 20) / 40, (16 - 20) / 40, -0.5)
        glVertex3f((15 - 20) / 40, (15 - 20) / 40, -0.5)
        glColor3f(0.0, 0.0, 0.0)
        glEnd()

        
        # нога левая перед
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((15+7 - 20) / 40, (15 - 20) / 40, -0.5)
        glVertex3f((18+7 - 20) / 40, (15 - 20) / 40, -0.5)
        glVertex3f((18+7 - 20) / 40, (15 - 20) / 40, (3 - 20) / 40)
        glVertex3f((15+7 - 20) / 40, (15 - 20) / 40, (3 - 20) / 40)
        glEnd()


        # нога левая зад
        glBegin(GL_POLYGON)
        glColor3f(0.0, 0.0, 0.0)
        glVertex3f((15+7 - 20) / 40, (20 - 20) / 40, -0.5)
        glVertex3f((18+7 - 20) / 40, (20 - 20) / 40, -0.5)
        glVertex3f((18+7 - 20) / 40, (20 - 20) / 40, (3 - 20) / 40)
        glVertex3f((15+7 - 20) / 40, (20 - 20) / 40, (3 - 20) / 40)
        glEnd()

        # нога левая верх
        glBegin(GL_POLYGON)
        glVertex3f((15+7 - 20) / 40, (20 - 20) / 40, (3 - 20) / 40)
        glVertex3f((18+7 - 20) / 40, (20 - 20) / 40, (3 - 20) / 40)
        glVertex3f((18+7 - 20) / 40, (16 - 20) / 40, (3 - 20) / 40)
        glVertex3f((15+7 - 20) / 40, (16 - 20) / 40, (3 - 20) / 40)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((15 + 7 - 20) / 40, (16 - 20) / 40, (3 - 20) / 40)
        glVertex3f((18 + 7 - 20) / 40, (16 - 20) / 40, (3 - 20) / 40)
        glVertex3f((18 + 7 - 20) / 40, (15 - 20) / 40, (3 - 20) / 40)
        glVertex3f((15 + 7 - 20) / 40, (15 - 20) / 40, (3 - 20) / 40)
        glColor3f(0.0, 0.0, 0.0)
        glEnd()

        # нога левая низ
        glBegin(GL_POLYGON)
        glVertex3f((15+7 - 20) / 40, (20 - 20) / 40, -0.5)
        glVertex3f((18+7 - 20) / 40, (20 - 20) / 40, -0.5)
        glVertex3f((18+7 - 20) / 40, (16 - 20) / 40, -0.5)
        glVertex3f((15+7 - 20) / 40, (16 - 20) / 40, -0.5)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((15 + 7 - 20) / 40, (16 - 20) / 40, -0.5)
        glVertex3f((18 + 7 - 20) / 40, (16 - 20) / 40, -0.5)
        glVertex3f((18 + 7 - 20) / 40, (15 - 20) / 40, -0.5)
        glVertex3f((15 + 7 - 20) / 40, (15 - 20) / 40, -0.5)
        glColor3f(0.0, 0.0, 0.0)
        glEnd()

        # нога левая правая
        glBegin(GL_POLYGON)
        glVertex3f((18+7 - 20) / 40, (16 - 20) / 40, (3 - 20) / 40)
        glVertex3f((18+7 - 20) / 40, (20 - 20) / 40, (3 - 20) / 40)
        glVertex3f((18+7 - 20) / 40, (20 - 20) / 40, -0.5)
        glVertex3f((18+7 - 20) / 40, (16 - 20) / 40, -0.5)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((18+7 - 20) / 40, (15 - 20) / 40, (3 - 20) / 40)
        glVertex3f((18+7 - 20) / 40, (16 - 20) / 40, (3 - 20) / 40)
        glVertex3f((18+7 - 20) / 40, (16 - 20) / 40, -0.5)
        glVertex3f((18+7 - 20) / 40, (15 - 20) / 40, -0.5)
        glColor3f(0.0, 0.0, 0.0)
        glEnd()

        # нога левая левая
        glBegin(GL_POLYGON)
        glVertex3f((15+7 - 20) / 40, (16 - 20) / 40, (3 - 20) / 40)
        glVertex3f((15+7 - 20) / 40, (20 - 20) / 40, (3 - 20) / 40)
        glVertex3f((15+7 - 20) / 40, (20 - 20) / 40, -0.5)
        glVertex3f((15+7 - 20) / 40, (16 - 20) / 40, -0.5)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((15 + 7 - 20) / 40, (15 - 20) / 40, (3 - 20) / 40)
        glVertex3f((15 + 7 - 20) / 40, (16 - 20) / 40, (3 - 20) / 40)
        glVertex3f((15 + 7 - 20) / 40, (16 - 20) / 40, -0.5)
        glVertex3f((15 + 7 - 20) / 40, (15 - 20) / 40, -0.5)
        glColor3f(0.0, 0.0, 0.0)
        glEnd()

        # туловище перед
        glBegin(GL_POLYGON)
        glVertex3f((14 - 20) / 40, (20 - 20) / 40, -0.5)
        glVertex3f((14 - 20) / 40, (20 - 20) / 40, (10 - 20) / 40)
        glVertex3f((25 - 20) / 40, (20 - 20) / 40, (10 - 20) / 40)
        glVertex3f((25 - 20) / 40, (20 - 20) / 40, -0.5)
        glEnd()
        # Пузико
        glBegin(GL_POLYGON)
        glColor3f(1, 1, 1)
        glVertex3f((16 - 20) / 40, (19.9 - 20) / 40, -0.5)
        glVertex3f((16 - 20) / 40, (19.9 - 20) / 40, (10 - 20) / 40)
        glVertex3f((23 - 20) / 40, (19.9 - 20) / 40, (10 - 20) / 40)
        glVertex3f((23 - 20) / 40, (19.9 - 20) / 40, -0.5)
        glEnd()
        # туловище зад
        glBegin(GL_POLYGON)
        glColor3f(0, 0, 0)
        glVertex3f((14 - 20) / 40, (26 - 20) / 40, -0.5)
        glVertex3f((14 - 20) / 40, (26 - 20) / 40, (10 - 20) / 40)
        glVertex3f((25 - 20) / 40, (26 - 20) / 40, (10 - 20) / 40)
        glVertex3f((25 - 20) / 40, (26 - 20) / 40, -0.5)
        glEnd()

        # туловище верх
        glBegin(GL_POLYGON)
        glVertex3f((25 - 20) / 40, (26 - 20) / 40, (10 - 20) / 40)
        glVertex3f((25 - 20) / 40, (20 - 20) / 40, (10 - 20) / 40)
        glVertex3f((14 - 20) / 40, (20 - 20) / 40, (10 - 20) / 40)
        glVertex3f((14 - 20) / 40, (26 - 20) / 40, (10 - 20) / 40)
        glEnd()

        # туловище низ
        glBegin(GL_POLYGON)
        glVertex3f((25 - 20) / 40, (26 - 20) / 40, -0.5)
        glVertex3f((25 - 20) / 40, (20 - 20) / 40, -0.5)
        glVertex3f((14 - 20) / 40, (20 - 20) / 40, -0.5)
        glVertex3f((14 - 20) / 40, (26 - 20) / 40, -0.5)
        glEnd()

        # туловище правая
        glBegin(GL_POLYGON)
        glVertex3f((25 - 20) / 40, (20 - 20) / 40, (10 - 20) / 40)
        glVertex3f((25 - 20) / 40, (26 - 20) / 40, (10 - 20) / 40)
        glVertex3f((25 - 20) / 40, (26 - 20) / 40, -0.5)
        glVertex3f((25 - 20) / 40, (20 - 20) / 40, -0.5)
        glEnd()

        # туловище левая
        glBegin(GL_POLYGON)
        glVertex3f((14 - 20) / 40, (20 - 20) / 40, (10 - 20) / 40)
        glVertex3f((14 - 20) / 40, (26 - 20) / 40, (10 - 20) / 40)
        glVertex3f((14 - 20) / 40, (26 - 20) / 40, -0.5)
        glVertex3f((14 - 20) / 40, (20 - 20) / 40, -0.5)
        glEnd()


        # рука правая перед
        glBegin(GL_POLYGON)
        glVertex3f((25 - 20) / 40, (22 - 20) / 40, (10 - 20) / 40)
        glVertex3f((28 - 20) / 40, (22 - 20) / 40, (10 - 20) / 40)
        glVertex3f((28 - 20) / 40, (22 - 20) / 40, (3 - 20) / 40)
        glVertex3f((25 - 20) / 40, (22 - 20) / 40, (3 - 20) / 40)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((25 - 20) / 40, (22 - 20) / 40, (3 - 20) / 40)
        glVertex3f((28 - 20) / 40, (22 - 20) / 40, (3 - 20) / 40)
        glVertex3f((28 - 20) / 40, (22 - 20) / 40, (2 - 20) / 40)
        glVertex3f((25 - 20) / 40, (22 - 20) / 40, (2 - 20) / 40)
        glColor3f(0.0, 0.0, 0.0)
        glEnd()

        # рука правая зад
        glBegin(GL_POLYGON)
        glVertex3f((25 - 20) / 40, (24 - 20) / 40, (10 - 20) / 40)
        glVertex3f((28 - 20) / 40, (24 - 20) / 40, (10 - 20) / 40)
        glVertex3f((28 - 20) / 40, (24 - 20) / 40, (3 - 20) / 40)
        glVertex3f((25 - 20) / 40, (24 - 20) / 40, (3 - 20) / 40)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((25 - 20) / 40, (24 - 20) / 40, (3 - 20) / 40)
        glVertex3f((28 - 20) / 40, (24 - 20) / 40, (3 - 20) / 40)
        glVertex3f((28 - 20) / 40, (24 - 20) / 40, (2 - 20) / 40)
        glVertex3f((25 - 20) / 40, (24 - 20) / 40, (2 - 20) / 40)
        glColor3f(0.0, 0.0, 0.0)
        glEnd()

        # рука правая верх
        glBegin(GL_POLYGON)
        glVertex3f((28 - 20) / 40, (22 - 20) / 40, (10 - 20) / 40)
        glVertex3f((25 - 20) / 40, (22 - 20) / 40, (10 - 20) / 40)
        glVertex3f((25 - 20) / 40, (24 - 20) / 40, (10 - 20) / 40)
        glVertex3f((28 - 20) / 40, (24 - 20) / 40, (10 - 20) / 40)
        glEnd()


        # рука правая низ
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((28 - 20) / 40, (22 - 20) / 40, (2 - 20) / 40)
        glVertex3f((25 - 20) / 40, (22 - 20) / 40, (2 - 20) / 40)
        glVertex3f((25 - 20) / 40, (24 - 20) / 40, (2 - 20) / 40)
        glVertex3f((28 - 20) / 40, (24 - 20) / 40, (2 - 20) / 40)
        glColor3f(0.0, 0.0, 0.0)
        glEnd()

        # рука правая правая
        glBegin(GL_POLYGON)
        glVertex3f((28 - 20) / 40, (22 - 20) / 40, (10 - 20) / 40)
        glVertex3f((28 - 20) / 40, (24 - 20) / 40, (10 - 20) / 40)
        glVertex3f((28 - 20) / 40, (24 - 20) / 40, (3 - 20) / 40)
        glVertex3f((28 - 20) / 40, (22 - 20) / 40, (3 - 20) / 40)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((28 - 20) / 40, (22 - 20) / 40, (3 - 20) / 40)
        glVertex3f((28 - 20) / 40, (24 - 20) / 40, (3 - 20) / 40)
        glVertex3f((28 - 20) / 40, (24 - 20) / 40, (2 - 20) / 40)
        glVertex3f((28 - 20) / 40, (22 - 20) / 40, (2 - 20) / 40)
        glColor3f(0.0, 0.0, 0.0)
        glEnd()

        # рука правая левая
        glBegin(GL_POLYGON)
        glVertex3f((25 - 20) / 40, (22 - 20) / 40, (10 - 20) / 40)
        glVertex3f((25 - 20) / 40, (24 - 20) / 40, (10 - 20) / 40)
        glVertex3f((25 - 20) / 40, (24 - 20) / 40, (3 - 20) / 40)
        glVertex3f((25 - 20) / 40, (22 - 20) / 40, (3 - 20) / 40)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((25 - 20) / 40, (22 - 20) / 40, (3 - 20) / 40)
        glVertex3f((25 - 20) / 40, (24 - 20) / 40, (3 - 20) / 40)
        glVertex3f((25 - 20) / 40, (24 - 20) / 40, (2 - 20) / 40)
        glVertex3f((25 - 20) / 40, (22 - 20) / 40, (2 - 20) / 40)
        glColor3f(0.0, 0.0, 0.0)
        glEnd()

        # рука левая перед
        glBegin(GL_POLYGON)
        glVertex3f((25-14 - 20) / 40, (22 - 20) / 40, (10 - 20) / 40)
        glVertex3f((28-14 - 20) / 40, (22 - 20) / 40, (10 - 20) / 40)
        glVertex3f((28-14 - 20) / 40, (22 - 20) / 40, (3 - 20) / 40)
        glVertex3f((25-14 - 20) / 40, (22 - 20) / 40, (3 - 20) / 40)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((25 - 14 - 20) / 40, (22 - 20) / 40, (3 - 20) / 40)
        glVertex3f((28 - 14 - 20) / 40, (22 - 20) / 40, (3 - 20) / 40)
        glVertex3f((28 - 14 - 20) / 40, (22 - 20) / 40, (2 - 20) / 40)
        glVertex3f((25 - 14 - 20) / 40, (22 - 20) / 40, (2 - 20) / 40)
        glColor3f(0.0, 0.0, 0.0)
        glEnd()

        # рука левая зад
        glBegin(GL_POLYGON)
        glVertex3f((25-14 - 20) / 40, (24 - 20) / 40, (10 - 20) / 40)
        glVertex3f((28-14 - 20) / 40, (24 - 20) / 40, (10 - 20) / 40)
        glVertex3f((28-14 - 20) / 40, (24 - 20) / 40, (3 - 20) / 40)
        glVertex3f((25-14 - 20) / 40, (24 - 20) / 40, (3 - 20) / 40)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((25 - 14 - 20) / 40, (24 - 20) / 40, (3 - 20) / 40)
        glVertex3f((28 - 14 - 20) / 40, (24 - 20) / 40, (3 - 20) / 40)
        glVertex3f((28 - 14 - 20) / 40, (24 - 20) / 40, (2 - 20) / 40)
        glVertex3f((25 - 14 - 20) / 40, (24 - 20) / 40, (2 - 20) / 40)
        glColor3f(0.0, 0.0, 0.0)
        glEnd()

        # рука левая верх
        glBegin(GL_POLYGON)
        glVertex3f((28-14 - 20) / 40, (22 - 20) / 40, (10 - 20) / 40)
        glVertex3f((25-14 - 20) / 40, (22 - 20) / 40, (10 - 20) / 40)
        glVertex3f((25-14 - 20) / 40, (24 - 20) / 40, (10 - 20) / 40)
        glVertex3f((28-14 - 20) / 40, (24 - 20) / 40, (10 - 20) / 40)
        glEnd()

        # рука левая низ
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((28-14 - 20) / 40, (22 - 20) / 40, (2 - 20) / 40)
        glVertex3f((25-14 - 20) / 40, (22 - 20) / 40, (2 - 20) / 40)
        glVertex3f((25-14 - 20) / 40, (24 - 20) / 40, (2 - 20) / 40)
        glVertex3f((28-14 - 20) / 40, (24 - 20) / 40, (2 - 20) / 40)
        glColor3f(0.0, 0.0, 0.0)
        glEnd()

        # рука левая правая
        glBegin(GL_POLYGON)
        glVertex3f((28-14 - 20) / 40, (22 - 20) / 40, (10 - 20) / 40)
        glVertex3f((28-14 - 20) / 40, (24 - 20) / 40, (10 - 20) / 40)
        glVertex3f((28-14 - 20) / 40, (24 - 20) / 40, (2 - 20) / 40)
        glVertex3f((28-14 - 20) / 40, (22 - 20) / 40, (2 - 20) / 40)
        glEnd()

        # рука левая левая
        glBegin(GL_POLYGON)
        glVertex3f((25-14 - 20) / 40, (22 - 20) / 40, (10 - 20) / 40)
        glVertex3f((25-14 - 20) / 40, (24 - 20) / 40, (10 - 20) / 40)
        glVertex3f((25-14 - 20) / 40, (24 - 20) / 40, (3 - 20) / 40)
        glVertex3f((25-14 - 20) / 40, (22 - 20) / 40, (3 - 20) / 40)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((25 - 14 - 20) / 40, (22 - 20) / 40, (3 - 20) / 40)
        glVertex3f((25 - 14 - 20) / 40, (24 - 20) / 40, (3 - 20) / 40)
        glVertex3f((25 - 14 - 20) / 40, (24 - 20) / 40, (2 - 20) / 40)
        glVertex3f((25 - 14 - 20) / 40, (22 - 20) / 40, (2 - 20) / 40)
        glColor3f(0.0, 0.0, 0.0)
        glEnd()

        # заготовка для головы перед
        glBegin(GL_POLYGON)
        glVertex3f((12 - 20) / 40, (16 - 20) / 40, (10 - 20) / 40)
        glVertex3f((12 - 20) / 40, (16 - 20) / 40, (25 - 20) / 40)
        glVertex3f((27 - 20) / 40, (16 - 20) / 40, (25 - 20) / 40)
        glVertex3f((27 - 20) / 40, (16 - 20) / 40, (10 - 20) / 40)
        glEnd()

        # заготовка для головы зад
        glBegin(GL_POLYGON)
        glVertex3f((12 - 20) / 40, (31 - 20) / 40, (10 - 20) / 40)
        glVertex3f((12 - 20) / 40, (31 - 20) / 40, (25 - 20) / 40)
        glVertex3f((27 - 20) / 40, (31 - 20) / 40, (25 - 20) / 40)
        glVertex3f((27 - 20) / 40, (31 - 20) / 40, (10 - 20) / 40)
        glEnd()

        # заготовка для головы верх
        glBegin(GL_POLYGON)
        glVertex3f((12 - 20) / 40, (16 - 20) / 40, (25 - 20) / 40)
        glVertex3f((12 - 20) / 40, (31 - 20) / 40, (25 - 20) / 40)
        glVertex3f((27 - 20) / 40, (31 - 20) / 40, (25 - 20) / 40)
        glVertex3f((27 - 20) / 40, (16 - 20) / 40, (25 - 20) / 40)
        glEnd()

        # заготовка для головы низ
        glBegin(GL_POLYGON)
        glVertex3f((12 - 20) / 40, (16 - 20) / 40, (10 - 20) / 40)
        glVertex3f((12 - 20) / 40, (31 - 20) / 40, (10 - 20) / 40)
        glVertex3f((27 - 20) / 40, (31 - 20) / 40, (10 - 20) / 40)
        glVertex3f((27 - 20) / 40, (16 - 20) / 40, (10 - 20) / 40)
        glEnd()

        # заготовка для головы правая
        glBegin(GL_POLYGON)
        glVertex3f((27 - 20) / 40, (16 - 20) / 40, (10 - 20) / 40)
        glVertex3f((27 - 20) / 40, (16 - 20) / 40, (25 - 20) / 40)
        glVertex3f((27 - 20) / 40, (31 - 20) / 40, (25 - 20) / 40)
        glVertex3f((27 - 20) / 40, (31 - 20) / 40, (10 - 20) / 40)
        glEnd()

        # заготовка для головы левая
        glBegin(GL_POLYGON)
        glVertex3f((12 - 20) / 40, (22 - 20) / 40, (10 - 20) / 40)
        glVertex3f((12 - 20) / 40, (24 - 20) / 40, (10 - 20) / 40)
        glVertex3f((12 - 20) / 40, (24 - 20) / 40, (2 - 20) / 40)
        glVertex3f((12 - 20) / 40, (22 - 20) / 40, (2 - 20) / 40)
        glEnd()

        # ушко правое перед
        glBegin(GL_POLYGON)
        glVertex3f((23 - 20) / 40, (23 - 20) / 40, (25 - 20) / 40)
        glVertex3f((28 - 20) / 40, (23 - 20) / 40, (30 - 20) / 40)
        glVertex3f((28 - 20) / 40, (23 - 20) / 40, (25 - 20) / 40)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(240 / 255, 142 / 255, 103 / 255)
        glVertex3f((25 - 20) / 40, (22.99 - 20) / 40, (26 - 20) / 40)
        glVertex3f((27 - 20) / 40, (22.99 - 20) / 40, (28 - 20) / 40)
        glVertex3f((27 - 20) / 40, (22.99 - 20) / 40, (26 - 20) / 40)
        glColor3f(0, 0, 0)
        glEnd()
        # ушко правое левый верх
        glBegin(GL_POLYGON)
        glVertex3f((23 - 20) / 40, (27 - 20) / 40, (25 - 20) / 40)
        glVertex3f((28 - 20) / 40, (23 - 20) / 40, (30 - 20) / 40)
        glVertex3f((23 - 20) / 40, (23 - 20) / 40, (25 - 20) / 40)
        glEnd()
        # ушко правое верх
        glBegin(GL_POLYGON)
        glVertex3f((28 - 20) / 40, (23 - 20) / 40, (30 - 20) / 40)
        glVertex3f((23 - 20) / 40, (27 - 20) / 40, (25 - 20) / 40)
        glVertex3f((27 - 20) / 40, (27 - 20) / 40, (25 - 20) / 40)
        glEnd()
        # ушко правое правое
        glBegin(GL_POLYGON)
        glVertex3f((28 - 20) / 40, (23 - 20) / 40, (30 - 20) / 40)
        glVertex3f((28 - 20) / 40, (23 - 20) / 40, (25 - 20) / 40)
        glVertex3f((27 - 20) / 40, (27 - 20) / 40, (25 - 20) / 40)
        glEnd()
        # ушко левое перед
        glPolygonMode(GL_BACK, GL_FILL)
        glBegin(GL_POLYGON)
        glVertex3f((16 - 20) / 40, (23 - 20) / 40, (25 - 20) / 40)
        glVertex3f((11 - 20) / 40, (23 - 20) / 40, (30 - 20) / 40)
        glVertex3f((11 - 20) / 40, (23 - 20) / 40, (25 - 20) / 40)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(240 / 255, 142 / 255, 103 / 255)
        glVertex3f((14 - 20) / 40, (22.99 - 20) / 40, (26 - 20) / 40)
        glVertex3f((12 - 20) / 40, (22.99 - 20) / 40, (28 - 20) / 40)
        glVertex3f((12 - 20) / 40, (22.9 - 20) / 40, (26 - 20) / 40)
        glColor3f(0, 0, 0)
        glEnd()
        # ушко левое правый верх
        glBegin(GL_POLYGON)
        glVertex3f((16 - 20) / 40, (27 - 20) / 40, (25 - 20) / 40)
        glVertex3f((11 - 20) / 40, (23 - 20) / 40, (30 - 20) / 40)
        glVertex3f((16 - 20) / 40, (23 - 20) / 40, (25 - 20) / 40)
        glEnd()
        # ушко левое правый верх
        glBegin(GL_TRIANGLE_FAN)
        glVertex3f((11 - 20) / 40, (23 - 20) / 40, (30 - 20) / 40)
        glVertex3f((16 - 20) / 40, (27 - 20) / 40, (25 - 20) / 40)
        glVertex3f((12 - 20) / 40, (27 - 20) / 40, (25 - 20) / 40)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex3f((11 - 20) / 40, (23 - 20) / 40, (30 - 20) / 40)
        glVertex3f((11 - 20) / 40, (23 - 20) / 40, (25 - 20) / 40)
        glVertex3f((12 - 20) / 40, (27 - 20) / 40, (25 - 20) / 40)
        glEnd()
        # ----------------------------------------------------------------хвост
        # --первая палка
        glColor3f(0.0, 0.0, 0.0)
        # --первая палка низ
        glBegin(GL_POLYGON)
        glVertex3f((22 - 20) / 40, (26 - 20) / 40, (0 - 20) / 40)
        glVertex3f((19 - 20) / 40, (26 - 20) / 40, (0 - 20) / 40)
        glVertex3f((27 - 20) / 40, (35.5 - 20) / 40, (0 - 20) / 40)
        glVertex3f((27.5 - 20) / 40, (32.5 - 20) / 40, (0 - 20) / 40)
        glEnd()
        # --первая палка лево
        glBegin(GL_POLYGON)
        glVertex3f((19 - 20) / 40, (26 - 20) / 40, (0 - 20) / 40)
        glVertex3f((19 - 20) / 40, (26 - 20) / 40, (3 - 20) / 40)
        glVertex3f((27 - 20) / 40, (35.5 - 20) / 40, (3 - 20) / 40)
        glVertex3f((27 - 20) / 40, (35.5 - 20) / 40, (0 - 20) / 40)
        glEnd()
        # --первая палка право
        glBegin(GL_POLYGON)
        glVertex3f((22 - 20) / 40, (26 - 20) / 40, (0 - 20) / 40)
        glVertex3f((22 - 20) / 40, (26 - 20) / 40, (3 - 20) / 40)
        glVertex3f((27 - 20) / 40, (32.5 - 20) / 40, (3 - 20) / 40)
        glVertex3f((27 - 20) / 40, (32.5 - 20) / 40, (0 - 20) / 40)
        glEnd()
        # --первая палка верх
        glBegin(GL_POLYGON)
        glVertex3f((22 - 20) / 40, (26 - 20) / 40, (3 - 20) / 40)
        glVertex3f((19 - 20) / 40, (26 - 20) / 40, (3 - 20) / 40)
        glVertex3f((27 - 20) / 40, (35.5 - 20) / 40, (3 - 20) / 40)
        glVertex3f((27.5 - 20) / 40, (32.5 - 20) / 40, (3 - 20) / 40)
        glEnd()
        # --вторая палка низ
        glBegin(GL_POLYGON)
        glVertex3f((27 - 20) / 40, (35.5 - 20) / 40, (0 - 20) / 40)
        glVertex3f((27 - 20) / 40, (32.5 - 20) / 40, (0 - 20) / 40)
        glVertex3f((35 - 20) / 40, (31.5 - 20) / 40, (0 - 20) / 40)
        glVertex3f((35 - 20) / 40, (34.5 - 20) / 40, (0 - 20) / 40)
        glEnd()
        # --вторая палка верх
        glBegin(GL_POLYGON)
        glVertex3f((27 - 20) / 40, (35.5 - 20) / 40, (3 - 20) / 40)
        glVertex3f((27 - 20) / 40, (32.5 - 20) / 40, (3 - 20) / 40)
        glVertex3f((35 - 20) / 40, (31.5 - 20) / 40, (3 - 20) / 40)
        glVertex3f((35 - 20) / 40, (34.5 - 20) / 40, (3 - 20) / 40)
        glEnd()
        # --вторая палка зад
        glBegin(GL_POLYGON)
        glVertex3f((27 - 20) / 40, (35.5 - 20) / 40, (0 - 20) / 40)
        glVertex3f((27 - 20) / 40, (35.5 - 20) / 40, (3 - 20) / 40)
        glVertex3f((35 - 20) / 40, (34.5 - 20) / 40, (3 - 20) / 40)
        glVertex3f((35 - 20) / 40, (34.5 - 20) / 40, (0 - 20) / 40)
        glEnd()
        # --вторая палка перед
        glBegin(GL_POLYGON)
        glVertex3f((27 - 20) / 40, (32.5 - 20) / 40, (0 - 20) / 40)
        glVertex3f((27 - 20) / 40, (32.5 - 20) / 40, (3 - 20) / 40)
        glVertex3f((35 - 20) / 40, (31.5 - 20) / 40, (3 - 20) / 40)
        glVertex3f((35 - 20) / 40, (31.5 - 20) / 40, (0 - 20) / 40)
        glEnd()
        # --кончик хвоста низ
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((35 - 20) / 40, (31.5 - 20) / 40, (0 - 20) / 40)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((35 - 20) / 40, (34.5 - 20) / 40, (0 - 20) / 40)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((38 - 20) / 40, (34.5 - 20) / 40, (0 - 20) / 40)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((38 - 20) / 40, (31.5 - 20) / 40, (0 - 20) / 40)
        glEnd()
        # кончик хвоста верх
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((35 - 20) / 40, (31.5 - 20) / 40, (3 - 20) / 40)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((35 - 20) / 40, (34.5 - 20) / 40, (3 - 20) / 40)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((38 - 20) / 40, (34.5 - 20) / 40, (3 - 20) / 40)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((38 - 20) / 40, (31.5 - 20) / 40, (3 - 20) / 40)
        glEnd()
        # кончик хвоста зад
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((35 - 20) / 40, (34.5 - 20) / 40, (0 - 20) / 40)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((35 - 20) / 40, (34.5 - 20) / 40, (3 - 20) / 40)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((38 - 20) / 40, (34.5 - 20) / 40, (3 - 20) / 40)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((38 - 20) / 40, (34.5 - 20) / 40, (0 - 20) / 40)
        glEnd()
        # кончик хвоста перед
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((35 - 20) / 40, (31.5 - 20) / 40, (0 - 20) / 40)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((35 - 20) / 40, (31.5 - 20) / 40, (3 - 20) / 40)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((38 - 20) / 40, (31.5 - 20) / 40, (3 - 20) / 40)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((38 - 20) / 40, (31.5 - 20) / 40, (0 - 20) / 40)
        glEnd()
        # кончик хвоста право
        glBegin(GL_POLYGON)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((38 - 20) / 40, (31.5 - 20) / 40, (0 - 20) / 40)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((38 - 20) / 40, (31.5 - 20) / 40, (3 - 20) / 40)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((38 - 20) / 40, (34.5 - 20) / 40, (3 - 20) / 40)
        glColor3f(1.0, 1.0, 1.0)
        glVertex3f((38 - 20) / 40, (34.5 - 20) / 40, (0 - 20) / 40)
        glEnd()
        # Левый глаз
        glBegin(GL_POLYGON)
        glColor3f(239/255, 236/255, 1/255)
        glVertex3f((14 - 20) / 40, (15.9 - 20) / 40, (23 - 20) / 40)
        glVertex3f((14 - 20) / 40, (15.9 - 20) / 40, (22 - 20) / 40)
        glVertex3f((16 - 20) / 40, (15.9 - 20) / 40, (22 - 20) / 40)
        glVertex3f((16 - 20) / 40, (15.9 - 20) / 40, (23 - 20) / 40)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex3f((13 - 20) / 40, (15.9 - 20) / 40, (22 - 20) / 40)
        glVertex3f((17 - 20) / 40, (15.9 - 20) / 40, (22 - 20) / 40)
        glVertex3f((17 - 20) / 40, (15.9 - 20) / 40, (21.5 - 20) / 40)
        glVertex3f((13 - 20) / 40, (15.9 - 20) / 40, (21.5 - 20) / 40)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex3f((13 - 20) / 40, (15.9 - 20) / 40, (21.5 - 20) / 40)
        glVertex3f((14.5 - 20) / 40, (15.9 - 20) / 40, (21.5 - 20) / 40)
        glVertex3f((14.5 - 20) / 40, (15.9 - 20) / 40, (20.5 - 20) / 40)
        glVertex3f((13 - 20) / 40, (15.9 - 20) / 40, (20.5 - 20) / 40)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex3f((17 - 20) / 40, (15.9 - 20) / 40, (21.5 - 20) / 40)
        glVertex3f((15.5 - 20) / 40, (15.9 - 20) / 40, (21.5 - 20) / 40)
        glVertex3f((15.5 - 20) / 40, (15.9 - 20) / 40, (20.5 - 20) / 40)
        glVertex3f((17 - 20) / 40, (15.9 - 20) / 40, (20.5 - 20) / 40)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex3f((13 - 20) / 40, (15.9 - 20) / 40, (20.5 - 20) / 40)
        glVertex3f((17 - 20) / 40, (15.9 - 20) / 40, (20.5 - 20) / 40)
        glVertex3f((17 - 20) / 40, (15.9 - 20) / 40, (20 - 20) / 40)
        glVertex3f((13 - 20) / 40, (15.9 - 20) / 40, (20 - 20) / 40)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(239 / 255, 236 / 255, 1 / 255)
        glVertex3f((14 - 20) / 40, (15.9 - 20) / 40, (20 - 20) / 40)
        glVertex3f((14 - 20) / 40, (15.9 - 20) / 40, (19 - 20) / 40)
        glVertex3f((16 - 20) / 40, (15.9 - 20) / 40, (19 - 20) / 40)
        glVertex3f((16 - 20) / 40, (15.9 - 20) / 40, (20 - 20) / 40)
        glEnd()
        # Правый глаз
        glBegin(GL_POLYGON)
        glColor3f(239 / 255, 236 / 255, 1 / 255)
        glVertex3f((14 + 9 - 20) / 40, (15.9 - 20) / 40, (23 - 20) / 40)
        glVertex3f((14 + 9 - 20) / 40, (15.9 - 20) / 40, (22 - 20) / 40)
        glVertex3f((16 + 9 - 20) / 40, (15.9 - 20) / 40, (22 - 20) / 40)
        glVertex3f((16 + 9 - 20) / 40, (15.9 - 20) / 40, (23 - 20) / 40)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex3f((13 + 9 - 20) / 40, (15.9 - 20) / 40, (22 - 20) / 40)
        glVertex3f((17 + 9 - 20) / 40, (15.9 - 20) / 40, (22 - 20) / 40)
        glVertex3f((17 + 9 - 20) / 40, (15.9 - 20) / 40, (21.5 - 20) / 40)
        glVertex3f((13 + 9 - 20) / 40, (15.9 - 20) / 40, (21.5 - 20) / 40)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex3f((13 + 9 - 20) / 40, (15.9 - 20) / 40, (21.5 - 20) / 40)
        glVertex3f((14.5 + 9 - 20) / 40, (15.9 - 20) / 40, (21.5 - 20) / 40)
        glVertex3f((14.5 + 9 - 20) / 40, (15.9 - 20) / 40, (20.5 - 20) / 40)
        glVertex3f((13 + 9 - 20) / 40, (15.9 - 20) / 40, (20.5 - 20) / 40)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex3f((17 + 9 - 20) / 40, (15.9 - 20) / 40, (21.5 - 20) / 40)
        glVertex3f((15.5 + 9 - 20) / 40, (15.9 - 20) / 40, (21.5 - 20) / 40)
        glVertex3f((15.5 + 9 - 20) / 40, (15.9 - 20) / 40, (20.5 - 20) / 40)
        glVertex3f((17 + 9 - 20) / 40, (15.9 - 20) / 40, (20.5 - 20) / 40)
        glEnd()
        glBegin(GL_POLYGON)
        glVertex3f((13 + 9 - 20) / 40, (15.9 - 20) / 40, (20.5 - 20) / 40)
        glVertex3f((17 + 9 - 20) / 40, (15.9 - 20) / 40, (20.5 - 20) / 40)
        glVertex3f((17 + 9 - 20) / 40, (15.9 - 20) / 40, (20 - 20) / 40)
        glVertex3f((13 + 9 - 20) / 40, (15.9 - 20) / 40, (20 - 20) / 40)
        glEnd()
        glBegin(GL_POLYGON)
        glColor3f(239 / 255, 236 / 255, 1 / 255)
        glVertex3f((14 + 9 - 20) / 40, (15.9 - 20) / 40, (20 - 20) / 40)
        glVertex3f((14 + 9 - 20) / 40, (15.9 - 20) / 40, (19 - 20) / 40)
        glVertex3f((16 + 9 - 20) / 40, (15.9 - 20) / 40, (19 - 20) / 40)
        glVertex3f((16 + 9 - 20) / 40, (15.9 - 20) / 40, (20 - 20) / 40)
        glEnd()
        # Моська
        # моська 1 перед
        glBegin(GL_POLYGON)
        glColor3f(1, 1, 1)
        glVertex3f((18 - 20) / 40, (15 - 20) / 40, (18 - 20) / 40)
        glVertex3f((21 - 20) / 40, (15 - 20) / 40, (18 - 20) / 40)
        glVertex3f((21 - 20) / 40, (15 - 20) / 40, (17 - 20) / 40)
        glVertex3f((18 - 20) / 40, (15 - 20) / 40, (17 - 20) / 40)
        glEnd()
        # моська 3 перед
        glBegin(GL_POLYGON)
        glColor3f(1, 1, 1)
        glVertex3f((15 - 20) / 40, (15 - 20) / 40, (17 - 20) / 40)
        glVertex3f((18.5 - 20) / 40, (15 - 20) / 40, (17 - 20) / 40)
        glVertex3f((18.5 - 20) / 40, (15 - 20) / 40, (15 - 20) / 40)
        glVertex3f((15 - 20) / 40, (15 - 20) / 40, (15 - 20) / 40)
        glEnd()
        # моська 4 перед
        glBegin(GL_POLYGON)
        glVertex3f((15+5.5 - 20) / 40, (15 - 20) / 40, (17 - 20) / 40)
        glVertex3f((18.5+5.5 - 20) / 40, (15 - 20) / 40, (17 - 20) / 40)
        glVertex3f((18.5+5.5 - 20) / 40, (15 - 20) / 40, (15 - 20) / 40)
        glVertex3f((15+5.5 - 20) / 40, (15 - 20) / 40, (15 - 20) / 40)
        glEnd()
        # моська 2 перед
        glBegin(GL_POLYGON)
        glVertex3f((18.5 - 20) / 40, (15 - 20) / 40, (17 - 20) / 40)
        glVertex3f((20.5 - 20) / 40, (15 - 20) / 40, (17 - 20) / 40)
        glVertex3f((20.5 - 20) / 40, (15 - 20) / 40, (15.5 - 20) / 40)
        glVertex3f((18.5 - 20) / 40, (15 - 20) / 40, (15.5 - 20) / 40)
        glEnd()
        # моська 2 низ
        glBegin(GL_POLYGON)
        glVertex3f((18.5 - 20) / 40, (16 - 20) / 40, (15.5 - 20) / 40)
        glVertex3f((20.5 - 20) / 40, (16 - 20) / 40, (15.5 - 20) / 40)
        glVertex3f((20.5 - 20) / 40, (15 - 20) / 40, (15.5 - 20) / 40)
        glVertex3f((18.5 - 20) / 40, (15 - 20) / 40, (15.5 - 20) / 40)
        glEnd()
        # моська 1 верх
        glBegin(GL_POLYGON)
        glColor3f(1, 1, 1)
        glVertex3f((18 - 20) / 40, (15 - 20) / 40, (18 - 20) / 40)
        glVertex3f((21 - 20) / 40, (15 - 20) / 40, (18 - 20) / 40)
        glVertex3f((21 - 20) / 40, (16 - 20) / 40, (18 - 20) / 40)
        glVertex3f((18 - 20) / 40, (16 - 20) / 40, (18 - 20) / 40)
        glEnd()
        # моська 1 лево
        glBegin(GL_POLYGON)
        glColor3f(1, 1, 1)
        glVertex3f((18 - 20) / 40, (15 - 20) / 40, (18 - 20) / 40)
        glVertex3f((18 - 20) / 40, (15 - 20) / 40, (17 - 20) / 40)
        glVertex3f((18 - 20) / 40, (16 - 20) / 40, (17 - 20) / 40)
        glVertex3f((18 - 20) / 40, (16 - 20) / 40, (18 - 20) / 40)
        glEnd()
        # моська 1 право
        glBegin(GL_POLYGON)
        glColor3f(1, 1, 1)
        glVertex3f((21 - 20) / 40, (15 - 20) / 40, (18 - 20) / 40)
        glVertex3f((21 - 20) / 40, (15 - 20) / 40, (17 - 20) / 40)
        glVertex3f((21 - 20) / 40, (16 - 20) / 40, (17 - 20) / 40)
        glVertex3f((21 - 20) / 40, (16 - 20) / 40, (18 - 20) / 40)
        glEnd()
        # моська 3 лево
        glBegin(GL_POLYGON)
        glColor3f(1, 1, 1)
        glVertex3f((15 - 20) / 40, (15 - 20) / 40, (17 - 20) / 40)
        glVertex3f((15 - 20) / 40, (15 - 20) / 40, (15 - 20) / 40)
        glVertex3f((15 - 20) / 40, (16 - 20) / 40, (15 - 20) / 40)
        glVertex3f((15 - 20) / 40, (16 - 20) / 40, (17 - 20) / 40)
        glEnd()
        # моська 4 право
        glBegin(GL_POLYGON)
        glColor3f(1, 1, 1)
        glVertex3f((24 - 20) / 40, (15 - 20) / 40, (17 - 20) / 40)
        glVertex3f((24 - 20) / 40, (15 - 20) / 40, (15 - 20) / 40)
        glVertex3f((24 - 20) / 40, (16 - 20) / 40, (15 - 20) / 40)
        glVertex3f((24 - 20) / 40, (16 - 20) / 40, (17 - 20) / 40)
        glEnd()
        # моська 3 верх
        glBegin(GL_POLYGON)
        glColor3f(1, 1, 1)
        glVertex3f((15 - 20) / 40, (15 - 20) / 40, (17 - 20) / 40)
        glVertex3f((19 - 20) / 40, (15 - 20) / 40, (17 - 20) / 40)
        glVertex3f((19 - 20) / 40, (16 - 20) / 40, (17 - 20) / 40)
        glVertex3f((15 - 20) / 40, (16 - 20) / 40, (17 - 20) / 40)
        glEnd()
        # моська 4 верх
        glBegin(GL_POLYGON)
        glColor3f(1, 1, 1)
        glVertex3f((15+5 - 20) / 40, (15 - 20) / 40, (17 - 20) / 40)
        glVertex3f((19+5 - 20) / 40, (15 - 20) / 40, (17 - 20) / 40)
        glVertex3f((19+5 - 20) / 40, (16 - 20) / 40, (17 - 20) / 40)
        glVertex3f((15+5 - 20) / 40, (16 - 20) / 40, (17 - 20) / 40)
        glEnd()
        # моська 3 низ
        glBegin(GL_POLYGON)
        glColor3f(1, 1, 1)
        glVertex3f((15 - 20) / 40, (15 - 20) / 40, (15 - 20) / 40)
        glVertex3f((19 - 20) / 40, (15 - 20) / 40, (15 - 20) / 40)
        glVertex3f((19 - 20) / 40, (16 - 20) / 40, (15 - 20) / 40)
        glVertex3f((15 - 20) / 40, (16 - 20) / 40, (15 - 20) / 40)
        glEnd()
        # моська 4 низ
        glBegin(GL_POLYGON)
        glColor3f(1, 1, 1)
        glVertex3f((15 + 5 - 20) / 40, (15 - 20) / 40, (15 - 20) / 40)
        glVertex3f((19 + 5 - 20) / 40, (15 - 20) / 40, (15 - 20) / 40)
        glVertex3f((19 + 5 - 20) / 40, (16 - 20) / 40, (15 - 20) / 40)
        glVertex3f((15 + 5 - 20) / 40, (16 - 20) / 40, (15 - 20) / 40)
        glEnd()
        # моська 3 право
        glBegin(GL_POLYGON)
        glVertex3f((18.5 - 20) / 40, (15 - 20) / 40, (15 - 20) / 40)
        glVertex3f((18.5 - 20) / 40, (15 - 20) / 40, (17 - 20) / 40)
        glVertex3f((18.5 - 20) / 40, (16 - 20) / 40, (17 - 20) / 40)
        glVertex3f((18.5 - 20) / 40, (16 - 20) / 40, (15 - 20) / 40)
        glEnd()
        # моська 4 лево
        glBegin(GL_POLYGON)
        glVertex3f((15+5.5 - 20) / 40, (15 - 20) / 40, (15 - 20) / 40)
        glVertex3f((15+5.5 - 20) / 40, (15 - 20) / 40, (17 - 20) / 40)
        glVertex3f((15+5.5 - 20) / 40, (16 - 20) / 40, (17 - 20) / 40)
        glVertex3f((15+5.5 - 20) / 40, (16 - 20) / 40, (15 - 20) / 40)
        glEnd()
        # моська носик
        glBegin(GL_POLYGON)
        glColor3f(240/255, 142/255, 103/255)
        glVertex3f((19 - 20) / 40, (14.9 - 20) / 40, (18 - 20) / 40)
        glVertex3f((19 - 20) / 40, (14.9 - 20) / 40, (17 - 20) / 40)
        glVertex3f((20 - 20) / 40, (14.9 - 20) / 40, (17 - 20) / 40)
        glVertex3f((20 - 20) / 40, (14.9 - 20) / 40, (18 - 20) / 40)
        glEnd()
        # Усик правый 1
        glBegin(GL_LINES)
        glColor3f(1, 1, 1)
        glVertex3f((17.5+5.5-20)/40, (15-20)/40, (17-20)/40)
        glVertex3f((22.5+5.5-20)/40, (14-20)/40, (18-20)/40)
        glEnd()
        # Усик правый 2
        glBegin(GL_LINES)
        glVertex3f((17.5 + 5.5 - 20) / 40, (15 - 20) / 40, (16 - 20) / 40)
        glVertex3f((23.5 + 5.5 - 20) / 40, (14 - 20) / 40, (16 - 20) / 40)
        glEnd()
        # Усик правый 3
        glBegin(GL_LINES)
        glVertex3f((17.5 + 5.5 - 20) / 40, (15 - 20) / 40, (15 - 20) / 40)
        glVertex3f((22.5 + 5.5 - 20) / 40, (14 - 20) / 40, (14 - 20) / 40)
        glEnd()
        # Усик левая 1
        glBegin(GL_LINES)
        glVertex3f((16 - 20) / 40, (15 - 20) / 40, (17 - 20) / 40)
        glVertex3f((11 - 20) / 40, (14 - 20) / 40, (18 - 20) / 40)
        glEnd()
        # Усик левая 2
        glBegin(GL_LINES)
        glVertex3f((16 - 20) / 40, (15 - 20) / 40, (16 - 20) / 40)
        glVertex3f((10 - 20) / 40, (14 - 20) / 40, (16 - 20) / 40)
        glEnd()
        # Усик левая 3
        glBegin(GL_LINES)
        glVertex3f((16 - 20) / 40, (15 - 20) / 40, (15 - 20) / 40)
        glVertex3f((11 - 20) / 40, (14 - 20) / 40, (14 - 20) / 40)
        glEnd()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glRotatef(30, 0, 0, 1)
                    glEnable(GL_DEPTH_TEST)
                if event.key == pygame.K_RIGHT:
                    glRotatef(-30, 0, 0, 1)
                    glEnable(GL_DEPTH_TEST)
                if event.key == pygame.K_UP:
                    glRotatef(30, 1, 0, 0)
                    glEnable(GL_DEPTH_TEST)
                if event.key == pygame.K_DOWN:
                    glRotatef(-30, 1, 0, 0)
                    glEnable(GL_DEPTH_TEST)

        pygame.display.flip()
        pygame.time.wait(1)



main()