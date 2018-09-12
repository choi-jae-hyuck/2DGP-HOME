from pico2d import *
from math import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=400
y=90
r=270
triger=0
while(True):
    while(x<780 and triger==0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x+5
        if(x==400and y==90):
            triger=1
        delay(0.01)
    while(y<550 and triger==0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y=y+5
        delay(0.01)
    while(x>0 and triger==0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x-5
        delay(0.01)
    while(y>90 and triger==0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y=y-5
        delay(0.01)
    while(triger==1):
        if(r==360):
            r=0
        r=r+1
        th=math.radians(r)
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x=x+(4*sin(th))
        y=y+(4*cos(th))
        if(r==270):
            triger=0
        delay(0.01)

close_canvas()
