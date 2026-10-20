from produk import cari_index_by_kode  
from validasi import input_tidak_kosong  


def hapus_produk():
    """Fitur 6: menghapus produk berdasarkan kode setelah operator konfirmasi."""
    print("\n--- HAPUS PRODUK ---")

    kode = input_tidak_kosong("Kode produk yang akan dihapus: ")  
    index = cari_index_by_kode(kode)  
    if index == -1:  
        print(f"Produk dengan kode '{kode}' tidak ditemukan.")  
        return  