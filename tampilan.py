from produk import daftar_produk

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

def tampilkan_semua_produk():
    """Fitur 2: menampilkan seluruh produk dalam bentuk tabel."""
    print("\n--- DAFTAR SEMUA PRODUK ---")

    if len(daftar_produk) == 0:
        print("Belum ada produk yang tersimpan.")
        return

    cetak_tabel(daftar_produk)
    print(f"\nTotal: {len(daftar_produk)} produk.")

NAMA_KOLOM_RIWAYAT = ["No", "Waktu", "Aksi", "Kode", "Nama Produk","Nilai Lama", "Nilai Baru"]
LEBAR_KOLOM_RIWAYAT = [4, 19, 10, 7, 12, 24, 24]  # total 118 karakter dengan pemisah
RATA_KOLOM_RIWAYAT = ["kanan", "kiri", "kiri", "kiri", "kiri", "kiri", "kiri"]

def _potong_teks(teks, lebar):
    if len(teks) <= lebar:
        return teks
    return teks[:lebar - 1] + "…"

def cetak_header_tabel_riwayat():
    header = " │ ".join(
        _rata_teks(nama, LEBAR_KOLOM_RIWAYAT[i], RATA_KOLOM_RIWAYAT[i])
        for i, nama in enumerate(NAMA_KOLOM_RIWAYAT)
    )
    garis = "─┼─".join("─" * lebar for lebar in LEBAR_KOLOM_RIWAYAT)
    print(header)
    print(garis)

def cetak_baris_riwayat(riwayat): #mencetak satu baris tabel dari satu dict riwayat
    sel = [
        str(riwayat["no_urut"]),
        riwayat["waktu"],
        riwayat["aksi"],
        riwayat["kode_produk"],
        riwayat["nama_produk"],
        riwayat["nilai_lama"],
        riwayat["nilai_baru"],
    ]
    print(" │ ".join(
        _rata_teks(_potong_teks(isi, LEBAR_KOLOM_RIWAYAT[i]), LEBAR_KOLOM_RIWAYAT[i], RATA_KOLOM_RIWAYAT[i])
        for i, isi in enumerate(sel)
    ))