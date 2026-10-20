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

def cetak_header(judul):
    """Mencetak judul dengan garis pemisah di atas dan bawah."""
    garis = "=" * LEBAR_HEADER
    print()
    print(garis)
    print(judul.center(LEBAR_HEADER))
    print(garis)

def _rata_teks(teks, lebar, rata):
    """Fungsi bantu: meratakan teks sesuai lebar kolom."""
    if rata == "kanan":
        return teks.rjust(lebar)
    return teks.ljust(lebar)


def cetak_tabel(list_produk):
    """Mencetak tabel produk dengan kolom: No, Kode, Nama, Kategori, Harga, Stok.

    Lebar kolom menyesuaikan isi data agar selalu rapi.
    """
    # 1. Siapkan isi setiap baris dalam bentuk teks
    semua_baris = []
    for nomor, produk in enumerate(list_produk, start=1):
        semua_baris.append([
            str(nomor),
            produk["kode_produk"],
            produk["nama"],
            produk["kategori"],
            format_rupiah(produk["harga"]),
            str(produk["stok"]),
        ])

    # 2. Hitung lebar tiap kolom = teks terpanjang (header atau isi data)
    lebar_kolom = []
    for i, nama_kolom in enumerate(NAMA_KOLOM):
        panjang_isi = [len(baris[i]) for baris in semua_baris]
        lebar_kolom.append(max([len(nama_kolom)] + panjang_isi))

    # 3. Cetak header, garis pemisah, lalu isi tabel
    header = " │ ".join(
        _rata_teks(nama, lebar_kolom[i], RATA_KOLOM[i])
        for i, nama in enumerate(NAMA_KOLOM)
    )
    garis = "─┼─".join("─" * lebar for lebar in lebar_kolom)

    print(header)
    print(garis)
    for baris in semua_baris:
        print(" │ ".join(
            _rata_teks(sel, lebar_kolom[i], RATA_KOLOM[i])
            for i, sel in enumerate(baris)
        ))