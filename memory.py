from random import shuffle
from turtle import *

from freegames import path

car = path('car.gif')
letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)] * 2
letters = letters[:64]
shuffle(letters)
state = {'mark': None}
hide = [True] * 64
taps = 0

def square(x, y):
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    global taps
    taps += 1
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or letters[mark] != letters[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def all_uncovered():
    return all(not hidden for hidden in hide)

def draw():
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    goto(-200, 200)
    write(f'Taps: {taps}', font=('Arial', 16, 'normal'))

    if all_uncovered():
        goto(0, 0)
        write('¡Juego completado!', align='center', font=('Arial', 30, 'bold'))
        update()
        return

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 17, y + 5)
        color('black')
        write(letters[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
