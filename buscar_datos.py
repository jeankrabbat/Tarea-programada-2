import os
import pickle
from punt_play import Punt_Play

def buscar_datos(key, info_dat_path):
    record_size = 200  # Tamaño del registro
    position = key  # Usar la llave directamente como posición

    print(f"Buscando registro en la posición: {position}")

    with open(info_dat_path, "rb") as info_dat:
        info_dat.seek(position * record_size)
        record = info_dat.read(record_size)

        if record.strip(b'\x00') != b'':
            try:
                punt_play = pickle.loads(record.strip(b'\x00'))
                print(f"Registro encontrado en info.dat: {punt_play.__dict__}")
            except pickle.UnpicklingError as e:
                print(f"Error al deserializar el registro de info.dat: {e}")
        else:
            print("El registro en info.dat está vacío.")

        # Verificar si hay colisiones
        col_file_path = f"{key}-col.dat"
        if os.path.exists(col_file_path):
            print(f"El registro de la posicion {position} tiene colisiones y se encuentran en el archivo {col_file_path}:")
            with open(col_file_path, "rb") as col_file:
                while True:
                    record = col_file.read(record_size)
                    if not record:
                        break
                    try:
                        punt_play = pickle.loads(record.strip(b'\x00'))
                        print(f"Registro leído de {col_file_path}: {punt_play.__dict__}")
                    except pickle.UnpicklingError as e:
                        print(f"Error al deserializar el registro de {col_file_path}: {e}")
        else:
            print("No hay archivo de colisiones.")