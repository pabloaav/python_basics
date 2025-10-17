# Paquete de Matemáticas

Un paquete Python que contiene operaciones matemáticas básicas y avanzadas.

## Estructura del Paquete

```
matematicas/
├── __init__.py
├── README.md
├── operaciones_basicas/
│   ├── __init__.py
│   └── operaciones.py
└── operaciones_avanzadas/
    ├── __init__.py
    └── operaciones.py
```

## Instalación

No requiere instalación especial. Simplemente asegúrate de que el paquete esté en tu ruta de Python.

## Uso

### Importación completa del paquete

```python
import matematicas

# Usar las funciones
resultado = matematicas.sumar(5, 3)
```

### Importación de módulos específicos

```python
from matematicas.operaciones_basicas import sumar, multiplicar
from matematicas.operaciones_avanzadas import seno, coseno

# Usar las funciones directamente
resultado = sumar(5, 3)
```

### Importación de funciones específicas

```python
from matematicas import sumar, seno, promedio

# Usar las funciones directamente
resultado = sumar(5, 3)
```

## Módulos

### operaciones_basicas

Contiene operaciones matemáticas fundamentales:

- `sumar(a, b)`: Suma dos números
- `restar(a, b)`: Resta dos números
- `multiplicar(a, b)`: Multiplica dos números
- `dividir(a, b)`: Divide dos números
- `potencia(base, exponente)`: Calcula la potencia
- `raiz_cuadrada(numero)`: Calcula la raíz cuadrada
- `factorial(n)`: Calcula el factorial
- `es_par(numero)`: Verifica si un número es par
- `es_impar(numero)`: Verifica si un número es impar
- `maximo(a, b)`: Encuentra el máximo entre dos números
- `minimo(a, b)`: Encuentra el mínimo entre dos números

### operaciones_avanzadas

Contiene operaciones matemáticas complejas:

- `seno(angulo_radianes)`: Calcula el seno
- `coseno(angulo_radianes)`: Calcula el coseno
- `tangente(angulo_radianes)`: Calcula la tangente
- `logaritmo(numero, base)`: Calcula el logaritmo
- `logaritmo_natural(numero)`: Calcula el logaritmo natural
- `valor_absoluto(numero)`: Calcula el valor absoluto
- `redondear(numero, decimales)`: Redondea un número
- `truncar(numero)`: Trunca un número
- `promedio(numeros)`: Calcula el promedio de una lista
- `desviacion_estandar(numeros)`: Calcula la desviación estándar
- `grados_a_radianes(grados)`: Convierte grados a radianes
- `radianes_a_grados(radianes)`: Convierte radianes a grados

## Ejemplos

Ver el archivo `ejemplo_matematicas.py` para ejemplos completos de uso.

## Versión

1.0.0

## Autor

Usuario
