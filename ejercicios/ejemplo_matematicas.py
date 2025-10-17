"""
Ejemplo de uso del paquete de Matemáticas
========================================

Este archivo demuestra cómo usar las funciones del paquete matemáticas.
"""

import sys
import os
# Agregar el directorio padre al path de Python para poder importar matematicas
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importar el paquete completo
import matematicas.operaciones_basicas as op_bs
import matematicas.operaciones_avanzadas as op_av

# También se puede importar módulos específicos
# from matematicas.operaciones_basicas import sumar, multiplicar, factorial
# from matematicas.operaciones_avanzadas import seno, coseno, promedio

def main():
    print("=== EJEMPLO DE USO DEL PAQUETE MATEMÁTICAS ===\n")
    
    # Ejemplos de operaciones básicas
    print("--- OPERACIONES BÁSICAS ---")
    print(f"Suma: 5 + 3 = {op_bs.sumar(5, 3)}")
    print(f"Resta: 10 - 4 = {op_bs.restar(10, 4)}")
    print(f"Multiplicación: 6 * 7 = {op_bs.multiplicar(6, 7)}")
    print(f"División: 15 / 3 = {op_bs.dividir(15, 3)}")
    print(f"Potencia: 2^8 = {op_bs.potencia(2, 8)}")
    print(f"Raíz cuadrada de 64: {op_bs.raiz_cuadrada(64)}")
    print(f"Factorial de 5: {op_bs.factorial(5)}")
    print(f"¿Es 7 par? {op_bs.es_par(7)}")
    print(f"¿Es 8 impar? {op_bs.es_impar(8)}")
    print(f"Máximo entre 12 y 8: {op_bs.maximo(12, 8)}")
    print(f"Mínimo entre 12 y 8: {op_bs.minimo(12, 8)}")
    
    print("\n--- OPERACIONES AVANZADAS ---")
    # Convertir grados a radianes para las funciones trigonométricas
    angulo_grados = 45
    angulo_radianes = op_av.grados_a_radianes(angulo_grados)
    
    print(f"Seno de {angulo_grados}°: {op_av.seno(angulo_radianes):.4f}")
    print(f"Coseno de {angulo_grados}°: {op_av.coseno(angulo_radianes):.4f}")
    print(f"Tangente de {angulo_grados}°: {op_av.tangente(angulo_radianes):.4f}")
    
    print(f"Logaritmo base 10 de 100: {op_av.logaritmo(100, 10)}")
    print(f"Logaritmo natural de e: {op_av.logaritmo_natural(math.e):.4f}")
    print(f"Valor absoluto de -15: {op_av.valor_absoluto(-15)}")
    print(f"Redondear 3.14159 a 2 decimales: {op_av.redondear(3.14159, 2)}")
    print(f"Truncar 7.89: {op_av.truncar(7.89)}")
    
    # Ejemplo con listas de números
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Promedio de {numeros}: {op_av.promedio(numeros)}")
    print(f"Desviación estándar de {numeros}: {op_av.desviacion_estandar(numeros):.4f}")
    
    print("\n--- USANDO IMPORTACIONES ESPECÍFICAS ---")
    print(f"Suma usando importación específica: {op_bs.sumar(20, 30)}")
    print(f"Multiplicación usando importación específica: {op_bs.multiplicar(4, 5)}")
    print(f"Factorial usando importación específica: {op_bs.factorial(6)}")
    print(f"Seno usando importación específica: {op_av.seno(angulo_radianes):.4f}")
    print(f"Promedio usando importación específica: {op_av.promedio([1, 2, 3, 4, 5])}")

if __name__ == "__main__":
    import math  # Para usar math.e en el ejemplo
    main()
