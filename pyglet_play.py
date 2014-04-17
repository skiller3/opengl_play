import pyglet.app as app
import pyglet.window as window
import pyglet.gl as gl
import pyglet.text as text
import pyglet.clock as clock

text_pos_x = 0
text_pos_y = 0

win = window.Window(width=640, height=480)

motion = 1

label = text.Label(text="Hello, World!", font_name="Times New Roman", font_size=12.0,
                   anchor_x="center", anchor_y="center", x=text_pos_x,
                   y=text_pos_y)

def draw_text():
    win.clear()
    label.draw()
    
win.on_draw = win.event(draw_text)

def move_label(date):
    global text_pos_x
    global text_pos_y
    global motion
    if (text_pos_x <= 0):
        motion = 1
    elif (text_pos_x >= win.width):
        motion = -1
    text_pos_x = text_pos_x + motion
    text_pos_y = text_pos_y + motion
    label.x = text_pos_x
    label.y = text_pos_y
    print((text_pos_x, text_pos_y))

clock.schedule_interval(move_label, 1/60.0)

app.run()



