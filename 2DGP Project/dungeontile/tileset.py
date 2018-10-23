from pico2d import *
import random

import tiles
import map

gen=map.Generator()
gen.gen_level()
open_canvas()

floor=tiles.Floor()
wall=tiles.Wall()

running=True
while running:
    clear_canvas()
    for i in range(0,16):
        for j in range(0,12):
            if gen.level[j][i]=='floor':
                floor.image1.clip_draw(0,0,41,41,i*50,j*50,50,50)
            elif gen.level[j][i]=='wall':
                wall.image1.clip_draw(0, 0, 41, 41, i * 50, j * 50, 50, 50)
    update_canvas()
    delay(0.05)

close_canvas()
