import random
import json
import os

from pico2d import *

import game_framework
import main_state



name = "MainState"

boy = None
grass = None
font = None



class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Pause:
    def __init__(self):
        self.image = load_image('pause.png')
        self.blink=0

    def draw(self):
        if(self.blink==0):
            self.image.draw(400, 400)
        elif(self.blink==1):
            pass
    def update(self):
        self.blink = (self.blink+1) % 2

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.dir = 1

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def enter():
    global pauseicon
    pauseicon=Pause()


def exit():
    global pauseicon
    del(pauseicon)
    pass


def pause():
        pass


def resume():
    pass


def handle_events():
    events= get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type ==SDL_KEYDOWN and event.key ==SDLK_ESCAPE:
            game_framework.change_state(main_state)
        elif event.type ==SDL_KEYDOWN and event.key == SDLK_o:
            game_framework.pop_state()


def update():
    pass


def draw():
    clear_canvas()
    pauseicon.draw()
    main_state.grass.draw()
    main_state.boy.draw()

    pauseicon.update()
    update_canvas()





