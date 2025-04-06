# =====================================================================
# TIPOS DE DATOS BÁSICOS EN PYTHON
# =====================================================================

# ----- Números -----

# Enteros (int)
edad = 30
cantidad_registros = 1000
print(f"Edad: {edad}, tipo: {type(edad)}")
print(f"Cantidad de registros: {cantidad_registros}, tipo: {type(cantidad_registros)}")

# Números de punto flotante (float)
altura = 1.75
precio = 19.99
print(f"Altura: {altura}, tipo: {type(altura)}")
print(f"Precio: {precio}, tipo: {type(precio)}")

# Operaciones básicas con números
suma = 10 + 5
resta = 10 - 5
multiplicacion = 10 * 5
division = 10 / 5  # Devuelve un float
division_entera = 10 // 3  # Devuelve un entero
modulo = 10 % 3  # Devuelve el resto
potencia = 10 ** 2  # 10 elevado a la 2

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print(f"División entera: {division_entera}")
print(f"Módulo: {modulo}")
print(f"Potencia: {potencia}")

# ----- Cadenas de texto (strings) -----

# Definición de strings
nombre = "María"
apellido = 'López'
texto_largo = """Este es un texto
que ocupa varias líneas
en Python"""

print(f"Nombre: {nombre}, tipo: {type(nombre)}")
print(f"Texto largo:\n{texto_largo}")

# Concatenación de strings
nombre_completo = nombre + " " + apellido
print(f"Nombre completo: {nombre_completo}")

# Métodos de strings útiles en data science
texto = "  Análisis de Datos con Python  "
print(f"Texto original: '{texto}'")
print(f"Texto en minúsculas: '{texto.lower()}'")
print(f"Texto en mayúsculas: '{texto.upper()}'")
print(f"Texto sin espacios al inicio y final: '{texto.strip()}'")
print(f"Texto reemplazando 'Python' por 'R': '{texto.replace('Python', 'R')}'")

# Formateo de strings (importante para reportes)
precision = 0.9876543
print(f"La precisión del modelo es: {precision:.2f}")  # Dos decimales
print(f"La precisión del modelo es: {precision:.2%}")  # Como porcentaje

# Indexación y slicing (muy útil en data)
texto = "Python"
print(f"Primera letra: {texto[0]}")
print(f"Última letra: {texto[-1]}")
print(f"Primeras tres letras: {texto[0:3]}")

# ----- Booleanos (bool) -----

# Valores booleanos
verdadero = True
falso = False
print(f"Variable verdadera: {verdadero}, tipo: {type(verdadero)}")
print(f"Variable falsa: {falso}, tipo: {type(falso)}")

# Operaciones lógicas
and_result = True and False  # False
or_result = True or False    # True
not_result = not True        # False

print(f"True and False: {and_result}")
print(f"True or False: {or_result}")
print(f"not True: {not_result}")

# Comparaciones que devuelven booleanos
es_mayor = 10 > 5
es_igual = 10 == 10
es_distinto = 10 != 5

print(f"10 > 5: {es_mayor}")
print(f"10 == 10: {es_igual}")
print(f"10 != 5: {es_distinto}")

# ----- None (tipo nulo) -----

# Uso de None (importante para representar valores nulos en datos)
valor_nulo = None
print(f"Valor nulo: {valor_nulo}, tipo: {type(valor_nulo)}")

# Verificar si un valor es None
es_nulo = valor_nulo is None
print(f"¿Es nulo?: {es_nulo}")