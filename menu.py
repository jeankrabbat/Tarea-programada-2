from cargar_datos import cargar_datos
from buscar_datos import buscar_datos

def mostrar_menu():
    print("Menú: ")
    print("1. Cargar datos")
    print("2. Buscar datos")
    print("3. Salir")

def seleccionar_opcion():
    opcion = input("Por favor, seleccione una opción (1-3): ")
    return opcion

def manejo_opcion(opcion):
    if opcion == "1":
        print("Eligiste cargar datos.")
        cargar_datos(r'C:\data\segundaprogramada\segunda_parte-bubble_sort-resultado_pbp_2009.csv', 'info.dat')
        return True
    elif opcion == "2":
        print("Eligiste buscar datos.")
        key = int(input("Ingrese la llave (0-749): "))
        buscar_datos(key, 'info.dat')
        return True
    elif opcion == "3":
        print("Saliendo del programa...")
        return False
    else:
        print("Opción no válida, por favor intente de nuevo.")
        return True

def menu():
    continuar_programa = True
    while continuar_programa:
        mostrar_menu()
        opcion = seleccionar_opcion()
        continuar_programa = manejo_opcion(opcion)