import os
from datetime import datetime

ARCHIVO = "inventario.txt"

def leer_inventario():
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as file:
            contenido = file.read()
            print("\n--- INVENTARIO COMPLETO ---")
            print(contenido if contenido else "El inventario está vacío.")
    except FileNotFoundError:
        print("El archivo inventario.txt no existe.")

def escribir_inventario(productos):
    with open(ARCHIVO, "w", encoding="utf-8") as file:
        for p in productos:
            file.write(p + "\n")
    print("Inventario sobrescrito exitosamente.")
    
def agregar_producto(producto):
    with open(ARCHIVO, "a", encoding="utf-8") as file:
        file.write(producto + "\n")
    print("Producto agregado")
    
def modificar_producto(nombre, nuevo_nombre):
    try:
        with open(ARCHIVO, "r+", encoding="utf-8") as file:
            lineas = file.readlines()
            file.seek(0)
            file.truncate()

            encontrado = False
            for linea in lineas:
                datos = linea.strip().split(",")
                if datos[0].strip().lower() == nombre.lower():
                    datos[0] = nuevo_nombre
                    nueva_linea = ", ".join(datos)
                    file.write(nueva_linea + "\n")
                    encontrado = True
                else:
                    file.write(linea)

        if encontrado:
            print(f"Producto '{nombre}' renombrado a '{nuevo_nombre}'.")
        else:
            print("Producto no encontrado.")
    except FileNotFoundError:
        print("El archivo inventario.txt no existe.")

def atributos_archivo():
    try:
        tamaño = os.path.getsize(ARCHIVO)
        mod_time = os.path.getmtime(ARCHIVO)
        fecha = datetime.fromtimestamp(mod_time)

        print("\n--- ATRIBUTOS DEL ARCHIVO ---")
        print(f"Tamaño: {tamaño} bytes")
        print(f"Última modificación: {fecha}")
    except FileNotFoundError:
        print("El archivo inventario.txt no existe.")

def buscar_producto(nombre):
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as file:
            for linea in file:
                datos = linea.strip().split(",")
                if datos[0].strip().lower() == nombre.lower():
                    print("\n--- PRODUCTO ENCONTRADO ---")
                    print(linea)
                    return
        print("Producto no encontrado.")
    except FileNotFoundError:
        print("El archivo inventario.txt no existe.")
        
def eliminar_producto(nombre):
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as file:
            lineas = file.readlines()

        with open(ARCHIVO, "w", encoding="utf-8") as file:
            eliminado = False
            for linea in lineas:
                datos = linea.strip().split(",")
                if datos[0].strip().lower() == nombre.lower():
                    eliminado = True
                    continue
                file.write(linea)

        if eliminado:
            print(f"Producto '{nombre}' eliminado.")
        else:
            print("Producto no encontrado.")
    except FileNotFoundError:
        print("El archivo inventario.txt no existe.")
 
# MENÚ PRINCIPAL
def menu():
    while True:
        print("\n--- MENÚ INVENTARIO ---")
        print("1. Leer inventario")
        print("2. Sobreescribir inventario")
        print("3. Agregar productos (a)")
        print("4. Modificar nombre de producto")
        print("5. Ver atributos del archivo")
        print("6. Buscar producto específico")
        print("7. Eliminar producto")
        print("8. Salir")
        
        option=input( "\n Elige una opción:\n")
        
        match option:
            case "8":
                print("Saliendo del sistema...")
                break
            
            case "1":
                leer_inventario()
                
            case "2":
                print("\nIngrese productos (separe con ',' ):")
                productos = []
                while True:
                    p= input("> ")
                    if p == ',':
                        break
                    productos.append(p)
                escribir_inventario(productos)
                
            case "3":
                producto = input("Ingrese el producto a agregar: ")
                agregar_producto(producto)
                
            case "4":
                nombre = input("Nombre actual del producto: ")
                nuevo = input("Nuevo nombre: ")
                modificar_producto(nombre, nuevo)
                
            case "5":
                atributos_archivo()                
                
            case "6":    
                nombre = input("Producto a buscar: ")
                buscar_producto(nombre)
                
            case "7":    
                nombre = input("Producto a eliminar: ")
                eliminar_producto(nombre)
                
            case _:    
                print("❌ Opción no válida. Intente nuevamente")
                
menu()