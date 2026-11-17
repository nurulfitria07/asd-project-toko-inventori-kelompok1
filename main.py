from produk import tambah_produk
from tampilan import cetak_header, tampilkan_semua_produk
from pencarian import cari_produk
from update import update_stok, update_harga
from hapus import hapus_produk
from tampilan import tampilkan_semua_riwayat
from pencarian import tampilkan_riwayat_produk

MENU = {
    "1": ("Tambah produk baru", tambah_produk),
    "2": ("Tampilkan semua produk", tampilkan_semua_produk),
    "3": ("Cari produk", cari_produk),
    "4": ("Update stok produk", update_stok),
    "5": ("Update harga produk", update_harga),
    "6": ("Hapus produk", hapus_produk),
    "7": ("Tampilkan riwayat transaksi", tampilkan_semua_riwayat),
    "8": ("Riwayat per produk", tampilkan_riwayat_produk)
}

def tampilkan_menu():
    """Mencetak daftar menu utama."""
    cetak_header("SISTEM MANAJEMEN TOKO / INVENTORI")
    for pilihan, (label, _fungsi) in MENU.items():
        print(f"  {pilihan}. {label}")
    print("  0. Keluar")

def jeda():
    """Menahan layar sampai operator menekan Enter agar hasil sempat dibaca."""
    try:
        input("\nTekan Enter untuk kembali ke menu...")
    except (EOFError, KeyboardInterrupt):
        pass

def main():
    """Loop utama program: tampilkan menu, baca pilihan, jalankan fitur."""
    while True:
        tampilkan_menu()

        try:
            pilihan = input(f"\nPilih menu (0-{len(MENU)}): ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nProgram dihentikan.")
            break

        if pilihan == "0":
            print("Terima kasih. Program selesai.")
            break

        if pilihan in MENU:
            _label, fungsi = MENU[pilihan]
            try:
                fungsi()
            except (EOFError, KeyboardInterrupt):
                # Ctrl+C di tengah fitur tidak boleh membuat program berhenti
                print("\nOperasi dibatalkan, kembali ke menu.")
        else:
            print(f"Pilihan tidak valid. Masukkan angka 0 sampai {len(MENU)}.")

        jeda()

if __name__ == "__main__":
    main()