# =====================================================================
# MANIPULACIÓN DE ARCHIVOS EN PYTHON
# =====================================================================

# ----- Operaciones básicas de archivo -----

# Escribir en un archivo
def escribir_archivo_texto():
    # Modo 'w' (write) - Crea un nuevo archivo o sobrescribe si existe
    with open("datos.txt", "w") as archivo:
        archivo.write("Línea 1: Introducción a Python\n")
        archivo.write("Línea 2: Manipulación de archivos\n")
        archivo.write("Línea 3: Análisis de datos\n")
    
    print("Archivo creado correctamente.")

# Leer un archivo completo
def leer_archivo_completo():
    try:
        with open("datos.txt", "r") as archivo:
            contenido = archivo.read()
            print("\nContenido completo del archivo:")
            print(contenido)
    except FileNotFoundError:
        print("El archivo no existe.")

# Leer archivo línea por línea (más eficiente para archivos grandes)
def leer_archivo_linea_por_linea():
    try:
        with open("datos.txt", "r") as archivo:
            print("\nLeyendo línea por línea:")
            for i, linea in enumerate(archivo, 1):
                print(f"Línea {i}: {linea.strip()}")
    except FileNotFoundError:
        print("El archivo no existe.")

# Añadir contenido a un archivo existente
def anadir_a_archivo():
    # Modo 'a' (append) - Añade al final del archivo
    with open("datos.txt", "a") as archivo:
        archivo.write("Línea 4: Esta línea fue añadida después\n")
    
    print("\nContenido añadido al archivo.")

# ----- Trabajar con rutas de archivos -----

import os

def trabajar_con_rutas():
    # Directorio actual
    directorio_actual = os.getcwd()
    print(f"\nDirectorio de trabajo actual: {directorio_actual}")
    
    # Listar archivos en el directorio actual
    archivos = os.listdir()
    print(f"Archivos en el directorio: {archivos}")
    
    # Verificar si un archivo existe
    existe = os.path.exists("datos.txt")
    print(f"¿Existe 'datos.txt'?: {existe}")
    
    # Construir rutas de forma segura
    ruta_completa = os.path.join(directorio_actual, "datos.txt")
    print(f"Ruta completa: {ruta_completa}")

# ----- Trabajar con archivos CSV (muy común en data science) -----

import csv

def trabajar_con_csv():
    # Crear un archivo CSV
    with open("empleados.csv", "w", newline="") as archivo:
        escritor = csv.writer(archivo)
        
        # Escribir encabezados
        escritor.writerow(["Nombre", "Departamento", "Salario"])
        
        # Escribir datos
        escritor.writerow(["Ana García", "Data Science", 65000])
        escritor.writerow(["Luis Martínez", "Ingeniería", 70000])
        escritor.writerow(["Elena Pérez", "Analítica", 68000])
    
    print("\nArchivo CSV creado correctamente.")
    
    # Leer un archivo CSV
    print("\nLeyendo archivo CSV:")
    with open("empleados.csv", "r", newline="") as archivo:
        lector = csv.reader(archivo)
        
        # Leer encabezados
        encabezados = next(lector)
        print(f"Encabezados: {encabezados}")
        
        # Leer filas de datos
        for fila in lector:
            nombre, departamento, salario = fila
            print(f"{nombre} trabaja en {departamento} y gana ${salario}")
    
    # Usando DictReader y DictWriter (más práctico)
    with open("estudiantes.csv", "w", newline="") as archivo:
        campos = ["id", "nombre", "carrera", "promedio"]
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        
        # Escribir encabezados
        escritor.writeheader()
        
        # Escribir datos
        escritor.writerow({
            "id": 1,
            "nombre": "Carlos López",
            "carrera": "Ciencia de Datos",
            "promedio": 9.2
        })
        escritor.writerow({
            "id": 2,
            "nombre": "María Sánchez",
            "carrera": "Ingeniería de Datos",
            "promedio": 9.5
        })
    
    print("\nArchivo CSV con DictWriter creado correctamente.")
    
    # Leer con DictReader
    print("\nLeyendo archivo CSV con DictReader:")
    with open("estudiantes.csv", "r", newline="") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            print(f"ID: {fila['id']}, Nombre: {fila['nombre']}, "
                  f"Carrera: {fila['carrera']}, Promedio: {fila['promedio']}")

# ----- Trabajar con archivos JSON (formato muy común en data science) -----

import json

def trabajar_con_json():
    # Datos para guardar en JSON
    datos = {
        "empresa": "DataTech",
        "empleados": [
            {
                "id": 1,
                "nombre": "Ana García",
                "departamento": "Data Science",
                "proyectos": ["Análisis de ventas", "Predicción de demanda"]
            },
            {
                "id": 2,
                "nombre": "Carlos López",
                "departamento": "Ingeniería de Datos",
                "proyectos": ["ETL pipeline", "Data lake"]
            }
        ],
        "ubicacion": {
            "ciudad": "Madrid",
            "pais": "España"
        }
    }
    
    # Escribir JSON a un archivo
    with open("empresa.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
    
    print("\nArchivo JSON creado correctamente.")
    
    # Leer JSON desde un archivo
    with open("empresa.json", "r", encoding="utf-8") as archivo:
        datos_leidos = json.load(archivo)
    
    print("\nDatos leídos del archivo JSON:")
    print(f"Empresa: {datos_leidos['empresa']}")
    print(f"Primer empleado: {datos_leidos['empleados'][0]['nombre']}")
    print(f"Proyectos del segundo empleado: {datos_leidos['empleados'][1]['proyectos']}")
    
    # Convertir string a JSON
    json_str = '{"nombre": "Elena", "edad": 28, "lenguajes": ["Python", "SQL", "R"]}'
    datos_parsed = json.loads(json_str)
    print(f"\nDatos parseados: {datos_parsed}")
    print(f"Lenguajes: {datos_parsed['lenguajes']}")
    
    # Convertir objeto a string JSON
    nuevo_objeto = {
        "id": 123,
        "valores": [1.2, 3.4, 5.6],
        "activo": True
    }
    json_string = json.dumps(nuevo_objeto, indent=2)
    print(f"\nObjeto convertido a string JSON:\n{json_string}")

# ----- Manejo de archivos Excel (formato muy usado en análisis de datos) -----

# Nota: Requiere instalar: pip install openpyxl pandas

def trabajar_con_excel():
    try:
        import pandas as pd
        
        # Crear un DataFrame
        datos = {
            'Nombre': ['Ana', 'Carlos', 'Elena', 'Miguel'],
            'Edad': [28, 34, 29, 42],
            'Departamento': ['Data Science', 'Ingeniería', 'Analítica', 'Desarrollo'],
            'Salario': [65000, 70000, 68000, 72000]
        }
        
        df = pd.DataFrame(datos)
        
        # Guardar DataFrame como Excel
        df.to_excel("empleados.xlsx", sheet_name="Empleados", index=False)
        print("\nArchivo Excel creado correctamente.")
        
        # Leer archivo Excel
        df_leido = pd.read_excel("empleados.xlsx", sheet_name="Empleados")
        print("\nDatos leídos del archivo Excel:")
        print(df_leido)
        
        # Manipular datos y guardar en nueva hoja
        df['Bono'] = df['Salario'] * 0.1
        df['Total'] = df['Salario'] + df['Bono']
        
        with pd.ExcelWriter("empleados_con_bonos.xlsx") as writer:
            df.to_excel(writer, sheet_name="Empleados", index=False)
            
            # Crear una hoja de resumen
            resumen = pd.DataFrame({
                'Concepto': ['Total Salarios', 'Total Bonos', 'Total Pagos'],
                'Valor': [df['Salario'].sum(), df['Bono'].sum(), df['Total'].sum()]
            })
            resumen.to_excel(writer, sheet_name="Resumen", index=False)
        
        print("\nArchivo Excel con múltiples hojas creado correctamente.")
        
    except ImportError:
        print("\nPara trabajar con archivos Excel, instala las librerías necesarias:")
        print("pip install openpyxl pandas")

# ----- Trabajar con archivos de texto grandes (técnicas para data engineering) -----

def procesar_archivo_grande():
    # Crear un archivo grande para demostración
    with open("datos_grandes.txt", "w") as archivo:
        for i in range(1000):
            archivo.write(f"Línea {i}: Este es un ejemplo de línea con datos {i*10}\n")
    
    print("\nArchivo grande creado correctamente.")
    
    # Procesamiento por lotes (chunking)
    print("\nProcesando archivo grande por lotes:")
    
    # Contador para estadísticas
    total_lineas = 0
    suma_valores = 0
    
    # Tamaño del lote
    batch_size = 100
    batch = []
    
    with open("datos_grandes.txt", "r") as archivo:
        for linea in archivo:
            total_lineas += 1
            
            # Extraer el valor numérico de la línea
            partes = linea.split()
            valor = int(partes[-1])
            suma_valores += valor
            
            # Añadir al lote actual
            batch.append(linea)
            
            # Procesar cuando el lote está completo
            if len(batch) >= batch_size:
                print(f"Procesando lote de {len(batch)} líneas...")
                # Aquí se podría hacer algún procesamiento con el lote
                batch = []  # Reiniciar el lote
    
    # Procesar el último lote si existe
    if batch:
        print(f"Procesando último lote de {len(batch)} líneas...")
    
    print(f"\nEstadísticas finales:")
    print(f"Total de líneas procesadas: {total_lineas}")
    print(f"Suma de todos los valores: {suma_valores}")
    print(f"Valor promedio: {suma_valores/total_lineas:.2f}")

# ----- Uso de contextos para manejo seguro de archivos -----

def demostrar_contextos():
    print("\nUso de contextos (with) para manejo seguro de archivos:")
    
    try:
        # Sin usar contexto (no recomendado)
        print("Sin usar contexto (modo incorrecto):")
        archivo = open("temp.txt", "w")
        archivo.write("Este es un ejemplo sin contexto.\n")
        # Si ocurre una excepción aquí, el archivo podría no cerrarse
        archivo.close()
        
        # Usando contexto (recomendado)
        print("Usando contexto (modo correcto):")
        with open("temp.txt", "w") as archivo:
            archivo.write("Este es un ejemplo con contexto.\n")
            # El archivo se cierra automáticamente al salir del bloque with
        
        print("El archivo se cerró automáticamente.")
        
        # Verificar que el archivo está cerrado
        with open("temp.txt", "r") as archivo:
            contenido = archivo.read()
            print(f"Contenido: {contenido.strip()}")
            
    except Exception as e:
        print(f"Error: {e}")

# ----- Ejecución de las funciones -----

if __name__ == "__main__":
    print("Demostraciones de manipulación de archivos en Python:")
    
    # Demostrar operaciones básicas
    escribir_archivo_texto()
    leer_archivo_completo()
    leer_archivo_linea_por_linea()
    anadir_a_archivo()
    leer_archivo_completo()
    
    # Demostrar trabajo con rutas
    trabajar_con_rutas()
    
    # Demostrar trabajo con CSV
    trabajar_con_csv()
    
    # Demostrar trabajo con JSON
    trabajar_con_json()
    
    # Demostrar trabajo con Excel
    trabajar_con_excel()
    
    # Demostrar procesamiento de archivos grandes
    procesar_archivo_grande()
    
    # Demostrar uso de contextos
    demostrar_contextos()