import random
from tabulate import tabulate

print("\n====== SELAMAT DATANG ======\n==== DI RENTAL MOBIL KENZ MOBILINDO ====")

# Variabel global
existing_ids = set()

def generate_id():
    while True:
        new_id = random.randint(100, 999)
        if new_id not in existing_ids:
            existing_ids.add(new_id)
            return new_id

# Data mobil awal
data_mobil = [
    {'ID': generate_id(), 'Tipe Mobil': 'Avanza', 'Merk Mobil': 'Toyota', 'Tahun': '2018', 'Transmisi': 'MT', 'Harga Sewa': 500000, 'Stok': 2},
    {'ID': generate_id(), 'Tipe Mobil': 'BRV', 'Merk Mobil': 'Honda', 'Tahun': '2022', 'Transmisi': 'AT', 'Harga Sewa': 700000, 'Stok': 1},
    {'ID': generate_id(), 'Tipe Mobil': 'Almaz', 'Merk Mobil': 'Wuling', 'Tahun': '2020', 'Transmisi': 'AT', 'Harga Sewa': 850000, 'Stok': 1},
    {'ID': generate_id(), 'Tipe Mobil': 'Innova', 'Merk Mobil': 'Toyota', 'Tahun': '2017', 'Transmisi': 'MT', 'Harga Sewa': 750000, 'Stok': 3},
    {'ID': generate_id(), 'Tipe Mobil': 'Calya', 'Merk Mobil': 'Daihatsu', 'Tahun': '2019', 'Transmisi': 'MT', 'Harga Sewa': 400000, 'Stok': 2},
    {'ID': generate_id(), 'Tipe Mobil': 'Expander', 'Merk Mobil': 'Mitsubishi', 'Tahun': '2021', 'Transmisi': 'AT', 'Harga Sewa': 650000, 'Stok': 2}
]
data_hapus = []  # Tempat sampah untuk data mobil yang dihapus

# Fungsi input dengan validasi tambahan
def input_alfabet(pesan):
    while True:
        teks = input(pesan).strip()
        if teks == "":
            print("Input tidak boleh kosong.")
        elif not teks.isalpha() or len(teks) < 2:
            print("Input harus berupa alfabet dan minimal 2 karakter.")
        else:
            return teks.title()

def input_tahun():
    while True:
        tahun = input("Masukkan tahun mobil: ").strip()
        if tahun == "":
            print("Input tidak boleh kosong.")
        elif not tahun.isdigit() or len(tahun) != 4:
            print("Tahun harus berupa angka 4 digit.")
        else:
            return tahun

def input_transmisi():
    while True:
        transmisi = input("Masukkan transmisi mobil (AT/MT): ").strip().upper()
        if transmisi == "":
            print("Input tidak boleh kosong.")
        elif transmisi in ('AT', 'MT'):
            return transmisi
        else:
            print("Masukkan jawaban yang valid (AT/MT).")

def input_angka(pesan):
    while True:
        angka = input(pesan).strip()
        if angka == "":
            print("Input tidak boleh kosong.")
        elif not angka.isdigit():
            print("Input harus berupa angka.")
        else:
            return int(angka)

def konfirmasi():
    while True:
        jawab = input("Apakah Anda yakin? (Y: Ya / T: Tidak): ").strip().upper()
        if jawab in ('Y', 'T'):
            return jawab
        print("Jawaban harus Y atau T.")

# Fungsi untuk menampilkan data mobil
def tampilkan_mobil():
    if not data_mobil:
        print("Tidak ada data mobil yang tersedia.")
    else:
        print(tabulate(data_mobil, headers="keys", tablefmt="fancy_grid"))

# Fungsi untuk menambah mobil
def tambah_mobil():
    tampilkan_mobil()
    tipe = input_alfabet("Masukkan tipe mobil yang ingin ditambahkan: ")
    merk = input_alfabet("Masukkan merk mobil yang ingin ditambahkan: ")
    tahun = input_tahun()
    transmisi = input_transmisi()
    harga = input_angka("Masukkan harga sewa mobil: ")
    stok = input_angka("Masukkan stok mobil: ")

    print("\nDetail mobil yang akan ditambahkan:")
    print(f"Tipe Mobil  : {tipe}")
    print(f"Merk Mobil  : {merk}")
    print(f"Tahun       : {tahun}")
    print(f"Transmisi   : {transmisi}")
    print(f"Harga Sewa  : {harga}")
    print(f"Stok        : {stok}")

    if konfirmasi() == 'Y':
        data_mobil.append({
            'ID': generate_id(),
            'Tipe Mobil': tipe,
            'Merk Mobil': merk,
            'Tahun': tahun,
            'Transmisi': transmisi,
            'Harga Sewa': harga,
            'Stok': stok
        })
        print("Data mobil berhasil ditambahkan.")
    else:
        print("Penambahan data mobil dibatalkan.")

# Fungsi untuk memfilter mobil
def filter_mobil():
    if not data_mobil:
        print("Tidak ada mobil untuk difilter.")
        return
    print("\nFilter Mobil:")
    print("1. Berdasarkan Tipe")
    print("2. Berdasarkan Merk")
    print("3. Berdasarkan Tahun")
    print("4. Berdasarkan Transmisi")
    print("5. Berdasarkan Harga Sewa")
    print("6. Berdasarkan Stok")
    pilihan = input_angka("Pilih filter (1-6): ")

    if pilihan == 1:
        kriteria = input("Masukkan tipe mobil: ").title()
        hasil = [m for m in data_mobil if kriteria in m['Tipe Mobil']]
    elif pilihan == 2:
        kriteria = input("Masukkan merk mobil: ").title()
        hasil = [m for m in data_mobil if kriteria in m['Merk Mobil']]
    elif pilihan == 3:
        kriteria = input("Masukkan tahun mobil: ")
        hasil = [m for m in data_mobil if kriteria == m['Tahun']]
    elif pilihan == 4:
        kriteria = input("Masukkan transmisi (AT/MT): ").upper()
        hasil = [m for m in data_mobil if kriteria == m['Transmisi']]
    elif pilihan == 5:
        kriteria = input_angka("Masukkan harga sewa: ")
        hasil = [m for m in data_mobil if kriteria == m['Harga Sewa']]
    elif pilihan == 6:
        kriteria = input_angka("Masukkan stok mobil: ")
        hasil = [m for m in data_mobil if kriteria == m['Stok']]
    else:
        print("Pilihan tidak valid.")
        return

    if hasil:
        print(tabulate(hasil, headers="keys", tablefmt="fancy_grid"))
    else:
        print("Tidak ada mobil yang memenuhi kriteria.")

# Fungsi untuk mengubah data mobil
def ubah_mobil():
    tampilkan_mobil()
    if not data_mobil:
        return
    while True:
        id_mobil = input_angka("Masukkan ID mobil yang ingin diubah (3 digit): ")
        if id_mobil < 100 or id_mobil > 999:
            print("ID harus berupa 3 digit.")
            continue
        index = next((i for i, m in enumerate(data_mobil) if m['ID'] == id_mobil), -1)
        if index == -1:
            print("ID tidak ditemukan.")
            continue
        break
    print("Data mobil terpilih:")
    print(data_mobil[index])
    print("\nData yang dapat diubah:")
    print("1. Tipe Mobil")
    print("2. Merk Mobil")
    print("3. Tahun")
    print("4. Transmisi")
    print("5. Harga Sewa")
    print("6. Stok")
    pilihan = input_angka("Pilih data yang ingin diubah (1-6): ")
    if pilihan == 1:
        data_mobil[index]['Tipe Mobil'] = input_alfabet("Masukkan tipe mobil baru: ")
    elif pilihan == 2:
        data_mobil[index]['Merk Mobil'] = input_alfabet("Masukkan merk mobil baru: ")
    elif pilihan == 3:
        data_mobil[index]['Tahun'] = input_tahun()
    elif pilihan == 4:
        data_mobil[index]['Transmisi'] = input_transmisi()
    elif pilihan == 5:
        data_mobil[index]['Harga Sewa'] = input_angka("Masukkan harga sewa baru: ")
    elif pilihan == 6:
        data_mobil[index]['Stok'] = input_angka("Masukkan stok baru: ")
    else:
        print("Pilihan tidak valid.")
        return
    print("Data mobil telah diubah:")
    print(data_mobil[index])

# Fungsi untuk menghapus mobil
def hapus_mobil():
    tampilkan_mobil()
    if not data_mobil:
        return
    while True:
        id_mobil = input_angka("Masukkan ID mobil yang ingin dihapus (3 digit): ")
        if id_mobil < 100 or id_mobil > 999:
            print("ID harus berupa 3 digit.")
            continue
        index = next((i for i, m in enumerate(data_mobil) if m['ID'] == id_mobil), -1)
        if index == -1:
            print("ID tidak ditemukan.")
            continue
        break
    print("Data mobil yang dipilih:")
    print(data_mobil[index])
    if konfirmasi() == 'Y':
        data_hapus.append(data_mobil.pop(index))
        print("Mobil berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")

# Fungsi tempat sampah (recycle bin)
def tempat_sampah():
    if not data_hapus:
        print("Tidak ada data di tempat sampah.")
        return
    print("Data mobil di tempat sampah:")
    print(tabulate(data_hapus, headers="keys", tablefmt="fancy_grid"))
    id_kembali = input_angka("Masukkan ID mobil yang ingin dikembalikan (0 untuk batal): ")
    if id_kembali == 0:
        print("Pengembalian dibatalkan.")
        return
    index = next((i for i, m in enumerate(data_hapus) if m['ID'] == id_kembali), -1)
    if index == -1:
        print("ID tidak ditemukan di tempat sampah.")
    else:
        data_mobil.append(data_hapus.pop(index))
        print("Mobil berhasil dikembalikan.")

# Fungsi untuk memesan mobil
def pesan_mobil():
    tampilkan_mobil()
    if not data_mobil:
        return
    while True:
        id_mobil = input_angka("Masukkan ID mobil yang ingin dipesan (3 digit): ")
        if id_mobil < 100 or id_mobil > 999:
            print("ID harus berupa 3 digit.")
            continue
        mobil = next((m for m in data_mobil if m['ID'] == id_mobil), None)
        if not mobil:
            print("ID mobil tidak ditemukan.")
            continue
        break
    if mobil['Stok'] <= 0:
        print("Stok mobil habis.")
        return
    durasi = input_angka("Masukkan durasi sewa (hari): ")
    if durasi <= 0:
        print("Durasi sewa harus lebih dari 0.")
        return
    total = mobil['Harga Sewa'] * durasi
    print(f"Total harga sewa: Rp {total:,}".replace(",", "."))
    bayar = input_angka("Masukkan jumlah uang yang dibayarkan: Rp ")
    if bayar < total:
        print("Uang tidak cukup, transaksi gagal.")
        return
    mobil['Stok'] -= 1
    if bayar > total:
        kembalian = bayar - total
        print(f"Transaksi berhasil. Kembalian: Rp {kembalian:,}".replace(",", "."))
    else:
        print("Transaksi berhasil. Uang pas.")
    print("Mobil telah dipesan:")
    print(mobil)

# Menu Admin
def menu_admin():
    while True:
        print("\n--- Menu Admin ---")
        print("1. Tampilkan Mobil")
        print("2. Filter Mobil")
        print("3. Tambah Mobil")
        print("4. Ubah Mobil")
        print("5. Hapus Mobil")
        print("6. Tempat Sampah")
        print("7. Keluar")
        pilihan = input_angka("Masukkan pilihan (1-7): ")
        if pilihan == 1:
            tampilkan_mobil()
        elif pilihan == 2:
            filter_mobil()
        elif pilihan == 3:
            tambah_mobil()
        elif pilihan == 4:
            ubah_mobil()
        elif pilihan == 5:
            hapus_mobil()
        elif pilihan == 6:
            tempat_sampah()
        elif pilihan == 7:
            print("Keluar dari menu admin.")
            break
        else:
            print("Pilihan tidak valid.")

# Menu Pelanggan
def menu_pelanggan():
    while True:
        print("\n--- Menu Pelanggan ---")
        tampilkan_mobil()
        print("1. Pesan Mobil")
        print("2. Keluar")
        pilihan = input_angka("Masukkan pilihan (1-2): ")
        if pilihan == 1:
            pesan_mobil()
        elif pilihan == 2:
            print("Terima kasih.")
            break
        else:
            print("Pilihan tidak valid.")

# Fungsi Login
def login():
    while True:
        print("\n--- Login ---")
        print("1. Login sebagai Admin")
        print("2. Login sebagai Pelanggan")
        print("3. Keluar")
        pilihan = input_angka("Masukkan pilihan (1-3): ")
        if pilihan == 1:
            username = input("Masukkan username admin: ").strip()
            password = input("Masukkan password admin: ").strip()
            if username == "derinadimar" and password == "derin1995":
                print("Login berhasil. Selamat datang Admin!")
                menu_admin()
            else:
                print("Username atau password salah.")
        elif pilihan == 2:
            print("Login sebagai pelanggan berhasil.")
            menu_pelanggan()
        elif pilihan == 3:
            print("Terima kasih telah menggunakan aplikasi.")
            break
        else:
            print("Pilihan tidak valid.")

# Program utama
login()

