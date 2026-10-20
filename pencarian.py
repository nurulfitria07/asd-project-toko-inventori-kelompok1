from produk import daftar_produk, cari_index_by_kode

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