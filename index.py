class Kafe:
    def __init__(self):
        self.menu = {}

    def tambah_menu(self, nama, harga):
        self.menu[nama] = harga

    def hapus_menu(self, nama):
        del self.menu[nama]

    def tampilkan_menu(self):
        print("Menu Kafe:")
        for nama, harga in self.menu.items():
            print(f"{nama}: Rp {harga}")

    def hitung_total(self, pesanan):
        total = 0
        for item in pesanan:
            menu, quantity = item.split(":")
            menu = menu.strip()
            quantity = int(quantity.strip())
            if menu in self.menu:
                total += self.menu[menu] * quantity
            else:
                print(f"Menu '{menu}' tidak tersedia.")
        return total

    def proses_pembayaran(self, total_harga):
        while True:
            uang_pembayaran = float(input("Masukkan jumlah uang pembayaran: "))
            if uang_pembayaran >= total_harga:
                kembalian = uang_pembayaran - total_harga
                print(f"Uang kembalian: Rp {kembalian:.2f}")
                break
            else:
                print("Jumlah uang pembayaran kurang. Silakan coba lagi.")


kafe = Kafe()

# Menambahkan menu
kafe.tambah_menu("Kopi", 10000)
kafe.tambah_menu("Teh", 8000)
kafe.tambah_menu("Roti", 15000)
kafe.tambah_menu("Susu", 12000)

while True:
    print("=== Kasir Kafe ===")
    print("1. Tampilkan Menu")
    print("2. Tambah Menu")
    print("3. Hapus Menu")
    print("4. Proses Pesanan")
    print("0. Keluar")
    pilihan = int(input("Masukkan pilihan Anda: "))

    if pilihan == 0:
        print("Terima kasih!")
        break
    elif pilihan == 1:
        kafe.tampilkan_menu()
    elif pilihan == 2:
        nama = input("Masukkan nama menu: ")
        harga = int(input("Masukkan harga menu: "))
        kafe.tambah_menu(nama, harga)
        print("Menu telah ditambahkan.")
    elif pilihan == 3:
        nama = input("Masukkan nama menu yang akan dihapus: ")
        kafe.hapus_menu(nama)
        print("Menu telah dihapus.")
    elif pilihan == 4:
        pesanan = input("Masukkan pesanan (format: menu:quantity,menu:quantity): ").split(",")
        total_harga = kafe.hitung_total(pesanan)
        print(f"Total harga: Rp {total_harga}")
        kafe.proses_pembayaran(total_harga)
    else:
        print("Pilihan tidak valid. Silakan coba lagi!")
