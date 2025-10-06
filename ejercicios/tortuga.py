import turtle

window = turtle.Screen()
window.bgcolor("white")
tortuga = turtle.Turtle()
tortuga.color("red")
tortuga.shape("turtle")
tortuga.speed(1)

# Dibujamos un cuadrado
for _ in range(4):
    tortuga.forward(100)  # Avanza 100 unidades
    tortuga.right(90)    # Gira 90 grados a la derecha

window.mainloop()  # Mantiene la ventana abierta
