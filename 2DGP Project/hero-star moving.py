from pico2d import *


def handle_events():
    # fill here
    pass


open_canvas()
star = load_image('star.png')
hero = load_image('hero.png')

running = True
x = 800 // 2
star_frame=0
hero_frame = 0

while running:
    clear_canvas()
    star.clip_draw(star_frame * 34 +2,1451 * 1, 31, 31, x, 155)
    hero.clip_draw(hero_frame * 33,1082 * 1, 33, 57, x, 55)
    update_canvas()

    handle_events()
    hero_frame = (hero_frame + 1) % 6
    star_frame = (star_frame + 1) % 8

    delay(0.05)

close_canvas()

