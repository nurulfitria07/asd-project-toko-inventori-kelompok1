from riwayat import daftar_riwayat
from validasi import input_jumlah_riwayat
from tampilan import cetak_header_tabel_riwayat, cetak_baris_riwayat


def tampilkan_riwayat_terbaru():
    print("\n--- RIWAYAT TERBARU ---")

    if daftar_riwayat.tail is None:
        print("Belum ada riwayat transaksi.")
        return

    n = input_jumlah_riwayat("Tampilkan berapa riwayat terbaru? ")

    # Jika N melebihi jumlah catatan, maka akan menampilkan semuanya 
    jumlah_tampil = min(n, daftar_riwayat.jumlah)

    print(f"\nMenampilkan {jumlah_tampil} riwayat terbaru.\n")
    cetak_header_tabel_riwayat()

    node = daftar_riwayat.tail
    sudah_dicetak = 0
    while node is not None and sudah_dicetak < jumlah_tampil:
        cetak_baris_riwayat(node.data)
        node = node.prev
        sudah_dicetak += 1