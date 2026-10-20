from validasi import input_tidak_kosong, input_harga, input_stok

daftar_produk = []

def buat_produk(kode_produk, nama, kategori, harga, stok):
    """Membuat satu struct produk (dict) dengan 5 atribut wajib."""
    return {
        "kode_produk": kode_produk,
        "nama": nama,
        "kategori": kategori,
        "harga": harga,
        "stok": stok,
    }

def cari_index_by_kode(kode):
    """Mencari posisi (index) produk berdasarkan kode secara exact match.
    Mengembalikan: index produk di daftar_produk, atau -1 jika tidak ada."""
    for index, produk in enumerate(daftar_produk):
        if produk["kode_produk"] == kode:
            return index
    return -1

def kode_sudah_ada(kode):
    """Mengembalikan True jika kode sudah dipakai produk lain."""
    return cari_index_by_kode(kode) != -1

def tambah_produk():
    """Fitur 1: menambahkan produk baru ke daftar_produk."""
    print("\n--- TAMBAH PRODUK BARU ---")

    # Kode tidak boleh kosong (dicek oleh input_tidak_kosong) dan tidak boleh duplikat
    kode = input_tidak_kosong("Kode produk : ")
    if kode_sudah_ada(kode):
        print(f"Gagal: kode produk '{kode}' sudah digunakan. Gunakan kode lain.")
        return

    nama = input_tidak_kosong("Nama produk : ")
    kategori = input_tidak_kosong("Kategori    : ")
    harga = input_harga("Harga (Rp)  : ")
    stok = input_stok("Stok        : ")

    produk_baru = buat_produk(kode, nama, kategori, harga, stok)
    daftar_produk.append(produk_baru)
    print(f"Produk {nama} berhasil ditambahkan.")