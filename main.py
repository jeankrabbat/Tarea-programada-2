from crear_info_dat import crear_info_dat
from menu import menu

def main():
    #Crear archivo si no existe
    crear_info_dat()

    #Menu
    menu()

if __name__ == "__main__":
    main()