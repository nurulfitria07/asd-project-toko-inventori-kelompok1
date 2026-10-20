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