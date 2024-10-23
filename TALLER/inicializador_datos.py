import os
import json

def inicializar_archivo_json():
    Ruta_Datos = os.path.join(os.path.dirname(__file__), 'datos', 'Inventory.json')
    os.makedirs(os.path.dirname(Ruta_Datos), exist_ok=True)

    if not os.path.exists(Ruta_Datos):
        Productos_creados = [
            {
                "Producto": "Arroz",
                "Cantidad": 100,
                "Precio": 2000
            },
            {
                "Producto": "Frijoles",
                "Cantidad": 5,
                "Precio": 2000
            }
        ]
        with open(Ruta_Datos, 'w') as archivo:
            json.dump(Productos_creados, archivo, indent=2)
            print(f"Archivo {Ruta_Datos} creado e inicializado con Productos de ejemplo.")
    else:
        print(f"El Archivo {Ruta_Datos} ya existe.")

if __name__ == "__main__":
    inicializar_archivo_json()

