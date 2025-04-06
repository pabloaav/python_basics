# Data Science con Python: Análisis básico con Pandas y NumPy
# Este código muestra un flujo de trabajo típico para análisis de datos

# Importación de librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Creación y lectura de datos
# Creamos un DataFrame de ejemplo (normalmente cargarías un CSV)
np.random.seed(42)  # Para reproducibilidad
n = 100

# Simulamos datos de casas: tamaño, habitaciones, edad y precio
tamano = np.random.normal(120, 30, n)  # Tamaño en metros cuadrados
habitaciones = np.random.randint(1, 6, n)
edad = np.random.randint(1, 50, n)  # Edad de la casa en años
# El precio dependerá de estas variables con algo de ruido
precio = 1000 * tamano + 10000 * habitaciones - 2000 * np.sqrt(edad) + np.random.normal(0, 25000, n)

# Creamos el DataFrame
datos = pd.DataFrame({
    'tamano': tamano,
    'habitaciones': habitaciones,
    'edad': edad,
    'precio': precio
})

# 2. Exploración inicial de datos
print("=== Información básica del DataFrame ===")
print(datos.info())
print("\n=== Primeras 5 filas ===")
print(datos.head())
print("\n=== Estadísticas descriptivas ===")
print(datos.describe())

# 3. Visualización básica
plt.figure(figsize=(12, 8))

# Distribución del precio
plt.subplot(2, 2, 1)
datos['precio'].hist(bins=20)
plt.title('Distribución de Precios')
plt.xlabel('Precio')
plt.ylabel('Frecuencia')

# Relación tamaño vs precio
plt.subplot(2, 2, 2)
plt.scatter(datos['tamano'], datos['precio'])
plt.title('Tamaño vs Precio')
plt.xlabel('Tamaño (m²)')
plt.ylabel('Precio')

# Relación habitaciones vs precio
plt.subplot(2, 2, 3)
plt.boxplot([datos[datos['habitaciones'] == i]['precio'] for i in range(1, 6)], 
            labels=range(1, 6))
plt.title('Precio por Número de Habitaciones')
plt.xlabel('Habitaciones')
plt.ylabel('Precio')

# Relación edad vs precio
plt.subplot(2, 2, 4)
plt.scatter(datos['edad'], datos['precio'])
plt.title('Edad vs Precio')
plt.xlabel('Edad (años)')
plt.ylabel('Precio')

plt.tight_layout()
# plt.savefig('analisis_viviendas.png')  # Descomentar para guardar la figura
# plt.show()  # Descomentar para mostrar la figura en entornos interactivos

# 4. Preprocesamiento de datos
# Verificamos si hay valores nulos
print("\n=== Valores nulos por columna ===")
print(datos.isnull().sum())

# 5. Análisis de correlación
print("\n=== Matriz de correlación ===")
print(datos.corr())

# 6. Modelo de regresión lineal simple
# Dividimos los datos en conjuntos de entrenamiento y prueba
X = datos[['tamano', 'habitaciones', 'edad']]
y = datos['precio']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenamos el modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Evaluamos el modelo
y_pred = modelo.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n=== Resultados del modelo ===")
print(f"Coeficientes: {modelo.coef_}")
print(f"Intercepto: {modelo.intercept_}")
print(f"Error cuadrático medio: {mse:.2f}")
print(f"Coeficiente de determinación (R²): {r2:.2f}")

# 7. Predicciones con el modelo
# Hagamos predicciones para algunas casas nuevas
casas_nuevas = pd.DataFrame({
    'tamano': [100, 150, 200],
    'habitaciones': [2, 3, 4],
    'edad': [20, 10, 5]
})

predicciones = modelo.predict(casas_nuevas)

print("\n=== Predicciones para casas nuevas ===")
casas_nuevas['precio_estimado'] = predicciones.round(2)
print(casas_nuevas)

# 8. Función para hacer predicciones interactivas
def predecir_precio(tamano, habitaciones, edad):
    """
    Función para predecir el precio de una casa basado en sus características
    
    Args:
        tamano (float): Tamaño de la casa en metros cuadrados
        habitaciones (int): Número de habitaciones
        edad (int): Edad de la casa en años
        
    Returns:
        float: Precio estimado de la casa
    """
    datos_casa = np.array([[tamano, habitaciones, edad]])
    return modelo.predict(datos_casa)[0]

# Ejemplo de uso de la función
tamano_ejemplo = 135
habitaciones_ejemplo = 3
edad_ejemplo = 15
precio_estimado = predecir_precio(tamano_ejemplo, habitaciones_ejemplo, edad_ejemplo)

print(f"\nPara una casa de {tamano_ejemplo}m², {habitaciones_ejemplo} habitaciones y {edad_ejemplo} años:")
print(f"El precio estimado es: ${precio_estimado:.2f}")

# 9. Guardado del modelo para uso futuro (opcional)
# import joblib
# joblib.dump(modelo, 'modelo_precios_casas.pkl')
# print("\nModelo guardado como 'modelo_precios_casas.pkl'")

print("\n=== Fin del análisis ===")