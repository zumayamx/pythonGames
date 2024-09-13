from random import randrange, choice
from turtle import *
from freegames import square, vector

# Lista de colores posibles (excluyendo el rojo)
colors = ['blue', 'green', 'yellow', 'purple', 'orange']

# Escoge colores aleatorios para la serpiente y la comida
snake_color = choice(colors)
food_color = choice([color for color in colors if color != snake_color])

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Posibles movimientos de la comida: arriba, abajo, izquierda, derecha
food_moves = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(position):
    """Return True if position inside boundaries."""
    return -200 < position.x < 190 and -200 < position.y < 190


def move_food():
    """Move food randomly one step inside boundaries."""
    global food
    move_direction = choice(food_moves)
    new_position = food + move_direction

    if inside(new_position):
        food.move(move_direction)


def move():
    """Move snake forward one segment and food randomly."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    # Dibujar la serpiente
    for body in snake:
        square(body.x, body.y, 9, snake_color)

    # Mover la comida antes de dibujarla
    move_food()

    # Dibujar la comida
    square(food.x, food.y, 9, food_color)

    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()