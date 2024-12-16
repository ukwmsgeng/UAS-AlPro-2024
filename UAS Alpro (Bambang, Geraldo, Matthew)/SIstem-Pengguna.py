import csv
import os

<<<<<<< Updated upstream
# Fungsi untuk Registrasi Mahasiswa Baru
def Register():
    print("\n=== Registrasi Mahasiswa Baru ===")
    NIM = input("Masukkan NIM: ")
    Nama = input("Masukkan Nama: ")
    No_HP = input("Masukkan Nomor HP: ")
    Email = input("Masukkan Email: ")
    
    # Validasi input sederhana
    if NIM and Nama and No_HP and Email:
        New_Student = [NIM, Nama, No_HP, Email]
        return New_Student
    else:
        print("Semua field harus diisi. Registrasi gagal.")
        return None

# Fungsi Login
def Login(Local_List):
    print("\n=== Login Mahasiswa ===")
    NIM = input("Masukkan NIM: ")
    Nama = input("Masukkan Nama: ")
    
    for user in Local_List:
        if user[0] == NIM and user[1] == Nama:
            print(f"Selamat datang, {Nama}!")
            return True, NIM, Nama
        
    print("NIM atau Nama salah, silakan coba lagi.")
    return False, None, None

# Fungsi Mengajukan Judul
def Apply(NIM, Nama, Dosen_List, Dosen_List_File):
    print("\n=== Pengajuan Judul Tugas Akhir ===")
    Title = input("Judul TA: ")
    Description = input("Deskripsi Tugas Akhir: ")
    Dosen_Pembimbing = input("Masukkan nama dosen pembimbing: ")
    
    # Periksa apakah dosen sudah ada di daftar
    if not any(dosen[0] == Dosen_Pembimbing for dosen in Dosen_List):
        # Jika belum, tambahkan ke daftar dosen
        Dosen_List.append([Dosen_Pembimbing])
        with open(Dosen_List_File, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Nama_Dosen'])
            writer.writerows(Dosen_List)
        print(f"Dosen {Dosen_Pembimbing} berhasil ditambahkan ke daftar dosen.")

    Link = input("Link Tugas: ")
    Status = "Pending"
    Submission = [NIM, Nama, Title, Description, Dosen_Pembimbing, Link, Status]
    
    if Title and Description and Link:
        return Submission
    else:
        print("Semua field harus diisi. Pengajuan gagal.")
        return None

# Fungsi Cek Pengajuan
def CheckSubmission(NIM, Data_List):
    submissions = [row for row in Data_List if row[0] == NIM]
    if submissions:
        print("\nPengajuan Anda:")
        for sub in submissions:
            print(f"Judul: {sub[2]}")
            print(f"Deskripsi: {sub[3]}")
            print(f"Dosen Pembimbing: {sub[4]}")
            print(f"Link: {sub[5]}")
            print(f"Status: {sub[6]}\n")
    else:
        print("Anda belum mengajukan apapun.")

# Inisialisasi Path
Path = os.path.dirname(os.path.abspath(__file__))
List_File = os.path.join(Path, 'List.csv')
Data_File = os.path.join(Path, 'Data.csv')
Dosen_List_File = os.path.join(Path, 'Dosen_List.csv')

# Baca List Mahasiswa
Local_List = []
if os.path.exists(List_File):
    with open(List_File, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header jika ada
        Local_List = [row for row in reader]
else:
    # Jika file tidak ada, buat file baru dengan header
    with open(List_File, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['NIM', 'Nama', 'No_HP', 'Email'])

# Baca Data Pengajuan (Jika Ada)
Local_Data = []
if os.path.exists(Data_File):
    with open(Data_File, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header jika ada
        Local_Data = [row for row in reader]
else:
    # Jika file tidak ada, buat file baru dengan header
    with open(Data_File, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['NIM', 'Nama', 'Judul', 'Deskripsi', 'Dosen_Pembimbing', 'Link', 'Status'])

# Baca Daftar Dosen
Dosen_List = []
if os.path.exists(Dosen_List_File):
    with open(Dosen_List_File, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader, None)  # Skip header jika ada
        Dosen_List = [row for row in reader]
else:
    with open(Dosen_List_File, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Nama_Dosen'])

# Mulai Program
while True:
    print("\n=== Sistem Pengajuan Tugas Akhir ===")
    print("1. Registrasi Mahasiswa Baru")
    print("2. Login")
    print("3. Keluar")
    pilihan = input("Masukkan pilihan (1/2/3): ")
    if pilihan == '1':
        New_Student = Register()
        if New_Student:
            # Tambahkan mahasiswa baru ke Local_List
            Local_List.append(New_Student)
            # Tulis data ke List.csv
            with open(List_File, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['NIM', 'Nama', 'No_HP', 'Email'])
                writer.writerows(Local_List)
            print("Registrasi berhasil.")
    elif pilihan == '2':
        Key, NIM, Nama = Login(Local_List)
        if Key:
            while True:
                print("\nPilih opsi:")
                print("1. Mengajukan Judul Tugas Akhir")
                print("2. Cek Status Pengajuan")
                print("3. Logout")
                choice = input("Masukkan pilihan (1/2/3): ")
                if choice == '1':
                    Submission = Apply(NIM, Nama , Dosen_List, Dosen_List_File)
                    if Submission:
                        # Tambahkan pengajuan ke data lokal
                        Local_Data.append(Submission)
                        # Tulis data ke Data.csv
                        with open(Data_File, mode='w', newline='') as file:
                            writer = csv.writer(file)
                            writer.writerow(['NIM', 'Nama', 'Judul', 'Deskripsi', 'Dosen_Pembimbing', 'Link', 'Status'])
                            writer.writerows(Local_Data)
                        print("Pengajuan berhasil disimpan.")
                    else:
                        print("Pengajuan gagal.")
                elif choice == '2':
                    CheckSubmission(NIM, Local_Data)
                elif choice == '3':
                    print("Logout berhasil.")
                    break
                else:
                    print("Pilihan tidak valid. Silakan pilih antara 1, 2, atau 3.")
        else:
            print("Login gagal.")
    elif pilihan == '3':
        print("Terima kasih, sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1, 2, atau 3.")
=======
# Quick Fix
Path = os.path.dirname(os.path.abspath(__file__))
List = os.path.join(Path, 'List.csv')
Data = os.path.join(Path, 'Data.csv')
Theme = os.path.join(Path, 'Theme.csv')
Professor = os.path.join(Path, 'Professor.csv')

#Baca List
Local_List = []
with open(List, mode='r') as file:
    reader = csv.reader(file)
    Local_List = [row for row in reader]
Local_Data = []
with open(Data, mode='r') as file:
    reader = csv.reader(file)
    Local_Data = [row for row in reader]
Local_Theme = []
with open(Theme, mode='r') as file:
    reader = csv.reader(file)
    Local_Theme = [row for row in reader]
Local_Professor = []
with open(Professor, mode='r') as file:
    reader = csv.reader(file)
    Local_Professor = [row for row in reader]

# Login
def Login(List):
    Name = input("Masukan nama: ")
    NRP = input("Masukan NRP: ")

    for user in List:
        if user[0] == Name and user[1] == NRP:
            print(f"Welcome, {Name}!")
            return True, Name

    print("Invalid bro, coba aja lagi.")
    return False, None

# Mengusulkan TA
def Apply(Name, Local_Theme, Local_Professor):
    Title = input("Judul TA : ")
    
    Key = 1
    while Key == 1:
        Theme = input("Tema TA : ")
        if Theme in [item for item in Local_Theme[0]]:
            Key = 0
        else:
            print("Tema salah, ulangi lagi.")
    
    # Plotting Dosen
    Professor = Local_Professor[0][Local_Theme[0].index(Theme)]
            
    Link = input("Link Tugas : ")
    Extra_Data = [[Name, Title, Theme, Professor, Link]]
    
    if Title and Theme and Link:
        return True, Extra_Data
    
    print("Coba lagi bro.")
    return False, None

#Start disini
Starter = 1
while Starter == 1:
    
    Key = False
    while Key == False:
        Key, Name = Login(Local_List)
        
    if Name in [row[0] for row in Local_Data]:
        print("Nama sudah terdaftar.")
        for A in range(len(Local_Data)):
            if Name in Local_Data[A]:
                print(Local_Data[A])
                break
    
    else:
        Key2, Extra_Data = Apply(Name, Local_Theme, Local_Professor)
        if Key2 == True:
            Local_Data += Extra_Data
            with open(Data, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(Local_Data)

    Starter = int(input("Lagi (0/1)? "))
>>>>>>> Stashed changes
