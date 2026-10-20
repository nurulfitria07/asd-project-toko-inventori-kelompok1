from produk import daftar_produk, cari_index_by_kode
from validasi import input_tidak_kosong
from tampilan import cetak_tabel

def cari_by_kode(kode):
    """Mencari produk dengan kode yang persis sama.
    Mengembalikan: list berisi 1 produk, atau list kosong jika tidak ada.
    """
    index = cari_index_by_kode(kode)
    if index == -1:
        return []
    return [daftar_produk[index]]

def cari_by_nama(kata_kunci):
    """Mencari semua produk yang namanya MENGANDUNG kata kunci.

    Tidak peka huruf besar/kecil: 'goreng' cocok dengan 'Minyak Goreng 1L'.
    Mengembalikan: list produk yang cocok (bisa kosong).
    """
    kata_kunci = kata_kunci.lower()
    hasil = []
    for produk in daftar_produk:
        if kata_kunci in produk["nama"].lower():
            hasil.append(produk)
    return hasil

def cari_produk():
    """Fitur 3: operator memilih mode pencarian lalu memasukkan kata kunci."""
    print("\n--- CARI PRODUK ---")
    print("Cari berdasarkan:")
    print("  1. Kode produk (harus persis sama)")
    print("  2. Nama produk (cukup mengandung kata kunci)")
    pilihan = input("Pilih mode (1/2): ").strip()

    if pilihan == "1":
        jenis = "kode"
    elif pilihan == "2":
        jenis = "nama"
    else:
        print("Error: pilihan mode tidak valid. Pilih 1 atau 2.")
        return

    # Kata kunci tidak boleh kosong
    kata_kunci = input_tidak_kosong(f"Masukkan {jenis} produk: ")

    if jenis == "kode":
        hasil = cari_by_kode(kata_kunci)
    else:
        hasil = cari_by_nama(kata_kunci)

    if len(hasil) == 0:
        print(f"Produk dengan {jenis} '{kata_kunci}' tidak ditemukan.")
        return

    print(f"\nDitemukan {len(hasil)} produk:\n")
    cetak_tabel(hasil)