from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


x=0
frame=0
triger=0

def ani_right(x,y,frame):
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame*100,100,100,100,x,90)
    update_canvas()
    frame=(frame+1)%8
    delay(0.05)
    get_events()
def ani_left():
    clear_canvas(x,y,frame)
    grass.draw(400,30)
    character.clip_draw(frame*100,0,100,100,x,90)
    update_canvas()
    frame=(frame+1)%8
    delay(0.05)
    get_events()

def move(x1,y1,x2,y2):
    xpos=(x2-x1) // 30
    ypos=(y2-y1) // 30
    while(x1!=x2):
        x1 +=xpos
        y1 +=ypos
        if (x1<x2):
            ani_right(x1,y1,frame)
        elif (x1>x2):
            ani_left(x1,y1,frame)


        
        
    
close_canvas()
