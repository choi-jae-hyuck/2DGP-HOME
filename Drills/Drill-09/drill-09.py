from pico2d import *
import random

# Game object class here

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

class Grass:
    def __init__(self):
        self.image=load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700),90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 600
        self.plus=random.randint(5,30)
        self.size=random.randint(1,2)
        if(self.size==1):
            self.image = load_image('ball21x21.png')
        elif(self.size==2):
            self.image = load_image('ball41x41.png')

    def update(self):
        if(self.y>60):
            self.y -= self.plus
        elif(self.y<60):
            self.y=60

    def draw(self):
        self.image.draw(self.x, self.y)


open_canvas()
grass = Grass()
running = True;

team = [Boy() for i in range(11)]
balls =[Ball() for i in range(20)]

while running:
    handle_events()
    for boy in team:
        boy.update()
    for ball in balls:
        ball.update()

    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for ball in balls:
        ball.draw()
    update_canvas()
    delay(0.05)

close_canvas()
#the end


# initialization code

# game main loop code

# finalization code