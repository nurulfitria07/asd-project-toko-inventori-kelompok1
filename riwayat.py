from datetime import datetime

class Node:
    """Satu simpul pada linked list. Menyimpan satu dict riwayat sebagai data."""

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListRiwayat:
    def __init__(self):
        self.head = None
        self.jumlah = 0

    def insert_akhir(self, data):
        node_baru = Node(data)

        if self.head is None:
            self.head = node_baru
        else:
            node_terakhir = self.head
            while node_terakhir.next is not None:
                node_terakhir = node_terakhir.next
            node_terakhir.next = node_baru

        self.jumlah += 1

daftar_riwayat = LinkedListRiwayat()

AKSI_TAMBAH = "TAMBAH"
AKSI_UBAH_STOK = "UBAH_STOK"
AKSI_UBAH_HARGA = "UBAH_HARGA"
AKSI_HAPUS = "HAPUS"

DAFTAR_AKSI = [AKSI_TAMBAH, AKSI_UBAH_STOK, AKSI_UBAH_HARGA, AKSI_HAPUS]