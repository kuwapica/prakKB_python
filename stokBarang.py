import json
import datetime

# File tempat menyimpan data mahasiwa
FILE_NAME = "stokBarang.json"

# Fungsi untuk membaca data dari file
def baca_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError):
        return []

# Fungsi untuk menyimpan data ke file
def simpan_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Fungsi untuk menambahkan buku
def tambah_barang(data):
    barang = input("Masukkan nama barang: ")
    harga = float(input("Masukkan harga satuan barang: "))
    stok = int(input("Masukkan stok barang: "))
    tanggal = datetime.datetime.now().strftime("%Y-%m-%d")

    stokBarang = {"tanggal": tanggal, "barang": barang, "harga": harga, "stok": stok}
    data.append(stokBarang)
    simpan_data(data)
    print("Barang berhasil ditambahkan!\n")

# Fungsi untuk menampilkan seluruh barang
def tampilkan_barang(data):
    if not data:
        print("Belum ada data barang.")
    else:
        print("\nData Barang:")
        print("No | Tanggal       | Barang        | Harga      | Stok | Total")
        print("-" * 60)
        for i, item in enumerate(data, start=1):
            total = item['harga'] * item['stok']
            print(f"{i}. | {item['tanggal']} | {item['barang']} | Rp{item['harga']:.2f} | {item['stok']} | Rp{total:.2f}")

# Fungsi untuk menghapus barang dari stok
def hapus_barang(data):
    tampilkan_barang(data)
    
    if not data:
        return
    
    barang = input("\nMasukkan nama barang yang akan dihapus: ").strip()
    
    # Filter barang yang tidak ingin dihapus
    data_baru = [item for item in data if item["barang"].lower() != barang.lower()]
    
    if len(data_baru) < len(data):
        simpan_data(data_baru)
        print(f"Barang '{barang}' berhasil dihapus.\n")
    else:
        print("Nama barang tidak ditemukan.\n")

# Program utama
def main():
    data_barang = baca_data()

    while True:
        print("\nMenu:")
        print("1. Tambah barang")
        print("2. Tampilkan barang")
        print("3. Hapus barang")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            tambah_barang(data_barang)
        elif pilihan == "2":
            tampilkan_barang(data_barang)
        elif pilihan == "3":
            hapus_barang(data_barang)
        elif pilihan == "4":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()
