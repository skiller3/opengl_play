from pyglet.gl import *
import pyglet.window as window
import pyglet.app as app
import ctypes

# -------------------------------- SHADERS ------------------------------------

TRIANGLES_VERT = """

#version 430 core

layout(location = 0) in vect4 vPosition;

void
main()
{
    glPosition = vPosition;
}
"""

TRIANGLES_FRAG = """

#version 430 core

out vec4 fColor;

void
main()
{
    fColor = vec4(0.0, 0.0, 1.0, 1.0);
}
"""

# ---------------------------------------------------------------------------

def GLfloatArray(*args):
    return (GLfloat * len(args))(*[float(n) for n in args])


def GLuintArray(*args):
    return (GLuint * len(args))(*[int(n) for n in args])


win = window.Window(resizable=False, width=512, height=512)


def init():
    init_shaders()

    buffer_names = GLuintArray(0)

    glGenBuffers(1, buffer_names)
    print("Buffer name is " + buffer_names[0])

    glBindBuffers(GL_ARRAY_BUFFER, buffer_names[1])
    vertices = GLfloatArray(-0.90, -0.90, 0.85, -0.90, -0.90, 0.85, 0.90, -0.85, 0.90, 
                            0.90, -0.85, 0.90)
    glBufferData(GL_ARRAY_BUFFER, ctypes.sizeof(vertices), GL_STATIC_DRAW)
    
def init_shaders():
    vshader = glCreateShader(GL_VERTEX_SHADER)
    fshader = glCreateShader(GL_FRAGMENT_SHADER)
    
