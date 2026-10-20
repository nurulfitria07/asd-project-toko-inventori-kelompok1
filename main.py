from produk import tambah_produk
from tampilan import cetak_header, tampilkan_semua_produk
from pencarian import cari_produk
from update import update_stok, update_harga
from hapus import hapus_produk

MENU = {
    "1": ("Tambah produk baru", tambah_produk),
    "2": ("Tampilkan semua produk", tampilkan_semua_produk),
    "3": ("Cari produk", cari_produk),
    "4": ("Update stok produk", update_stok),
    "5": ("Update harga produk", update_harga),
    "6": ("Hapus produk", hapus_produk),
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