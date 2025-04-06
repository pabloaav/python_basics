puntuacion = int(input("Ingrese una puntuacion entre 0 y 10: "))
puntuacion_permitida = range(0, 11)

if puntuacion in puntuacion_permitida:
    # continuar al chequeo de la nota
    if puntuacion >= 9:
        print("Su nota es A.")
    elif puntuacion >= 8:
        print("Su nota es B.")
    elif puntuacion >= 7:
        print("Su nota es C.")
    elif puntuacion >= 6:
        print("Su nota es D.")
    else:
        print("Su nota es F.")
else:
    print("¡Error! Puntuacion fuera de rango.")
