import os

def crear_info_dat():
    nombre_archivo = "info.dat"
    num_registros = 750
    record_size = 200  

    if not os.path.exists(nombre_archivo):
        with open(nombre_archivo, "wb") as file:
            for _ in range(num_registros):
                file.write(b'\x00' * record_size)
        print(f"El archivo {nombre_archivo} ha sido creado con {num_registros} registros vacíos.")
    else:
        print(f"El archivo {nombre_archivo} ya existe!")