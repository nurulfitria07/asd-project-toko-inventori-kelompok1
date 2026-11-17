from datetime import datetime

class Node:
    """Satu simpul pada linked list. Menyimpan satu dict riwayat sebagai data."""

    def __init__(self, data):
        self.data = data
        self.prev = None #DOUBLY
        self.next = None

class LinkedListRiwayat:
    def __init__(self):
        self.head = None
        self.tail = None  # DOUBLY
        self.jumlah = 0

    def insert_akhir(self, data):
        node_baru = Node(data)

        if self.head is None:
            self.head = node_baru
            self.tail = node_baru  # DOUBLY
        else:
            node_baru.prev = self.tail  # DOUBLY
            self.tail.next = node_baru  # DOUBLY
            self.tail = node_baru  # DOUBLY
            
        self.jumlah += 1

daftar_riwayat = LinkedListRiwayat()

AKSI_TAMBAH = "TAMBAH"
AKSI_UBAH_STOK = "UBAH_STOK"
AKSI_UBAH_HARGA = "UBAH_HARGA"
AKSI_HAPUS = "HAPUS"

DAFTAR_AKSI = [AKSI_TAMBAH, AKSI_UBAH_STOK, AKSI_UBAH_HARGA, AKSI_HAPUS]

def angka_ke_teks(angka):
    angka = float(angka)
    if angka.is_integer():
        return str(int(angka))
    return str(angka)

def ringkasan_produk(produk):
    return f"stok={produk['stok']}; harga={angka_ke_teks(produk['harga'])}"

def catat_riwayat(aksi, produk, nilai_lama, nilai_baru):
    riwayat = {
        "no_urut": daftar_riwayat.jumlah + 1,
        "aksi": aksi,
        "kode_produk": produk["kode_produk"],
        "nama_produk": produk["nama"],
        "nilai_lama": nilai_lama,
        "nilai_baru": nilai_baru,
        "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    daftar_riwayat.insert_akhir(riwayat)