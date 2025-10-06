# =====================================================================
# ESTRUCTURAS DE DATOS EN PYTHON
# =====================================================================

# ----- Listas -----
# Las listas son fundamentales en data science para almacenar colecciones de datos

# Creación de listas
numeros = [1, 2, 3, 4, 5]
nombres = ["Ana", "Juan", "Pedro"]
mixta = [1, "Dos", 3.0, True]
lista_vacia = []

print(f"Lista de números: {numeros}, tipo: {type(numeros)}")
print(f"Lista mixta: {mixta}")

# Acceso a elementos
primer_numero = numeros[0]  # 1
ultimo_nombre = nombres[-1]  # Pedro
print(f"Primer número: {primer_numero}")
print(f"Último nombre: {ultimo_nombre}")

# Slicing (muy usado en data science)
subset = numeros[1:4]  # [2, 3, 4]
print(f"Subset de números: {subset}")

# Modificar elementos
numeros[0] = 10
print(f"Lista modificada: {numeros}")

# Métodos de listas importantes para data science
numeros.append(6)      # Añadir elemento al final
print(f"Después de append: {numeros}")

numeros.insert(1, 15)  # Insertar elemento en posición específica
print(f"Después de insert: {numeros}")

numeros.remove(3)      # Eliminar elemento por valor
print(f"Después de remove: {numeros}")

valor_eliminado = numeros.pop()  # Eliminar último elemento y retornarlo
print(f"Valor eliminado: {valor_eliminado}")
print(f"Después de pop: {numeros}")

# Contar y buscar en listas
lista_con_duplicados = [1, 2, 3, 2, 4, 2, 5]
print(f"Lista con duplicados: {lista_con_duplicados}")
conteo = lista_con_duplicados.count(2)  # Cuenta ocurrencias de un valor
posicion = lista_con_duplicados.index(3)  # Encuentra la posición de un valor
print(f"El número 2 aparece {conteo} veces")
print(f"El número 3 está en la posición {posicion}")

# Ordenar listas (importante para análisis)
numeros_desordenados = [5, 2, 8, 1, 9]
numeros_desordenados.sort()  # Ordena la lista in-place
print(f"Lista ordenada: {numeros_desordenados}")
numeros_desordenados.sort(reverse=True)  # Ordena en orden descendente
print(f"Lista ordenada descendente: {numeros_desordenados}")

# Comprensión de listas (muy poderosa y eficiente en Python)
cuadrados = [n**2 for n in range(1, 6)]
print(f"Cuadrados: {cuadrados}")

pares = [n for n in range(1, 11) if n % 2 == 0]
print(f"Números pares: {pares}")

# Listas de listas (matrices, muy comunes en data science)
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Matriz:\n{matriz}")
print(f"Elemento (1,2): {matriz[1][2]}")  # Accede al elemento en fila 1, columna 2 (valor 6)

# ----- Tuplas -----
# Las tuplas son como listas inmutables, excelentes para datos que no deben cambiar

# Creación de tuplas
coordenadas = (10.5, 20.8)
persona = ("Juan", 30, "Ingeniero")
tupla_vacia = ()
tupla_un_elemento = (42,)  # Nota la coma necesaria para tuplas de un elemento

print(f"Coordenadas: {coordenadas}, tipo: {type(coordenadas)}")
print(f"Persona: {persona}")

# Acceso a elementos
x = coordenadas[0]
y = coordenadas[1]
print(f"Coordenada x: {x}, Coordenada y: {y}")

# Desempaquetado de tuplas (muy útil en data science)
nombre, edad, profesion = persona
print(f"Nombre: {nombre}, Edad: {edad}, Profesión: {profesion}")

# Métodos de tuplas
ocurrencias = (1, 2, 2, 3, 2).count(2)
indice = (1, 2, 3, 4).index(3)
print(f"El número 2 aparece {ocurrencias} veces")
print(f"El número 3 está en la posición {indice}")

# Ventajas de tuplas en data science:
# 1. Inmutabilidad (previene modificaciones accidentales)
# 2. Más eficientes en memoria que las listas
# 3. Pueden usarse como claves en diccionarios

# ----- Diccionarios -----
# Fundamentales para trabajar con datos estructurados

# Creación de diccionarios
estudiante = {
    "nombre": "María",
    "edad": 22,
    "carrera": "Ciencia de Datos",
    "promedio": 9.5
}

print(f"Estudiante: {estudiante}, tipo: {type(estudiante)}")

# Acceso a valores
nombre_estudiante = estudiante["nombre"]
print(f"Nombre del estudiante: {nombre_estudiante}")

# Método get (seguro, no genera error si la clave no existe)
# Muy útil cuando trabajamos con datos que pueden tener valores faltantes
telefono = estudiante.get("telefono", "No disponible")
print(f"Teléfono: {telefono}")

# Modificar o añadir elementos
estudiante["edad"] = 23
estudiante["telefono"] = "555-1234"
print(f"Estudiante actualizado: {estudiante}")

# Eliminar elementos
del estudiante["promedio"]
print(f"Después de eliminar promedio: {estudiante}")

# Métodos útiles de diccionarios
claves = estudiante.keys()
valores = estudiante.values()
items = estudiante.items()  # Devuelve pares (clave, valor)

print(f"Claves: {list(claves)}")
print(f"Valores: {list(valores)}")
print(f"Items: {list(items)}")

# Iterar sobre diccionarios (muy común en análisis de datos)
print("\nInformación del estudiante:")
for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")

# Diccionarios anidados (comunes en datos JSON)
universidad = {
    "nombre": "Universidad Tecnológica",
    "carreras": {
        "ciencia_datos": {
            "duracion": 4,
            "estudiantes": 120
        },
        "ingenieria_datos": {
            "duracion": 5,
            "estudiantes": 80
        }
    }
}

print(f"\nEstudiantes en Ingeniería de Datos: {universidad['carreras']['ingenieria_datos']['estudiantes']}")

# Comprensión de diccionarios
cuadrados_dict = {x: x**2 for x in range(1, 6)}
print(f"Diccionario de cuadrados: {cuadrados_dict}")

# ----- Sets (conjuntos) -----
# Útiles para eliminar duplicados y operaciones de conjuntos

# Creación de sets
numeros_unicos = {1, 2, 3, 4, 5}
colores = {"rojo", "verde", "azul"}
numeros_desde_lista = set([1, 2, 2, 3, 3, 3, 4])  # Elimina duplicados

print(f"Números únicos: {numeros_unicos}, tipo: {type(numeros_unicos)}")
print(f"Set creado desde lista: {numeros_desde_lista}")

# Operaciones de conjuntos (muy útiles en data science)
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

union = set1 | set2  # También: set1.union(set2)
interseccion = set1 & set2  # También: set1.intersection(set2)
diferencia = set1 - set2  # También: set1.difference(set2)

print(f"Unión: {union}")
print(f"Intersección: {interseccion}")
print(f"Diferencia: {diferencia}")

# Añadir y eliminar elementos
colores.add("amarillo")
colores.remove("verde")  # genera error si no existe
print(f"Colores actualizados: {colores}")

# Verificar membresía (muy rápido en sets)
print(f"¿'rojo' está en colores?: {'rojo' in colores}")

# Eliminar duplicados de una lista (caso de uso común)
lista_con_duplicados = [1, 2, 2, 3, 3, 3, 4, 5, 5]
lista_sin_duplicados = list(set(lista_con_duplicados))
print(f"Lista original: {lista_con_duplicados}")
print(f"Lista sin duplicados: {lista_sin_duplicados}")

#frozenset (set inmutable)
