import os
import json

Ruta_Datos = os.path.join(os.path.dirname(__file__), '..', 'datos', 'Inventory.json')

def Cargar_datos():
    if os.path.exists(Ruta_Datos):
        try:
            with open(Ruta_Datos, 'r') as archivo:
                return json.load(archivo)
        except json.JSONDecodeError:
            print("Error: El archivo JSON está mal formado.")
            return []
        except Exception as e:
            print(f"Error al cargar los datos: {e}")
            return []
    return []


def Guardar_datos(Productos_creados):
    os.makedirs(os.path.dirname(Ruta_Datos), exist_ok=True)
    with open(Ruta_Datos, 'w') as archivo:
        json.dump(Productos_creados, archivo, indent=2)