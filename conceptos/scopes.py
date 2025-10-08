"""
SCOPES EN PYTHON (Explicado)
----------------------------
Este archivo explica el concepto de "scopes" (ámbitos o alcances de variables) en Python
según la documentación oficial: 
https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces

💡 En resumen:
Un *scope* es el contexto donde los nombres (variables, funciones, etc.) existen y se pueden usar.

Python busca los nombres en este orden (regla LEGB):
    L -> Local
    E -> Enclosing
    G -> Global
    B -> Built-in
"""

# ============================================================
# 1️⃣ GLOBAL SCOPE (Ámbito Global)
# ============================================================

# Este es el ámbito más externo, el que pertenece al módulo completo (el archivo .py).
# Las variables definidas fuera de cualquier función o clase son *globales*.
# Son accesibles desde cualquier parte del archivo (aunque no siempre modificables).

x = 10  # Variable global


def mostrar_global():
    print("Desde mostrar_global(), x =", x)  # Accede a la variable global


mostrar_global()
print("Fuera de la función, x sigue siendo =", x)


# ============================================================
# 2️⃣ LOCAL SCOPE (Ámbito Local)
# ============================================================

# Cada vez que se ejecuta una función, Python crea un nuevo *scope local*.
# Las variables definidas dentro de esa función solo existen mientras la función se ejecuta.

def ejemplo_local():
    y = 5  # Variable local (solo existe dentro de esta función)
    print("Dentro de ejemplo_local(), y =", y)


ejemplo_local()
# print(y)  # ❌ Error: 'y' no está definida fuera de la función


# ============================================================
# 3️⃣ USANDO 'global' PARA MODIFICAR UNA VARIABLE GLOBAL
# ============================================================

# Si queremos cambiar el valor de una variable global desde dentro de una función,
# debemos usar la palabra clave 'global' para indicarle a Python que no cree una nueva variable local.

contador = 0  # variable global


def incrementar():
    global contador  # indica que queremos usar la variable global 'contador'
    contador += 1
    print("Contador dentro de la función:", contador)


incrementar()
incrementar()
print("Contador fuera de la función:", contador)


# ============================================================
# 4️⃣ ENCLOSING SCOPE (Ámbito Envolvente)
# ============================================================

# Este ámbito aparece cuando hay funciones anidadas (una dentro de otra).
# La función interna puede acceder a variables definidas en la función externa.
# Estas variables están en el *enclosing scope* (ámbito envolvente).

def exterior():
    mensaje = "Hola desde exterior()"  # variable en el scope "enclosing"

    def interior():
        # Puede leer la variable 'mensaje' del scope externo
        print("Dentro de interior():", mensaje)

    interior()


exterior()


# ============================================================
# 5️⃣ USANDO 'nonlocal' PARA MODIFICAR VARIABLES DEL ENCLOSING SCOPE
# ============================================================

# La palabra clave 'nonlocal' permite modificar una variable definida en el
# scope de una función externa (pero no global).

def funcion_externa():
    texto = "Mensaje original"

    def funcion_interna():
        nonlocal texto  # indica que usamos la variable del scope envolvente
        texto = "Mensaje modificado por funcion_interna()"

    funcion_interna()
    print("Después de funcion_interna(), texto =", texto)


funcion_externa()


# ============================================================
# 6️⃣ BUILT-IN SCOPE (Ámbito Incorporado)
# ============================================================

# Es el ámbito más amplio: contiene todos los nombres predefinidos de Python,
# como 'len', 'range', 'print', 'sum', etc.
# Siempre están disponibles sin necesidad de importarlos.

print("Ejemplo de función built-in: len('Python') =", len("Python"))


# ============================================================
# 7️⃣ ORDEN DE BÚSQUEDA DE NOMBRES (LEGB)
# ============================================================
"""
Cuando Python necesita encontrar una variable, sigue este orden:
L -> Local: variables dentro de la función actual
E -> Enclosing: variables en funciones envolventes
G -> Global: variables definidas a nivel de módulo
B -> Built-in: nombres del propio Python
"""

nombre = "Global"


def externa():
    nombre = "Enclosing"

    def interna():
        nombre = "Local"
        print("Dentro de interna():", nombre)  # Usa la variable local

    interna()
    # Usa la variable del scope 'enclosing'
    print("Dentro de externa():", nombre)


externa()
print("En el scope global:", nombre)


# ============================================================
# 8️⃣ CLOSURES (Funciones que recuerdan su enclosing scope)
# ============================================================

# Una función puede "recordar" el scope donde fue creada, incluso si ese scope ya no existe.
# Esto se llama "closure".

def crear_multiplicador(factor):
    """
    Devuelve una función que multiplica por 'factor'.
    La variable 'factor' pertenece al scope "enclosing".
    """
    def multiplicar(x):
        return x * factor  # Usa la variable del scope envolvente
    return multiplicar


doble = crear_multiplicador(2)
triple = crear_multiplicador(3)

print("5 * 2 =", doble(5))
print("5 * 3 =", triple(5))
