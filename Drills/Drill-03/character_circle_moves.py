from pico2d import *
from math import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=400
y=100
r=270
while(True):
    if(r==360):
        r=0
    r=r+1
    th=math.radians(r)
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    x=x+(4*sin(th))
    y=y+(4*cos(th))
    delay(0.01)

close_canvas()
