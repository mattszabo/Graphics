from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Box:

    def __init__(self, *args):
        if len(args) == 1:
            self.width = args[0]
            self.height = args[0]
            self.depth = args[0]
        elif len(args) == 3:
            self.width = args[0]
            self.height = args[1]
            self.depth = args[2]
        else:
            self.width = 1
            self.height = 1
            self.depth = 1

    def draw(self):
        # Draw Cube (multiple quads)
        glBegin(GL_QUADS)
 
        glColor3f(0.0,1.0,0.0)
        glVertex3f( self.width, self.height,-self.depth)
        glVertex3f(-self.width, self.height,-self.depth)
        glVertex3f(-self.width, self.height, self.depth)
        glVertex3f( self.width, self.height, self.depth) 
 
        glColor3f(1.0,0.0,0.0)
        glVertex3f( self.width,-self.height, self.depth)
        glVertex3f(-self.width,-self.height, self.depth)
        glVertex3f(-self.width,-self.height,-self.depth)
        glVertex3f( self.width,-self.height,-self.depth) 
 
        glColor3f(0.0,1.0,0.0)
        glVertex3f( self.width, self.height, self.depth)
        glVertex3f(-self.width, self.height, self.depth)
        glVertex3f(-self.width,-self.height, self.depth)
        glVertex3f( self.width,-self.height, self.depth)
 
        glColor3f(1.0,1.0,0.0)
        glVertex3f( self.width,-self.height,-self.depth)
        glVertex3f(-self.width,-self.height,-self.depth)
        glVertex3f(-self.width, self.height,-self.depth)
        glVertex3f( self.width, self.height,-self.depth)
 
        glColor3f(0.0,0.0,1.0)
        glVertex3f(-self.width, self.height, self.depth) 
        glVertex3f(-self.width, self.height,-self.depth)
        glVertex3f(-self.width,-self.height,-self.depth) 
        glVertex3f(-self.width,-self.height, self.depth) 
 
        glColor3f(1.0,0.0,1.0)
        glVertex3f( self.width, self.height,-self.depth) 
        glVertex3f( self.width, self.height, self.depth)
        glVertex3f( self.width,-self.height, self.depth)
        glVertex3f( self.width,-self.height,-self.depth)

        glEnd()
 
