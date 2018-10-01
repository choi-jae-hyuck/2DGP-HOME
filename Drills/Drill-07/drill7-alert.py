from pico2d import *
import turtle
import random


def stop():
    turtle.bye()

def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()



def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_curve_10_points(p1, p2, p3, p4,p5,p6,p7,p8,p9,p10):
    draw_big_point(p1)
    draw_big_point(p2)
    draw_big_point(p3)
    draw_big_point(p4)
    draw_big_point(p5)
    draw_big_point(p6)
    draw_big_point(p7)
    draw_big_point(p8)
    draw_big_point(p9)
    draw_big_point(p10)

    for i in range(0, 20 + 1, 2):
        t = i / 20
        x = (1 - t) * p1[0] + t * p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        draw_point((x, y))
    draw_point(p2)

    for i in range(0, 20 + 1, 2):
        t = i / 20
        x = (1 - t) * p2[0] + t * p3[0]
        y = (1 - t) * p2[1] + t * p3[1]
        draw_point((x, y))
    draw_point(p3)

    for i in range(0, 20 + 1, 2):
        t = i / 20
        x = (1 - t) * p3[0] + t * p4[0]
        y = (1 - t) * p3[1] + t * p4[1]
        draw_point((x, y))
    draw_point(p4)

    for i in range(0, 20+ 1, 2):
        t = i / 20
        x = (1 - t) * p4[0] + t * p5[0]
        y = (1 - t) * p4[1] + t * p5[1]
        draw_point((x, y))
    draw_point(p5)

    for i in range(0, 20+ 1, 2):
        t = i / 20
        x = (1 - t) * p5[0] + t * p6[0]
        y = (1 - t) * p5[1] + t * p6[1]
        draw_point((x, y))
    draw_point(p6)

    for i in range(0, 20 + 1, 2):
        t = i / 20
        x = (1 - t) * p6[0] + t * p7[0]
        y = (1 - t) * p6[1] + t * p7[1]
        draw_point((x, y))
    draw_point(p7)

    for i in range(0, 20 + 1, 2):
        t = i / 20
        x = (1 - t) * p7[0] + t * p8[0]
        y = (1 - t) * p7[1] + t * p8[1]
        draw_point((x, y))
    draw_point(p8)

    for i in range(0, 20 + 1, 2):
        t = i / 20
        x = (1 - t) * p8[0] + t * p9[0]
        y = (1 - t) * p8[1] + t * p9[1]
        draw_point((x, y))
    draw_point(p9)

    for i in range(0, 20 + 1, 2):
        t = i / 20
        x = (1 - t) * p9[0] + t * p10[0]
        y = (1 - t) * p9[1] + t * p10[1]
        draw_point((x, y))
    draw_point(p10)

    for i in range(0, 20 + 1, 2):
        t = i / 20
        x = (1 - t) * p10[0] + t * p1[0]
        y = (1 - t) * p10[1] + t * p1[1]
        draw_point((x, y))
    draw_point(p1)


a1=[random.randint(-300,300) for n in range(2)]
a2=[random.randint(-300,300) for n in range(2)]
a3=[random.randint(-300,300) for n in range(2)]
a4=[random.randint(-300,300) for n in range(2)]
a5=[random.randint(-300,300) for n in range(2)]
a6=[random.randint(-300,300) for n in range(2)]
a7=[random.randint(-300,300) for n in range(2)]
a8=[random.randint(-300,300) for n in range(2)]
a9=[random.randint(-300,300) for n in range(2)]
a10=[random.randint(-300,300) for n in range(2)]


KPU_WIDTH, KPU_HEIGHT = 1280, 1024
kpu_ground = load_image('KPU_G.png')
character = load_image('animation_sheet.png')
running = True
px, py = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * 1, 100, 100, px, py)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.02)

close_canvas()


turtle.done()
