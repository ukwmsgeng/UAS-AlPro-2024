import csv
import os

# Quick fix
Path = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(Path, 'Data.csv')
professor_path = os.path.join(Path, 'Professor.csv')

# Load Data + Temp Data
local_data = []
with open(data_path, mode='r') as file:
    reader = csv.reader(file)
    local_data = [row for row in reader]

local_professor = []
with open(professor_path, mode='r') as file:
    reader = csv.reader(file)
    local_professor = [row for row in reader]

temporary_list = []

# Cek nama dosen    
def checking_list(name):
    if name in [row[0] for row in local_professor]:
        return name
    else:
        print("Error, nama dosen tidak ditemukan")
        return None

# Start disini
name = input("Nama dosen: ")
key_name = checking_list(name)

if key_name:
    for row_index in range(len(local_data)):
        if local_data[row_index][3] == key_name:
            temporary_list.append(local_data[row_index])

    if temporary_list:
        print(f"Berikut adalah daftar judul untuk dosen {key_name}:")
        print(temporary_list)
    else:
        print(f"Tidak ada data untuk dosen {key_name}")
