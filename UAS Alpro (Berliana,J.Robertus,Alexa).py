from collections import deque
from datetime import datetime


antrean_konsultasi_langsung = deque()
antrean_jadwal_konsultasi = deque()
jadwal_konsultasi = []


def login():
    """Fungsi untuk proses login pengguna"""
    credentials = {
        "pasien": {"username": "pasien", "password": "12345"},
        "admin": {"username": "admin", "password": "admin123"},
        "dokter": {"username": "dokter", "password": "dokter123"}
    }

    print("=== Login Sistem ===")

    print("Pilih peran:")
    print("1. Pasien")
    print("2. Admin")
    print("3. Dokter")

    role_choice = input("Masukkan pilihan (1/2/3): ")

    roles = {"1": "pasien", "2": "admin", "3": "dokter"}
    role = roles.get(role_choice)

    if not role:
        print("Pilihan tidak valid. Silakan coba lagi!")
        return None

    if role == "pasien":
        print("Login berhasil sebagai Pasien.")
        return role

    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    cred = credentials.get(role)
    if username == cred["username"] and password == cred["password"]:
        print(f"Login berhasil sebagai {role.capitalize()}.")
        return role

    print("Username atau password salah. Silakan coba lagi!")
    return None


def validasi_tanggal():
    while True:
        tanggal_input = input("Masukkan tanggal konsultasi (DD-MM-YYYY): ")
        try:
            tanggal_obj = datetime.strptime(tanggal_input, "%d-%m-%Y")
            return tanggal_obj.strftime("%d-%m-%Y")
        except ValueError:
            print("Format tanggal salah. Gunakan format DD-MM-YYYY.")


def get_hari(tanggal):
    hari_map = {
        0: "Senin",
        1: "Selasa",
        2: "Rabu",
        3: "Kamis",
        4: "Jumat",
        5: "Sabtu",
        6: "Minggu"
    }
    tanggal_obj = datetime.strptime(tanggal, "%d-%m-%Y")
    return hari_map[tanggal_obj.weekday()]



def tampilkan_jadwal_berdasarkan_hari():
    grouped = {}
    for jadwal in jadwal_konsultasi:
        hari = get_hari(jadwal["tanggal"])
        grouped.setdefault(hari, []).append(f"{jadwal['nama']} - ({jadwal['tanggal']} {jadwal['waktu']})")

    for hari in ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]:
        print(f"{hari}:")
        if hari in grouped:
            for jadwal in grouped[hari]:
                print(f"- {jadwal}")
        else:
            print("- Tidak ada pasien")



# Menu Pasien
def menu_pasien():
    while True:
        print("\n=== Menu Pasien ===")
        print("1. Ambil nomor antrean konsultasi langsung dengan dokter")
        print("2. Ambil nomor antrean mengatur jadwal konsultasi")
        print("3. Kembali ke menu login")

        choice = input("Masukkan pilihan (1/2/3): ")

        if choice == "1":
            nomor_antrean = len(antrean_konsultasi_langsung) + 1
            antrean_konsultasi_langsung.append(nomor_antrean)
            print(f"Nomor antrean konsultasi langsung Anda: {nomor_antrean}")
        elif choice == "2":
            nomor_antrean = len(antrean_jadwal_konsultasi) + 1
            antrean_jadwal_konsultasi.append(nomor_antrean)
            print(f"Nomor antrean janji konsultasi Anda: {nomor_antrean}")
        elif choice == "3":
            return
        else:
            print("Pilihan tidak valid. Silakan coba lagi!")

# Menu Admin
def menu_admin():
    while True:
        print("\n=== Menu Admin ===")
        print("1. Panggil nomor antrean konsultasi langsung")
        print("2. Panggil nomor antrean atur janji konsultasi")
        print("3. Tampilkan daftar jadwal pasien berdasarkan hari")
        print("4. Cari jadwal pasien berdasarkan nama")
        print("5. Edit jadwal konsultasi")
        print("6. Kembali ke menu login")

        choice = input("Masukkan pilihan (1/2/3/4/5/6): ")

        if choice == "1":
            if antrean_konsultasi_langsung:
                nomor_antrean = antrean_konsultasi_langsung.popleft()
                print(f"Memanggil nomor antrean konsultasi langsung: {nomor_antrean}")
            else:
                print("Tidak ada antrean konsultasi langsung.")
        elif choice == "2":
            if antrean_jadwal_konsultasi:
                nomor_antrean = antrean_jadwal_konsultasi.popleft()
                print(f"Memanggil nomor antrean janji konsultasi: {nomor_antrean}")
                nama = input("Masukkan nama pasien: ")
                usia = input("Masukkan usia pasien: ")
                penyakit = input("Masukkan penyakit pasien: ")
                nomor_telepon = input("Masukkan nomor telepon pasien: ")
                print("Pilih dokter:")
                print("1. Dokter Lexa")
                print("2. Dokter Berliana")
                dokter_choice = input("Masukkan pilihan (1/2): ")
                dokter = "Dokter Lexa" if dokter_choice == "1" else "Dokter Berliana"
                tanggal = validasi_tanggal()
                waktu = input("Masukkan waktu konsultasi (HH:MM): ")
                jadwal_konsultasi.append({"nama": nama, "usia": usia, "penyakit": penyakit, "nomor_telepon": nomor_telepon, "dokter": dokter, "tanggal": tanggal, "waktu": waktu})
                print("Jadwal konsultasi berhasil dibuat.")
            else:
                print("Tidak ada antrean janji konsultasi.")
        elif choice == "3":
            tampilkan_jadwal_berdasarkan_hari()
        elif choice == "4":
            nama = input("Masukkan nama pasien yang dicari: ")
            ditemukan = [jadwal for jadwal in jadwal_konsultasi if jadwal["nama"].lower() == nama.lower()]
            if ditemukan:
                print("Jadwal ditemukan:")
                for jadwal in ditemukan:
                    print(jadwal)
            else:
                print("Jadwal tidak ditemukan.")
        elif choice == "5":
            print("Daftar jadwal konsultasi:")
            for i, jadwal in enumerate(jadwal_konsultasi, start=1):
                print(f"{i}. {jadwal}")
            index = int(input("Masukkan nomor jadwal yang ingin diedit: ")) - 1
            if 0 <= index < len(jadwal_konsultasi):
                print("1. Edit tanggal")
                print("2. Edit waktu")
                print("3. Hapus jadwal")
                sub_choice = input("Masukkan pilihan (1/2/3): ")

                if sub_choice == "1":
                    tanggal_baru = validasi_tanggal()
                    jadwal_konsultasi[index]["tanggal"] = tanggal_baru
                    print("Tanggal berhasil diperbarui.")
                elif sub_choice == "2":
                    waktu_baru = input("Masukkan waktu baru (HH:MM): ")
                    jadwal_konsultasi[index]["waktu"] = waktu_baru
                    print("Waktu berhasil diperbarui.")
                elif sub_choice == "3":
                    jadwal_konsultasi.pop(index)
                    print("Jadwal berhasil dihapus.")
                else:
                    print("Pilihan tidak valid.")
            else:
                print("Nomor tidak valid.")
        elif choice == "6":
            return
        else:
            print("Pilihan tidak valid. Silakan coba lagi!")

# Menu Dokter
def menu_dokter():
    while True:
        print("\n=== Menu Dokter ===")
        print("1. Tampilkan daftar jadwal pasien berdasarkan hari")
        print("2. Hapus jadwal konsultasi setelah pasien konsultasi")
        print("3. Kembali ke menu login")

        choice = input("Masukkan pilihan (1/2/3): ")

        if choice == "1":
            tampilkan_jadwal_berdasarkan_hari()
        elif choice == "2":
            print("Daftar jadwal konsultasi:")
            for i, jadwal in enumerate(jadwal_konsultasi, start=1):
                print(f"{i}. {jadwal}")
            index = int(input("Masukkan nomor jadwal yang ingin dihapus: ")) - 1
            if 0 <= index < len(jadwal_konsultasi):
                jadwal_konsultasi.pop(index)
                print("Jadwal berhasil dihapus.")
            else:
                print("Nomor tidak valid.")
        elif choice == "3":
            return
        else:
            print("Pilihan tidak valid. Silakan coba lagi!")
            
            
            
if __name__ == "__main__":
    while True:
        user = login()
        if user == "pasien":
            menu_pasien()
        elif user == "admin":
            menu_admin()
        elif user == "dokter":
            menu_dokter()
        else:
            print("Gagal login. Program akan diulang.")