from OpenGL.GL import *
from OpenGL.GLU import *
import pyglet.app as app
import pyglet.window as window
import pyglet.clock as clock
import pyglet.event as event
import pyglet.window.key as key

RED = [255, 0, 0, 1]
GREEN = [0, 255, 0, 1]
BLUE = [0, 0, 255, 1]
YELLOW = [255, 0, 0, 1]
PURPLE = [159, 0, 197, 1]
ORANGE = [255, 165, 0, 1]
BROWN = [150, 75, 0, 1]
BLACK = [0, 0, 0, 1]

win = window.Window(resizable=True, visible=False)
glClearColor(1, 1, 1, 1)
glEnable(GL_DEPTH_TEST)

def GLfloatArray(*args):
    return (GLfloat * len(args))(*[float(n) for n in args])

def GLuintArray(*args):
    return (GLuint * len(args))(*[int(n) for n in args])

class Cube():
    def __init__(self, length, x=0, y=0, z=0, rx=0, ry=0, rz=0):
        self.length = length
        self.x = x
        self.y = y
        self.z = z
        self.rx = rx
        self.ry = ry
        self.rz = rz
        self._init_gl_draw_list()
        
    def _init_gl_draw_list(self):
        vertices = GLfloatArray(
            self.x - self.length / 2.0, self.y - self.length / 2.0, self.length / 2.0,
            self.x + self.length / 2.0, self.y - self.length / 2.0, self.length / 2.0,
            self.x + self.length / 2.0, self.y + self.length / 2.0, self.length / 2.0,
            self.x - self.length / 2.0, self.y + self.length / 2.0, self.length / 2.0,
            self.x - self.length / 2.0, self.y - self.length / 2.0, self.length / -2.0,
            self.x + self.length / 2.0, self.y - self.length / 2.0, self.length / -2.0,
            self.x + self.length / 2.0, self.y + self.length / 2.0, self.length / -2.0,
            self.x - self.length / 2.0, self.y + self.length / 2.0, self.length / -2.0
        )
        colors = GLfloatArray(*RED + GREEN + BLUE + YELLOW + PURPLE + 
                              ORANGE + BROWN + BLACK)
        indices = GLuintArray(0,1,2,0,2,3,1,5,6,1,6,2,0,7,4,0,3,7,0,4,5,0,5,1,4,7,5,
                              4,6,7,3,2,6,3,6,7)
        self.gl_draw_list = glGenLists(1)
        glNewList(self.gl_draw_list, GL_COMPILE)

        glPushClientAttrib(GL_CLIENT_VERTEX_ARRAY_BIT)
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, vertices)
        glColorPointer(4, GL_FLOAT, 0, colors)
        glDrawElements(GL_TRIANGLES, len(indices), GL_UNSIGNED_INT, indices)
        glPopClientAttrib()

        glEndList()

def rotate(cube):
    # pass
    cube.rx = (cube.rx + 2) % 360
    cube.ry = (cube.ry + 1) % 360
    cube.rz = (cube.rz + 5) % 360

def draw(cube):
    glPushMatrix()
    glTranslatef(cube.x, cube.y, cube.z)
    glRotatef(cube.rx, 1, 0, 0)
    glRotatef(cube.ry, 0, 1, 0)
    glRotatef(cube.rz, 0, 0, 1)
    glCallList(cube.gl_draw_list)
    glPopMatrix()

cube = Cube(50)

@win.event
def on_resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, float(width)/float(height), 0.1, 1000)
    glMatrixMode(GL_MODELVIEW)
    return event.EVENT_HANDLED

@win.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0, 0, -100)
    draw(cube)

@win.event
def on_key_press(symbol, modifiers):
    if symbol == key.UP and modifiers & key.MOD_CTRL != key.MOD_CTRL:
        cube.y += 25
    elif symbol == key.DOWN and modifiers & key.MOD_CTRL != key.MOD_CTRL:
        cube.y -= 25
    elif symbol == key.LEFT:
        cube.x -= 25
    elif symbol == key.RIGHT:
        cube.x += 25
    elif symbol == key.UP and modifiers & key.MOD_CTRL == key.MOD_CTRL:
        cube.z -= 25
    elif symbol == key.DOWN and modifiers & key.MOD_CTRL == key.MOD_CTRL:
        cube.z += 25

win.set_visible(True)
clock.schedule(lambda t: rotate(cube))
app.run()
