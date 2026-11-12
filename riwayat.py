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
