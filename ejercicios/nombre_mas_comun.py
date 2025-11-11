# Programa para identificar el nombre más común.

# Lista de nombres con repeticiones
nombres = ["Juan", "Pepito", "Rosa", "Juan", "Pedro", "Rosa", "Juan"]

# Diccionario para contar apariciones de cada nombre
cuenta_nombres = {}

# Recorremos la lista de nombres
for nombre in nombres:
    # Si el nombre no está ya contado, lo contamos usando .count()
    nombre_esta = cuenta_nombres.get(nombre)
    if not nombre_esta:
        cuenta_nombres[nombre] = nombres.count(nombre)

# Mostramos el diccionario con los conteos
print(cuenta_nombres)

# Encontramos el nombre más común (el que más veces aparece)
print(max(cuenta_nombres, key=cuenta_nombres.get))


# Explicación paso a paso del código:
""" 
1. La lista `nombres` contiene varios nombres, algunos repetidos.

2. Creamos un diccionario `cuenta_nombres` para guardar cuántas veces aparece cada nombre.

3. Con un bucle `for`, recorremos cada nombre en la lista:
    - Si aún no está en el diccionario (lo verificamos con `get(nombre)`), lo agregamos y usamos `nombres.count(nombre)` para saber cuántas veces aparece.

4. Usamos `print(cuenta_nombres)` para ver cuántas veces aparece cada nombre.

5. Luego usamos `max(cuenta_nombres, key=cuenta_nombres.get)` para encontrar la clave (nombre) que tenga el valor más alto (más apariciones).
    - Aquí `key=cuenta_nombres.get` le dice a `max()` que debe comparar los nombres usando el número de veces que aparecen. """

# otro ejemplo de solucion mas entendible


def nombre_mas_repetido(lista_nombres):
    cuenta_nombres = {}  # Diccionario para contar cada nombre

    # Contamos cuántas veces aparece cada nombre
    for nombre in lista_nombres:
        if nombre in cuenta_nombres:
            cuenta_nombres[nombre] += 1
        else:
            cuenta_nombres[nombre] = 1

    # Buscamos la clave (nombre) con el valor más alto
    mas_repetido = max(cuenta_nombres, key=cuenta_nombres.get)

    return mas_repetido


# Ejemplo de uso
nombres = ["Ana", "Luis", "Ana", "Pedro", "Luis", "Ana", "Carlos", "Luis"]
print(nombre_mas_repetido(nombres))  # Ana
