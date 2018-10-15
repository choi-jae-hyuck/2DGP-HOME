import random
import json
import os

from pico2d import *

import game_framework
import title_state
import pause_state
import pause_moving_state
from boy import Boy



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

    def draw(self):
        self.image.draw(400,400)



def enter():
    global boy,grass,pauseicon
    boy =Boy()
    grass = Grass()
    pauseicon=Pause()

def exit():
    global boy,grass,pauseicon
    del(boy)
    del(grass)
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
            game_framework.change_state(title_state)
        elif event.type ==SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_state)
        elif event.type ==SDL_KEYDOWN and event.key == SDLK_o:
            game_framework.push_state(pause_moving_state)


def update():
    boy.update()


def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()


