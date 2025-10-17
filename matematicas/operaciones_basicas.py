"""
Operaciones Matemáticas Básicas
==============================

Este módulo contiene funciones para realizar operaciones matemáticas fundamentales.
"""

import math


def sumar(a, b):
    """
    Suma dos números.
    
    Args:
        a (float): Primer número
        b (float): Segundo número
        
    Returns:
        float: La suma de a y b
    """
    return a + b


def restar(a, b):
    """
    Resta dos números.
    
    Args:
        a (float): Minuendo
        b (float): Sustraendo
        
    Returns:
        float: La diferencia de a y b
    """
    return a - b


def multiplicar(a, b):
    """
    Multiplica dos números.
    
    Args:
        a (float): Primer factor
        b (float): Segundo factor
        
    Returns:
        float: El producto de a y b
    """
    return a * b


def dividir(a, b):
    """
    Divide dos números.
    
    Args:
        a (float): Dividendo
        b (float): Divisor
        
    Returns:
        float: El cociente de a y b
        
    Raises:
        ValueError: Si el divisor es cero
    """
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b


def potencia(base, exponente):
    """
    Calcula la potencia de un número.
    
    Args:
        base (float): Base
        exponente (float): Exponente
        
    Returns:
        float: base elevado a la exponente
    """
    return base ** exponente


def raiz_cuadrada(numero):
    """
    Calcula la raíz cuadrada de un número.
    
    Args:
        numero (float): Número del cual calcular la raíz cuadrada
        
    Returns:
        float: La raíz cuadrada del número
        
    Raises:
        ValueError: Si el número es negativo
    """
    if numero < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return math.sqrt(numero)


def factorial(n):
    """
    Calcula el factorial de un número.
    
    Args:
        n (int): Número entero no negativo
        
    Returns:
        int: El factorial de n
        
    Raises:
        ValueError: Si n es negativo
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def es_par(numero):
    """
    Verifica si un número es par.
    
    Args:
        numero (int): Número a verificar
        
    Returns:
        bool: True si el número es par, False si es impar
    """
    return numero % 2 == 0


def es_impar(numero):
    """
    Verifica si un número es impar.
    
    Args:
        numero (int): Número a verificar
        
    Returns:
        bool: True si el número es impar, False si es par
    """
    return numero % 2 != 0


def maximo(a, b):
    """
    Encuentra el máximo entre dos números.
    
    Args:
        a (float): Primer número
        b (float): Segundo número
        
    Returns:
        float: El mayor de los dos números
    """
    return a if a > b else b


def minimo(a, b):
    """
    Encuentra el mínimo entre dos números.
    
    Args:
        a (float): Primer número
        b (float): Segundo número
        
    Returns:
        float: El menor de los dos números
    """
    return a if a < b else b
