from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *

import sys

name = 'ball_glut'

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(400,400)
    glutCreateWindow(name)

    glClearColor(0.,0.,0.,1.)
    glShadeModel(GL_SMOOTH)
    glutDisplayFunc(display)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(40.,1.,1.,40.)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0,0,10,
              0,0,0,
              0,1,0)
    glPushMatrix()
    glutMainLoop()
    return

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    color = [1.0,0.,0.,1.]
    glColor(color)
    glBegin(GL_POLYGON)
    glVertex3d(1,2,3)
    glVertex3d(0,0,2)
    glVertex3d(1, 0, 3)
    glEnd()
    glPopMatrix()
    glutSwapBuffers()
    return

if __name__ == '__main__': main()
