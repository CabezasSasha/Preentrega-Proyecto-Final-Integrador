import os
import json

# Archivo donde se guardará el inventario
archivo_inventario = "inventario.txt"

# Lista para almacenar los productos
inventario = []

def cargar_inventario():
    """Función para cargar el inventario desde un archivo"""
    if os.path.exists(archivo_inventario):
        with open(archivo_inventario, 'r') as file:
            global inventario
            inventario = json.load(file)
            print("Inventario cargado correctamente.\n")
    else:
        print("No se encontró un archivo de inventario previo. Se creará uno nuevo.\n")

def guardar_inventario():
    """Función para guardar el inventario en un archivo"""
    with open(archivo_inventario, 'w') as file:
        json.dump(inventario, file)
    print("Inventario guardado correctamente.\n")

def agregar_producto():
    """Función para agregar un producto al inventario"""
    nombre_producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    # Agregar el producto como un diccionario a la lista
    inventario.append({"nombre": nombre_producto, "cantidad": cantidad})
    print(f"Producto '{nombre_producto}' agregado con éxito.\n")
    guardar_inventario()

def mostrar_inventario():
    """Función para mostrar todos los productos en el inventario"""
    if inventario:
        print("\nInventario de productos:")
        for producto in inventario:
            print(f"Producto: {producto['nombre']}, Cantidad: {producto['cantidad']}")
    else:
        print("El inventario está vacío.\n")

def menu():
    """Función que muestra el menú y maneja la selección del usuario"""
    cargar_inventario()
    while True:
        print("\nMenu de Gestión de Inventario")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1, 2, 3): ")
        
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            mostrar_inventario()
        elif opcion == '3':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Por favor, ingrese 1, 2 o 3.")

# Ejecutar el menú
menu()
