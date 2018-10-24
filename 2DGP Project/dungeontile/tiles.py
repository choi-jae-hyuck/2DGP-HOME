from pico2d import *
import random
import map

class Floor:
    image1= None
    image2 = None
    image3 = None
    image4 = None
    def __init__(self):
        if Floor.image1==None :
            Floor.image1=load_image('dungeon_floor.png')
        elif Floor.image2==None :
            Floor.image2 = load_image('dungeon_floor2.png')
        elif Floor.image3 == None:
            Floor.image3 = load_image('dungeon_floor3.png')
        elif Floor.image4 == None:
            Floor.image4 = load_image('dungeon_floor4.png')

class Stair:
    image1=None
    image2=None
    def __init__(self):
        if Stair.image1==None:
            Stair.image1 = load_image('dungeon_stair.png')
        elif Stair.image2 == None:
            Stair.image2 = load_image('dungeon_stair2.png')

class Wall:
    image1=None
    image2=None
    def __init__(self):
        if Wall.image1==None:
            Wall.image1 = load_image('dungeon_wall.png')
        elif Wall.image2==None:
            Wall.image2 = load_image('dungeon_wall2.png')

def MapDraw(list,x,y):
    for i in range(y,y+12):
        for j in range(x,x+16):
            if list[y][x]== 'floor':
                Floor.image1.clip_draw(0, 0, 41, 41, 25 + (i * 50), 25 + (j * 50), 50, 50)
            elif list[y][x]=='wall':
                Wall.image1.clip_draw(0, 0, 41, 41, 25 + i * 50, 25 + j * 50, 50, 50)
