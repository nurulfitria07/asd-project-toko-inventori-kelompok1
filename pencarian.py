from produk import daftar_produk, cari_index_by_kode

def cari_by_kode(kode):
    """Mencari produk dengan kode yang persis sama.
    Mengembalikan: list berisi 1 produk, atau list kosong jika tidak ada.
    """
    index = cari_index_by_kode(kode)
    if index == -1:
        return []
    return [daftar_produk[index]]