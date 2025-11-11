""" Desafío 1: Filtrado de Temperaturas
Dada una lista de temperaturas en Celsius (pueden ser números negativos y positivos), crea una list comprehension que solo incluya las temperaturas positivas """

temperaturas = [-5, 10, -2, 15, -8, 23, 0, 12, -3, 27, -15]
# Crear lista solo con temperaturas positivas
temperaturas_positivas = [t for t in temperaturas if t > 0]
print("Temperaturas positivas:", temperaturas_positivas)

""" Desafío 2: Procesamiento de Strings
Dada una lista de nombres, crea una list comprehension que genere una nueva lista con los nombres que:
Empiecen con vocal
Tengan más de 5 letras """

nombres = ["Ana", "Eduardo", "Isabel", "Francisco",
           "Omar", "Pedro", "Ursula", "Roberto"]
# Crear lista con nombres que cumplan las condiciones
new_names = [n for n in nombres if n[0].upper() in 'AEIOU' and len(n) > 5]
print("Nombres que empiezan con vocal y tienen más de 5 letras:", new_names)

"""Desafío 3: Matriz de Multiplicación
Crea una list comprehension que genere una matriz 5x5 donde cada elemento sea el producto de sus índices (i,j).
Por ejemplo, el elemento en la posición [2][3] debería ser 6 (2*3)."""
matriz_multiplicacion = [[i * j for j in range(5)] for i in range(5)]
print("Matriz de multiplicación 5x5:")
for fila in matriz_multiplicacion:
    for j in fila:
        print(f"{j:3}", end=" ")
    print(fila)
"""Desafío 4: Procesamiento de Fechas
Dada una lista de años, crea una list comprehension que identifique cuáles son años bisiestos.
Un año es bisiesto si es divisible por 4 y no por 100, o si es divisible por 400."""

anios = [2000, 2001, 2002, 2003, 2004, 2005, 2006,
         2007, 2008, 2009, 2010, 2011, 2012, 2020, 2024]
# Crear lista con años bisiestos
anios_bisiestos = [a for a in anios if (
    a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)]
print("Años bisiestos:", anios_bisiestos)
"""Desafío 5: Transformación de Datos
Dada una lista de diccionarios con información de estudiantes, crea una list comprehension que extraiga solo los nombres de los estudiantes que tienen un promedio superior a 8.5"""
estudiantes = [
    {"nombre": "Ana", "promedio": 9.5},
    {"nombre": "Juan", "promedio": 8.2},
    {"nombre": "María", "promedio": 9.0},
    {"nombre": "Carlos", "promedio": 7.8},
    {"nombre": "Laura", "promedio": 8.7}
]

# Extraer diccionarios con promedio > 8.5
estudiantes_dest = {indice: valor for indice, valor in enumerate(
    estudiantes) if valor["promedio"] > 8.5}
print("\nEstudiantes destacados por índice:")
print(estudiantes_dest)
for indice, estudiante in estudiantes_dest.items():
    print(
        f"Índice {indice}: Nombre: {estudiante['nombre']:8} | Promedio: {estudiante['promedio']:.1f}")

# Crear lista con nombres de estudiantes que cumplan la condición
estudiantes_destacados = [e["nombre"]
                          for e in estudiantes if e["promedio"] > 8.5]
print("Estudiantes con promedio superior a 8.5:", estudiantes_destacados)
