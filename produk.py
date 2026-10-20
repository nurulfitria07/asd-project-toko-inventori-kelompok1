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