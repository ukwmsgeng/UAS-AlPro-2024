import csv
import os

<<<<<<< Updated upstream
# Fungsi Login Dosen
def LoginDosen(Dosen_List):
    print("\n=== Login Dosen ===")
    Nama_Dosen = input("Masukkan Nama Dosen: ")
    
    for dosen in Dosen_List:
        if dosen[0] == Nama_Dosen:
            print(f"Selamat datang, {Nama_Dosen}!")
            return True, Nama_Dosen
    
    print("Nama dosen tidak terdaftar.")
    return False, None

# Fungsi Menampilkan Pengajuan dengan Sortiran Judul
def ViewSubmissions(Data_List):
    print("\nDaftar Pengajuan Judul Tugas Akhir:")
    if not Data_List:
        print("Belum ada pengajuan.")
        return
    # Mengurutkan Data Berdasarkan Judul
    sorted_data = sorted(Data_List, key=lambda x: x[2])
    for idx, row in enumerate(sorted_data):
        print(f"{idx+1}. Nama: {row[1]}, NIM: {row[0]}, Judul: {row[2]}, Status: {row[6]}")

# Fungsi Menyetujui atau Menolak Pengajuan
def ApproveSubmission(Data_List, Data_File):
    if not Data_List:
        print("Belum ada pengajuan untuk diproses.")
        return
    ViewSubmissions(Data_List)
    try:
        choice = int(input("\nMasukkan nomor pengajuan yang ingin Anda proses: "))
        # Mengurutkan Data Berdasarkan Judul (sama seperti tampilan)
        sorted_data = sorted(Data_List, key=lambda x: x[2])
        index = choice - 1
        if 0 <= index < len(sorted_data):
            submission = sorted_data[index]
            print(f"\nPengajuan oleh {submission[1]} (NIM: {submission[0]}) dengan judul '{submission[2]}'.")
            decision = input("Apakah Anda ingin menyetujui pengajuan ini? (y/n): ").lower()
            if decision == 'y':
                submission[6] = "Disetujui"
                print("Pengajuan telah disetujui.")
            elif decision == 'n':
                submission[6] = "Ditolak"
                print("Pengajuan telah ditolak.")
            else:
                print("Input tidak valid.")
                return
            # Update Data_List
            # Cari indeks asli dari submission di Data_List
            for i in range(len(Data_List)):
                if Data_List[i][0] == submission[0] and Data_List[i][2] == submission[2]:
                    Data_List[i][6] = submission[6]
                    break
            # Tulis ulang data ke file CSV
            with open(Data_File, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['NIM', 'Nama', 'Judul', 'Deskripsi', 'Dosen_Pembimbing', 'Link', 'Status'])
                writer.writerows(Data_List)
        else:
            print("Pengajuan tidak ditemukan.")
    except ValueError:
        print("Input harus berupa angka.")

# Inisialisasi Path
Path = os.path.dirname(os.path.abspath(__file__))
Data_File = os.path.join(Path, 'Data.csv')
Dosen_List_File = os.path.join(Path, 'Dosen_List.csv')

# Baca Data Pengajuan
Data_List = []
if os.path.exists(Data_File):
    with open(Data_File, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header
        Data_List = [row for row in reader]

# Baca Daftar Dosen
Dosen_List = []
if os.path.exists(Dosen_List_File):
    with open(Dosen_List_File, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header jika ada
        Dosen_List = [row for row in reader]
else:
    # Jika file tidak ada, buat file baru dengan header
    with open(Dosen_List_File, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nama_Dosen'])

# Mulai Program
Key, Nama_Dosen = LoginDosen(Dosen_List)
if Key:
    while True:
        print("\nPilih opsi:")
        print("1. Lihat Daftar Pengajuan")
        print("2. Proses Pengajuan")
        print("3. Keluar")
        pilihan = input("Masukkan pilihan (1/2/3): ")
        if pilihan == '1':
            ViewSubmissions(Data_List)
        elif pilihan == '2':
            ApproveSubmission(Data_List, Data_File)
        elif pilihan == '3':
            print("Terima kasih, sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih antara 1, 2, atau 3.")
else:
    print("Login gagal.")
=======
# Error Fix
Path = os.path.dirname(os.path.abspath(__file__))
Data = os.path.join(Path, 'Data.csv')

#Baca Data
Local_Data = []
with open(Data, mode='r') as file:
    reader = csv.reader(file)
    Local_Data = [row for row in reader]
    
print(Local_Data)
>>>>>>> Stashed changes
