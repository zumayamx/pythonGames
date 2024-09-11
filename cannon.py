from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 15  
        speed.y = (y + 200) / 15  

def inside(xy):
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 1.0  

    if inside(ball):
        speed.y -= 0.5  
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            if not inside(target):
                target.x = 200  
            targets.append(target)

    draw()

    ontimer(move, 25)  

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
