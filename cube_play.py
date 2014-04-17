import pyglet.app as app
import pyglet.window as window
import pyglet.gl as gl
import pyglet.text as text
import pyglet.clock as clock

class Cube():
    def __init__(self):
        self.x, self.y, self.z = 0, 0, 0
        self.side_length = 40
        self.colors = ((255,0,0), (0,255,0), (0,0,255), (255,0,0), (0,255,0), (0,0,255))

class Animation():
    def move_cube(self, tick):
        pass

    def start(self):
        self.cube = Cube()
        self.win = window.Window(width=640, height=480, caption="Cube Animation")
        
        gl.glEnable(gl.GL_DEPTH_TEST)

        @self.win.event
        def on_draw():
            gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
            
            gl.glLoadIdentity()
            
            # Front - Blended
            gl.glBegin(gl.GL_POLYGON)
            gl.glColor3f(1.0, 0.0, 0.0)
            gl.glVertex3f(0.5, -0.5, -0.5)
            gl.glColor3f(0.0, 1.0, 0.0)
            gl.glVertex3f(0.5, 0.5, -0.5)
            gl.glColor3f(0.0, 0.0, 1.0)
            gl.glVertex3f(-0.5,  0.5, -0.5)
            gl.glColor3f(0.0, 1.0, 1.0)
            gl.glVertex3f(-0.5, -0.5, -0.5)
            gl.glEnd()

            # Back - White
            gl.glBegin(gl.GL_POLYGON)
            gl.glColor3f(1.0, 1.0, 1.0)
            gl.glVertex3f(0.5, -0.5, 0.5)
            gl.glVertex3f(0.5, 0.5, 0.5)
            gl.glVertex3f(-0.5,  0.5, 0.5)
            gl.glVertex3f(-0.5, -0.5, 0.5)
            gl.glEnd()

            # Right - Purple
            gl.glBegin(gl.GL_POLYGON)
            gl.glColor3f(1.0, 0.0, 1.0)
            gl.glVertex3f(0.5, -0.5, -0.5)
            gl.glVertex3f(0.5, 0.5, -0.5)
            gl.glVertex3f(0.5, 0.5, 0.5)
            gl.glVertex3f(0.5, -0.5, 0.5)
            gl.glEnd()

            # Left - Green
            gl.glBegin(gl.GL_POLYGON)
            gl.glColor3f(0.0, 1.0, 0.0)
            gl.glVertex3f(-0.5, -0.5, 0.5)
            gl.glVertex3f(-0.5, 0.5, 0.5)
            gl.glVertex3f(-0.5, 0.5, -0.5)
            gl.glVertex3f(-0.5, -0.5, -0.5)
            gl.glEnd()

            # Top - Blue
            gl.glBegin(gl.GL_POLYGON)
            gl.glColor3f(0.0, 0.0, 1.0)
            gl.glVertex3f(0.5, 0.5, 0.5)
            gl.glVertex3f(0.5, 0.5, -0.5)
            gl.glVertex3f(-0.5, 0.5, -0.5)
            gl.glVertex3f(-0.5, 0.5, 0.5)
            gl.glEnd()

            # Bottom - Red
            gl.glBegin(gl.GL_POLYGON)
            gl.glColor3f(1.0, 0.0, 0.0)
            gl.glVertex3f(0.5, -0.5, -0.5)
            gl.glVertex3f(0.5, -0.5, 0.5)
            gl.glVertex3f(-0.5, -0.5, 0.5)
            gl.glVertex3f(-0.5, -0.5, -0.5)
            gl.glEnd()

            gl.glFlush()

            print("tick")
                    
        clock.schedule_interval(self.move_cube, 1/60.0)

    def pause(self):
        clock.unschedule(self.move_cube)

    def stop(self):
        clock.unschedule(self.move_cube)
        self.win.close()


def run(): app.run()
def stop(): app.exit()

# if __name__ == "__main__": run()




