import json
from .utils import Cargar_datos, Guardar_datos


def Agregar_producto(nombre, cantidad, precio):
    productos = Cargar_datos()
    nuevo_producto = {
        "Nombre del producto": nombre,
        "Cantidad de productos": int(cantidad),
        "Precio del producto": float(precio)
    }
    productos.append(nuevo_producto)
    Guardar_datos(productos)
    print(f"Producto registrado: '{nombre}' con cantidad {cantidad} y precio {precio}.")


def Actualizar_inv_productos(nombre, nueva_cantidad, nuevo_precio):
    productos = Cargar_datos()
    producto_encontrado = next((p for p in productos if p["Nombre del producto"] == nombre), None)

    if producto_encontrado is None:
        print("El producto no existe en el inventario.")
        return

    try:
        if nueva_cantidad is not None:
            producto_encontrado["Cantidad de productos"] = int(nueva_cantidad)

        if nuevo_precio is not None:
            producto_encontrado["Precio del producto"] = float(nuevo_precio)

        Guardar_datos(productos)
        print(f"Producto {nombre} actualizado con éxito.")
    except ValueError:
        print("Error: La cantidad y el precio deben ser números válidos.")

def Eliminar_inv_producto(nombre_producto):
    productos = Cargar_datos()
    producto_encontrado = next((p for p in productos if p["Nombre del producto"] == nombre_producto), None)

    if producto_encontrado is None:
        print("El producto no existe en el inventario.")
        return

    productos.remove(producto_encontrado)
    Guardar_datos(productos)
    print(f"Producto {nombre_producto} eliminado con éxito.")


def Mostrar_productos():
    productos = Cargar_datos()

    if not productos:
        print("Inventario vacío.")
        return

    print("Inventario de productos:")
    for producto in productos:
        nombre = producto.get("Nombre del producto")
        cantidad = producto.get("Cantidad de productos")
        precio = producto.get("Precio del producto")
        print(f"Nombre: {nombre}, Cantidad: {cantidad}, Precio: {precio}")
