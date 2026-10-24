from produk import daftar_produk, cari_index_by_kode  
from validasi import input_konfirmasi, input_tidak_kosong  
from tampilan import cetak_tabel

def hapus_produk():
    """Fitur 6: menghapus produk berdasarkan kode setelah operator konfirmasi."""
    print("\n--- HAPUS PRODUK ---")

    #cek apakah ada produk yang tersimpan
    if len(daftar_produk) == 0:
        print("Belum ada produk yang tersimpan.")
        return

    kode = input_tidak_kosong("Kode produk yang akan dihapus: ")  
    index = cari_index_by_kode(kode)  
    if index == -1:  
        print(f"Produk dengan kode '{kode}' tidak ditemukan.")  
        return  

    produk = daftar_produk[index]  

    # Tampilkan dulu produk yang akan dihapus agar operator tidak salah hapus  
    print("\nProduk yang akan dihapus:")  
    cetak_tabel([produk])  
    print()

    if input_konfirmasi(f"Yakin ingin menghapus '{produk['nama']}'? (y/n): "):  
        nama = produk["nama"]  
        del daftar_produk[index]  # hapus langsung dari list yang sama  
        print(f"Produk {nama} berhasil dihapus dari sistem.")  
    else:  
        print("Penghapusan dibatalkan.")  