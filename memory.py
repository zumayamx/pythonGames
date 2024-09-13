from random import shuffle
from turtle import *

from freegames import path

car = path('car.gif')
letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'cyan']

elements = [(letter, color) for letter in letters for color in colors[:8]]
elements = elements * 2
elements = elements[:64]
shuffle(elements)
state = {'mark': None}
hide = [True] * 64
taps = 0

def square(x, y):
    """Dibuja un cuadrado en la posición (x, y)."""
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
    """Convierte las coordenadas (x, y) en un índice de casilla."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    """Convierte un índice de casilla en coordenadas (x, y)."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    """Maneja el evento de clic en la posición (x, y)."""
    global taps
    taps += 1
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or elements[mark] != elements[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

def all_uncovered():
    """Verifica si todos los cuadros han sido destapados."""
    return all(not hidden for hidden in hide)

def draw():
    """Dibuja el estado actual del juego y actualiza la pantalla."""
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
        color_value = elements[mark][1]
        color(color_value)
        goto(x + 17, y + 5)
        write(elements[mark][0], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)

setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
