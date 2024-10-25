from Inventory import Agregar_producto, Actualizar_inv_productos, Eliminar_inv_producto, Mostrar_productos
from inicializador_datos import inicializar_archivo_json

def menu():
    print("*** Menu del inventario ***")
    print("1. Agregar producto")
    print("2. Actualizar productos")
    print("3. Eliminar productos")
    print("4. Mostrar productos")
    print("5. Salir")
    return input("Seleccione una opción: ")

def main():
    inicializar_archivo_json()

    while True:
        opcion = menu()
        if opcion == '1':
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = input("Ingrese la cantidad del producto: ")
            precio = input("Ingrese el valor del producto: ")
            Agregar_producto(nombre, cantidad, precio)
        elif opcion == '2':
            nombre_producto = input("Ingrese el nombre del producto a modificar: ")
            nueva_cantidad = input("Ingrese la nueva cantidad: ")
            nuevo_precio = input("Ingrese el nuevo precio: ")
            Actualizar_inv_productos(nombre_producto, nueva_cantidad, nuevo_precio)  # Pasar argumentos
        elif opcion == '3':
            nombre_producto = input("Ingrese el nombre del producto a eliminar: ")
            Eliminar_inv_producto(nombre_producto)
        elif opcion == '4':
            Mostrar_productos()
        elif opcion == '5':
            print("¡Gracias por usar el inventario!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
