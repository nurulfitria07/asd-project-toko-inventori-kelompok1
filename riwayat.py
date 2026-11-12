class Node:
    """Satu simpul pada linked list. Menyimpan satu dict riwayat sebagai data."""

    def __init__(self, data):
        self.data = data
        self.next = None
