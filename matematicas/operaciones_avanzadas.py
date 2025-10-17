"""
Operaciones Matemáticas Avanzadas
=================================

Este módulo contiene funciones para realizar operaciones matemáticas complejas
y especializadas, incluyendo trigonométricas, logarítmicas y estadísticas.
"""

import math
import statistics


def seno(angulo_radianes):
    """
    Calcula el seno de un ángulo en radianes.
    
    Args:
        angulo_radianes (float): Ángulo en radianes
        
    Returns:
        float: El seno del ángulo
    """
    return math.sin(angulo_radianes)


def coseno(angulo_radianes):
    """
    Calcula el coseno de un ángulo en radianes.
    
    Args:
        angulo_radianes (float): Ángulo en radianes
        
    Returns:
        float: El coseno del ángulo
    """
    return math.cos(angulo_radianes)


def tangente(angulo_radianes):
    """
    Calcula la tangente de un ángulo en radianes.
    
    Args:
        angulo_radianes (float): Ángulo en radianes
        
    Returns:
        float: La tangente del ángulo
    """
    return math.tan(angulo_radianes)


def logaritmo(numero, base=10):
    """
    Calcula el logaritmo de un número en una base dada.
    
    Args:
        numero (float): Número del cual calcular el logaritmo
        base (float, optional): Base del logaritmo. Por defecto 10.
        
    Returns:
        float: El logaritmo del número en la base especificada
        
    Raises:
        ValueError: Si el número es menor o igual a 0 o la base es menor o igual a 1
    """
    if numero <= 0:
        raise ValueError("El logaritmo no está definido para números menores o iguales a 0")
    if base <= 1:
        raise ValueError("La base del logaritmo debe ser mayor que 1")
    
    return math.log(numero, base)


def logaritmo_natural(numero):
    """
    Calcula el logaritmo natural (base e) de un número.
    
    Args:
        numero (float): Número del cual calcular el logaritmo natural
        
    Returns:
        float: El logaritmo natural del número
        
    Raises:
        ValueError: Si el número es menor o igual a 0
    """
    if numero <= 0:
        raise ValueError("El logaritmo natural no está definido para números menores o iguales a 0")
    
    return math.log(numero)


def valor_absoluto(numero):
    """
    Calcula el valor absoluto de un número.
    
    Args:
        numero (float): Número del cual calcular el valor absoluto
        
    Returns:
        float: El valor absoluto del número
    """
    return abs(numero)


def redondear(numero, decimales=0):
    """
    Redondea un número a un número específico de decimales.
    
    Args:
        numero (float): Número a redondear
        decimales (int, optional): Número de decimales. Por defecto 0.
        
    Returns:
        float: El número redondeado
    """
    return round(numero, decimales)


def truncar(numero):
    """
    Trunca un número eliminando la parte decimal.
    
    Args:
        numero (float): Número a truncar
        
    Returns:
        int: El número truncado
    """
    return math.trunc(numero)


def promedio(numeros):
    """
    Calcula el promedio (media aritmética) de una lista de números.
    
    Args:
        numeros (list): Lista de números
        
    Returns:
        float: El promedio de los números
        
    Raises:
        ValueError: Si la lista está vacía
    """
    if not numeros:
        raise ValueError("No se puede calcular el promedio de una lista vacía")
    
    return statistics.mean(numeros)


def desviacion_estandar(numeros):
    """
    Calcula la desviación estándar de una lista de números.
    
    Args:
        numeros (list): Lista de números
        
    Returns:
        float: La desviación estándar de los números
        
    Raises:
        ValueError: Si la lista tiene menos de 2 elementos
    """
    if len(numeros) < 2:
        raise ValueError("Se necesitan al menos 2 números para calcular la desviación estándar")
    
    return statistics.stdev(numeros)


def grados_a_radianes(grados):
    """
    Convierte grados a radianes.
    
    Args:
        grados (float): Ángulo en grados
        
    Returns:
        float: Ángulo en radianes
    """
    return math.radians(grados)


def radianes_a_grados(radianes):
    """
    Convierte radianes a grados.
    
    Args:
        radianes (float): Ángulo en radianes
        
    Returns:
        float: Ángulo en grados
    """
    return math.degrees(radianes)
