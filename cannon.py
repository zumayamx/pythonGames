from random import randrange  
from turtle import *  
from freegames import vector  

# Inicializa la posición de la bola y su velocidad.
ball = vector(-200, -200)
speed = vector(0, 0)

# Lista para almacenar los objetivos.
targets = []

# Función que se ejecuta cuando se hace clic en la pantalla.
def tap(x, y):
    # Si la bola no está dentro de la ventana, inicializa su posición y velocidad.
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        # Calcula la velocidad de la bola en función de la posición del clic.
        speed.x = (x + 200) / 15  
        speed.y = (y + 200) / 15  

# Función que verifica si está dentro de los límites de la ventana.
def inside(xy):
    return -200 < xy.x < 200 and -200 < xy.y < 200

# Función que crea la bola y los objetivos en la pantalla.
def draw():
    clear()  

    # Crea cada objetivo en la lista de targets.
    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')  

    # Crea la bola si está dentro de la ventana.
    if inside(ball):
        goto(ball.x, ball.y)
        dot(6, 'red')  

    update()  

# Función que mueve los objetivos y la bola.
def move():
    # Cada 40 iteraciones, crea un nuevo objetivo en el borde derecho de la pantalla.
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
        # Si el objetivo no choca con la bola, lo mantiene en la lista.
        if abs(target - ball) > 13:
            # Si el objetivo sale de la ventana, lo reposiciona en el borde derecho.
            if not inside(target):
                target.x = 200
            targets.append(target)  
    draw()  
    ontimer(move, 25)  

# Configura la ventana de juego.
setup(420, 420, 370, 0)
hideturtle()  
up()  
tracer(False)  
onscreenclick(tap) #
move()  
done()  
