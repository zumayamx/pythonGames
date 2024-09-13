"""
José Manuel García Zumaya - A01784238
Pacman Game - Freegames
"""

from turtle import *

from math import sqrt

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def draw_circle(start, end):
    """Dibuja un círculo desde start hasta end."""
    up()
    # Mover al punto de inicio (centro del círculo)
    goto(start.x, start.y)
    down()

    # Calcular el radio como la distancia entre start y end
    radius = sqrt((end.x - start.x) ** 2 + (end.y - start.y) ** 2)

    # Validar que el radio sea positivo
    if radius <= 0:
        print("El radio es demasiado pequeño para dibujar un círculo.")
        return
    
    print(f"Radio calculado: {radius}")

    begin_fill()
    # Dibujar el círculo usando el radio calculado
    circle(radius)
    end_fill()


def rectangle(start, end):
    """Dibuja un rectángulo desde start hasta end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    # Calcular las dimensiones del rectángulo
    width = end.x - start.x
    height = end.y - start.y

    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)

    end_fill()


def triangle(start, end):
    """Draw triangle from start to end."""
    pass  # TODO


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')  # Nuevo color amarillo
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', draw_circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()