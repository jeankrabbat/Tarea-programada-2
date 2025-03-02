import csv
import os
import pickle
from funcion_hash import funcion_hash
from punt_play import Punt_Play

def cargar_datos(file_path, info_dat_path):
    record_size = 200  # Tamaño del registro

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            punt_play = Punt_Play(row['Game ID'], row['Teams'], row['Total Yards'], row['Quarter'])
            hash_value = funcion_hash(row['Date'], row['Quarter'], row['Teams'].split('@')[0])
            posicion = hash_value * record_size

    

            with open(info_dat_path, "r+b") as info_dat:
                info_dat.seek(posicion)
                record = info_dat.read(record_size)

                if record.strip(b'\x00') == b'':
                    info_dat.seek(posicion)
                    serialized_data = pickle.dumps(punt_play)
                    if len(serialized_data) <= record_size:
                        info_dat.write(serialized_data.ljust(record_size, b'\x00'))
                    else:
                        print(f"Error: El tamaño del registro serializado excede los {record_size} bytes.")
                else:
                    col_file_path = f"{hash_value}-col.dat"
                    with open(col_file_path, "ab") as col_file:
                        serialized_data = pickle.dumps(punt_play)
                        col_file.write(serialized_data.ljust(record_size, b'\x00'))