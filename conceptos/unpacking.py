# ============================================================
# 1️⃣ UNPACKING EN ASIGNACIONES
# ============================================================

# Unpacking básico de una lista o tupla
numeros = [1, 2, 3]
a, b, c = numeros
print(f"Unpacking básico: a={a}, b={b}, c={c}")

# Extended unpacking con *
primero, *resto, ultimo = [1, 2, 3, 4, 5]
print(f"Extended unpacking: primero={primero}, resto={resto}, ultimo={ultimo}")

# Unpacking en bucles
pares = [(1, 'uno'), (2, 'dos'), (3, 'tres')]
for numero, nombre in pares:
    print(f"Número: {numero}, Nombre: {nombre}")
# ============================================================
# 2️⃣ UNPACKING EN LLAMADAS A FUNCIONES
# ============================================================


def suma(a, b, c):
    return a + b + c


numeros = [1, 2, 3]
resultado = suma(*numeros)  # Equivalente a suma(1, 2, 3)
print(f"\nSuma usando unpacking de lista: {resultado}")

# Unpacking de diccionario como argumentos nombrados


def crear_persona(nombre, edad, profesion):
    return f"{nombre} tiene {edad} años y es {profesion}"


datos = {'nombre': 'Ana', 'edad': 28, 'profesion': 'ingeniera'}
# Equivalente a crear_persona(nombre='Ana', edad=28, profesion='ingeniera')
persona = crear_persona(**datos)
print(f"Persona creada con unpacking de diccionario: {persona}")

# ============================================================
# 3️⃣ UNPACKING EN DEFINICIÓN DE FUNCIONES
# ============================================================

# *args para argumentos posicionales variables


def concatenar(*palabras):
    """Concatena cualquier número de palabras con espacios."""
    return ' '.join(palabras)


print(f"\nConcatenación: {concatenar('Hola', 'mundo', 'Python')}")

# **kwargs para argumentos nombrados variables


def imprimir_datos(**datos):
    """Imprime pares clave-valor de forma ordenada."""
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")


print("\nDatos del usuario:")
imprimir_datos(nombre="Carlos", edad=30, ciudad="Madrid")

# Combinando argumentos posicionales, args y kwargs


def funcion_hibrida(arg1, arg2, *args, kwarg1="default", **kwargs):
    print(f"Argumentos posicionales: {arg1}, {arg2}")
    print(f"Args adicionales: {args}")
    print(f"Kwarg1: {kwarg1}")
    print(f"Kwargs adicionales: {kwargs}")


print("\nEjemplo de función híbrida:")
funcion_hibrida(1, 2, 3, 4, kwarg1="personalizado",
                extra1="valor1", extra2="valor2")

# ============================================================
# 4️⃣ CASOS DE USO AVANZADOS
# ============================================================

# Unpacking múltiple en una línea
a, b, *rest = [1, 2, 3, 4, 5]
print(f"\nUnpacking múltiple: a={a}, b={b}, rest={rest}")

# Intercambio de variables
x, y = 10, 20
x, y = y, x  # Intercambio sin variable temporal
print(f"Después del intercambio: x={x}, y={y}")

# Ignorar valores con _
nombre, _, edad = ["Ana", "dato_no_importante", 25]
print(f"Ignorando valor del medio: {nombre} tiene {edad} años")

# Unpacking anidado
((a, b), (c, d)) = [(1, 2), (3, 4)]
print(f"Unpacking anidado: a={a}, b={b}, c={c}, d={d}")

if __name__ == '__main__':
    # Los ejemplos ya se ejecutan a medida que se define el código
    pass
