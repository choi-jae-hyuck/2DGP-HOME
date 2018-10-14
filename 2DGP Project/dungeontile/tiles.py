from pico2d import *
import random
import random


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

class Floor:
    def __init__(self):
        self.state=random.randint(0,3)
        if(self.state==0):
            self.image=load_image('dungeon_floor.png')
        elif (self.state == 1):
            self.image = load_image('dungeon_floor2.png')
        elif (self.state == 2):
            self.image = load_image('dungeon_floor3.png')
        elif (self.state == 3):
            self.image = load_image('dungeon_floor4.png')

class Stair:
    def __init__(self):
        self.state=random.randint(0,1)
        if (self.state == 0):
            self.image = load_image('dungeon_stair.png')
        elif (self.state == 1):
            self.image = load_image('dungeon_stair2.png')

class Wall:
    def __init__(self):
        self.state=random.randint(0,1)
        if (self.state == 0):
            self.image = load_image('dungeon_wall.png')
        elif (self.state == 1):
            self.image = load_image('dungeon_wall2.png')

class Tile:
    def __init__(self):
        self.state=random.randint(0,3)
        self.x=0
        self.y=100
        if(self.state==0):
            self.type=Floor()
        elif(self.state==1):
            self.type=Stair()
        elif (self.state == 2):
            self.type = Wall()

    def draw(self):
        self.type.image.clip_draw(0,0, 48, 48, self.x, self.y)

open_canvas()
tile=Tile()

running = True

while running:
    clear_canvas()

    for i in range(20):
        tile.x=i*48
        tile.draw()

    update_canvas()

    handle_events()
    

    delay(0.05)

close_canvas()

