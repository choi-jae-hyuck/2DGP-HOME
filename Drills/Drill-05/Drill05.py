from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')


x=0
frame=0

def ani_right(x,y,frame):
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame*100,100,100,100,x,y)
    update_canvas()
    delay(0.05)
    get_events()
def ani_left(x,y,frame):
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame*100,0,100,100,x,y)
    update_canvas()
    delay(0.05)
    get_events()

def move(x1,y1,x2,y2,frame):
    xpos=(x2-x1) // 30
    ypos=(y2-y1) // 30
    for i in range(1,30+1):
        x1 +=xpos
        y1 +=ypos
        frame=(frame+1)%8
        if (xpos>0):
            ani_right(x1,y1,frame)
        elif (xpos<0):
            ani_left(x1,y1,frame)

while(True):
    move(203,535,132,243,frame)
    move(132,243,535,470,frame)
    move(535,470,477,203,frame)
    move(477,203,715,136,frame)
    move(715,136,316,225,frame)
    move(316,225,510,92,frame)
    move(510,92,692,518,frame)
    move(692,518,682,336,frame)
    move(682,336,712,349,frame)
    move(712,349,203,535,frame)

        
        
    
close_canvas()
