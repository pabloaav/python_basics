"""
Paquete de Matemáticas
=====================

Un paquete Python que contiene operaciones matemáticas básicas y avanzadas.

Módulos disponibles:
- operaciones_basicas: Operaciones aritméticas fundamentales
- operaciones_avanzadas: Funciones matemáticas complejas y especializadas

Autor: Usuario
Versión: 1.0.0
"""

from .operaciones_basicas import (
    sumar, restar, multiplicar, dividir, potencia, raiz_cuadrada,
    factorial, es_par, es_impar, maximo, minimo
)
from .operaciones_avanzadas import (
    seno, coseno, tangente, logaritmo, logaritmo_natural,
    valor_absoluto, redondear, truncar, promedio, desviacion_estandar
)

__version__ = "1.0.0"
__author__ = "Usuario"
__all__ = [
    # Operaciones básicas
    "sumar", "restar", "multiplicar", "dividir", "potencia", "raiz_cuadrada",
    "factorial", "es_par", "es_impar", "maximo", "minimo",
    
    # Operaciones avanzadas
    "seno", "coseno", "tangente", "logaritmo", "logaritmo_natural",
    "valor_absoluto", "redondear", "truncar", "promedio", "desviacion_estandar"
]
