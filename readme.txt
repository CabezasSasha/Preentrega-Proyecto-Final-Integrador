Sistema de Gestión de Inventario - git init

Descripción:
Este proyecto es un sistema de gestión de inventario desarrollado en Python. El sistema permite al usuario agregar productos al inventario y visualizar los productos registrados mediante un menú interactivo.

Funciones principales:

Agregar productos: Los usuarios pueden ingresar un nombre y una cantidad para cada producto.
Mostrar inventario: Permite visualizar todos los productos registrados hasta el momento.
Guardado persistente: El sistema almacena los datos de los productos de forma persistente en un archivo de texto (inventario.txt).

Requisitos:

Python 3.x debe estar instalado en tu computadora.
Cómo ejecutar el proyecto:

Asegúrate de que tienes el archivo PFI-preentrega.py descargado.

Abre una terminal (o línea de comandos) y navega al directorio donde se encuentra el archivo PFI-preentrega.py.

Ejecuta el siguiente comando:

python PFI-preentrega.py
Selecciona las opciones del menú para gestionar el inventario:

Opción 1: Agregar un producto.
Opción 2: Mostrar el inventario.
Opción 3: Salir del sistema.
Estructura de archivos del proyecto:

PFI-preentrega.py: Contiene el código del sistema de inventario.
inventario.txt (Opcional): Archivo usado para guardar productos de forma persistente.

Funcionamiento del guardado persistente:
Este sistema utiliza funciones de la librería estándar de Python para guardar y cargar datos de manera persistente. Los productos son almacenados como líneas de texto en un archivo llamado inventario.txt. Cada producto se guarda en el formato nombre,cantidad, y al iniciar el programa, los datos son cargados desde este archivo si existe.

Carga de datos:
Al iniciar, el sistema verifica si el archivo inventario.txt existe. Si existe, los productos se cargan en una lista llamada inventario.

python
if os.path.exists("inventario.txt"):
    with open("inventario.txt", "r") as file:
        for line in file:
            nombre, cantidad = line.strip().split(",")
            inventario.append({"nombre": nombre, "cantidad": int(cantidad)})

Guardado de datos:
Cuando se agrega un nuevo producto, el inventario se guarda automáticamente en el archivo inventario.txt. Esto garantiza que los datos persistan incluso después de que el programa se cierre.

python
with open("inventario.txt", "w") as file:
    for producto in inventario:
        file.write(f"{producto['nombre']},{producto['cantidad']}\n")

Notas adicionales:
Este proyecto es una entrega evaluativa que demuestra el uso de conceptos fundamentales de Python, como bucles, listas, condicionales y manejo de archivos para la gestión de inventarios. Además, muestra cómo persistir datos utilizando el sistema de archivos de manera eficiente.

