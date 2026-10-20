LEBAR_HEADER = 60
# Kolom tabel dan perataannya: "kanan" untuk angka, "kiri" untuk teks
NAMA_KOLOM = ["No", "Kode", "Nama", "Kategori", "Harga", "Stok"]
RATA_KOLOM = ["kanan", "kiri", "kiri", "kiri", "kanan", "kanan"]


def format_rupiah(angka):
    """Mengubah angka menjadi teks rupiah. Contoh: 15000 -> 'Rp 15.000'."""
    angka = float(angka)
    if angka.is_integer():
        teks = f"{int(angka):,}".replace(",", ".")
    else:
        # Ada pecahan: pakai koma sebagai pemisah desimal (gaya Indonesia)
        teks = f"{angka:,.2f}".replace(",", "#").replace(".", ",").replace("#", ".")
    return "Rp " + teks