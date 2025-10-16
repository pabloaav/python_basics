from functools import reduce
nombres = ["Ana", "Bernardo", "Carlos", "Diana",
           "Eduardo", "Fernanda", "Alan", "Alicia", "anita"]

# Filtrar los nombres que comienzan con 'A' o 'a'
nombres_con_a = list(
    filter(lambda n: n.startswith(('A', 'a',)), nombres))
print(nombres_con_a)  # Resultado: ['Ana', 'Alan', 'Alicia', 'anita']

# filtrar una lista de tuplas de estdiantes para ordenarlos con la funcion sorted por alguna de sus propiedades
estudiantes = [
    ("Ana", 23, "Ingeniería", 8.5),
    ("Bernardo", 21, "Medicina", 7.8),
    ("Carlos", 25, "Arquitectura", 9.2),
    ("Diana", 22, "Economía", 8.9)
]

# Ordenar por el promedio (cuarto elemento de la tupla)
estudiantes_ordenados = sorted(
    estudiantes, key=lambda e: e[3], reverse=True)
print(estudiantes_ordenados)

# ============================================================
# 🚀 Orden superior usando reduce
# ============================================================
# Calcular la suma de una lista de números usando reduce
numeros = [1, 2, 3, 4, 5]
suma = reduce(lambda x, y: x + y, numeros)
print(suma)  # Resultado: 15
