import turtle

window = turtle.Screen()
window.bgcolor("white")
tortuga = turtle.Turtle()
tortuga.color("blue")
tortuga.shape("turtle")
tortuga.speed(3)  # Un poco más rápido para que no tarde tanto

# Función para dibujar un triángulo equilátero


def dibujar_triangulo(direccion):
    for _ in range(3):
        tortuga.forward(100)
        if direccion == "up":
            tortuga.left(120)  # Gira 120 grados a la izquierda
        else:
            tortuga.right(120)  # Gira 120 grados a la derecha


# Posicionamos la tortuga para el primer triángulo (apuntando hacia arriba)
tortuga.penup()
tortuga.goto(-50, -50)  # Base del primer triángulo
tortuga.pendown()

# Dibujamos el primer triángulo (apuntando hacia arriba)
dibujar_triangulo("up")

# Posicionamos la tortuga para el segundo triángulo (apuntando hacia abajo)
tortuga.penup()
# Posición centrada verticalmente para el segundo triángulo
tortuga.goto(-50, 0)
tortuga.pendown()

# Dibujamos el segundo triángulo (apuntando hacia abajo)
dibujar_triangulo("down")

window.exitonclick()  # Mantiene la ventana abierta
