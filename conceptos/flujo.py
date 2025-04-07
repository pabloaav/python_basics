# =====================================================================
# CONTROL DE FLUJO EN PYTHON
# =====================================================================

# ----- Condicionales (if-elif-else) -----

# Estructura básica if-else
edad = 20
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")

# Estructura if-elif-else
puntuacion = 85
if puntuacion >= 90:
    calificacion = "A"
elif puntuacion >= 80:
    calificacion = "B"
elif puntuacion >= 70:
    calificacion = "C"
elif puntuacion >= 60:
    calificacion = "D"
else:
    calificacion = "F"

print(f"Puntuación: {puntuacion}, Calificación: {calificacion}")

# Operadores de comparación:
# == (igual)
# != (distinto)
# > (mayor que)
# < (menor que)
# >= (mayor o igual que)
# <= (menor o igual que)

# Operadores lógicos
edad = 25
tiene_licencia = True

if edad >= 18 and tiene_licencia:
    print("Puede conducir")
else:
    print("No puede conducir")

# Operador ternario (útil para asignaciones condicionales simples)
estado = "aprobado" if puntuacion >= 60 else "reprobado"
print(f"Estado: {estado}")

# Verificar si un valor está en una colección
fruta = "manzana"
if fruta in ["manzana", "naranja", "plátano"]:
    print(f"{fruta} está en la lista de frutas")

# ----- Bucles -----

# Bucle for (muy usado en data science para iterar sobre datos)
print("\nBucle for con range:")
for i in range(5):  # 0, 1, 2, 3, 4
    print(i)

# Iterar sobre una lista
nombres = ["Ana", "Carlos", "Elena"]
print("\nIterando sobre una lista:")
for nombre in nombres:
    print(f"Hola, {nombre}")

# Iterar con enumerate (obtiene índice y valor)
print("\nUsando enumerate:")
for indice, nombre in enumerate(nombres):
    print(f"Índice {indice}: {nombre}")

# Bucle for con diccionarios
estudiante = {"nombre": "María", "edad": 22, "carrera": "Ciencia de Datos"}
print("\nIterando sobre un diccionario:")
for i in estudiante:
    print(f"{i}: {estudiante[i]}")

# Iterar sobre una tupla
mi_tupla = ("manzana", "banana", "cereza")

for fruta in mi_tupla:
    print(fruta)
for i, fruta in enumerate(mi_tupla):
    print(f"{i}: {fruta}")


# Mejor forma de iterar sobre diccionarios
print("\nIterando con .items():")
for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")

# Bucle while
contador = 0
print("\nBucle while:")
while contador < 5:
    print(contador)
    contador += 1

# Control de bucles: break y continue
print("\nUsando break:")
for i in range(10):
    if i == 5:
        break  # Sale del bucle cuando i==5
    print(i)

print("\nUsando continue:")
for i in range(10):
    if i % 2 == 0:
        continue  # Salta a la siguiente iteración si i es par
    print(i)

# Bucles anidados (comunes en procesamiento de matrices)
print("\nBucles anidados:")
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# Comprensión de listas como alternativa a los bucles for
# (muy común y eficiente en data science)
numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros]
print(f"\nCuadrados mediante comprensión de listas: {cuadrados}")

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

# Usamos zip para sumar elemento a elemento
suma = [a + b for a, b in zip(lista1, lista2)]
print(zip(lista1, lista2))
print(list(zip(lista1, lista2)))  # Resultado: [(1, 4), (2, 5), (3, 6)]
# Sumar elemento a elemento
print(suma)  # Resultado: [5, 7, 9]


# Con condición
pares = [x for x in range(10) if x % 2 == 0]
print(f"Números pares: {pares}")

# ----- Funciones -----

# Definición básica de una función
def saludar(nombre):
    """Función que saluda a una persona."""
    return f"Hola, {nombre}!"

# Llamada a la función
mensaje = saludar("Carlos")
print(f"\n{mensaje}")

# Función con parámetros por defecto
def saludar_formal(nombre, titulo="Sr./Sra."):
    return f"Saludos, {titulo} {nombre}"

print(saludar_formal("García"))  # Usa el valor por defecto
print(saludar_formal("López", "Dr."))  # Sobreescribe el valor por defecto

# Funciones con múltiples parámetros
def calcular_estadisticas(numeros):
    """Calcula estadísticas básicas de una lista de números."""
    return {
        "suma": sum(numeros),
        "promedio": sum(numeros) / len(numeros),
        "min": min(numeros),
        "max": max(numeros)
    }

datos = [10, 15, 20, 25, 30]
estadisticas = calcular_estadisticas(datos)
print(f"\nEstadísticas: {estadisticas}")

# Parámetros posicionales vs. nombrados
def dividir(a, b):
    return a / b

# Diferentes formas de llamar a la función
resultado1 = dividir(10, 2)  # Parámetros posicionales
resultado2 = dividir(a=10, b=2)  # Parámetros nombrados
resultado3 = dividir(b=2, a=10)  # Orden diferente pero mismo resultado

print(f"\nResultados de división: {resultado1}, {resultado2}, {resultado3}")

# *args para número variable de argumentos posicionales
def sumar(*numeros):
    """Suma cualquier cantidad de números."""
    total = 0
    for num in numeros:
        total += num
    return total

print(f"\nSuma de 1+2: {sumar(1, 2)}")
print(f"Suma de 1+2+3+4: {sumar(1, 2, 3, 4)}")

# **kwargs para número variable de argumentos nombrados
def crear_perfil(**datos):
    """Crea un perfil con los datos proporcionados."""
    return datos

perfil = crear_perfil(nombre="Ana", edad=28, profesion="Data Scientist")
print(f"\nPerfil: {perfil}")

# Combinando *args y **kwargs
def super_funcion(*args, **kwargs):
    """Función que acepta cualquier cantidad de argumentos."""
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")

super_funcion(1, 2, 3, a=10, b=20)

# Funciones lambda (anónimas) - muy útiles para operaciones rápidas
duplicar = lambda x: x * 2
print(f"\nDuplicar 5: {duplicar(5)}")

# Uso común de lambdas con funciones como map, filter, sorted
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(f"Cuadrados con map: {cuadrados}")

pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Pares con filter: {pares}")

estudiantes = [
    {"nombre": "Ana", "promedio": 9.5},
    {"nombre": "Carlos", "promedio": 8.2},
    {"nombre": "Elena", "promedio": 9.8}
]

# Ordenar por promedio usando lambda
ordenados = sorted(estudiantes, key=lambda e: e["promedio"], reverse=True)
print(f"\nEstudiantes ordenados por promedio:")
for e in ordenados:
    print(f"{e['nombre']}: {e['promedio']}")

# Funciones como objetos de primera clase
def aplicar_operacion(lista, operacion):
    """Aplica una operación a cada elemento de la lista."""
    return [operacion(x) for x in lista]

def cuadrado(x):
    return x ** 2

def cubo(x):
    return x ** 3

numeros = [1, 2, 3, 4]
print(f"\nCuadrados: {aplicar_operacion(numeros, cuadrado)}")
print(f"Cubos: {aplicar_operacion(numeros, cubo)}")
print(f"Duplicados: {aplicar_operacion(numeros, lambda x: x * 2)}")