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


def Actualizar_inv_productos(nombre_producto, nueva_cantidad, nuevo_precio):
    productos = Cargar_datos()
    for producto in productos:
        if producto["Nombre del producto"] == nombre_producto:
            if nueva_cantidad is not None:
                producto["Cantidad de productos"] = int(nueva_cantidad)  # Convertir a int
                print(f"Cantidad de '{nombre_producto}' modificada a {nueva_cantidad}.")

            if nuevo_precio is not None:
                producto["Precio del producto"] = float(nuevo_precio)  # Convertir a float
                print(f"Precio de '{nombre_producto}' modificado a {nuevo_precio}.")

            print(f"Producto '{nombre_producto}' actualizado.")
            Guardar_datos(productos)  # Guardar después de actualizar
            return

    print(f"Producto '{nombre_producto}' no encontrado.")


def Eliminar_inv_producto(nombre_producto):
    productos = Cargar_datos()

    for producto in productos:
        if producto["Nombre del producto"] == nombre_producto:
            productos.remove(producto)
            Guardar_datos(productos)
            print(f"Producto '{nombre_producto}' eliminado.")
            return

    print("Producto no encontrado.")


def Mostar_productos():
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
