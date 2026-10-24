import math

def input_tidak_kosong(prompt):
    """Minta input teks dan ulangi sampai tidak kosong.

    Mengembalikan: str yang sudah dibersihkan spasi di kiri/kanan.
    """
    while True:
        teks = input(prompt).strip()
        if teks != "":
            return teks
        print("Error: input tidak boleh kosong.")


def input_harga(prompt):
    """Minta input harga dan ulangi sampai berupa angka > 0.

    Mengembalikan: float (harga lebih dari 0).
    """
    while True:
        # Menambahkan indikator Rp secara otomatis
        prompt_teks = prompt if "Rp" in prompt else f"{prompt} (Rp): "
        teks = input(prompt_teks).strip()
        
        try:
            harga = float(teks)
        except ValueError:
            print("Error: harga harus berupa angka (contoh: 15000).")
            continue

        # Memastikan input bukan Infinity atau NaN
        if not math.isfinite(harga):
            print("Error: harga harus berupa angka yang valid.")
        elif harga <= 0:
            print("Error: harga harus lebih dari 0.")
        else:
            return harga


def input_stok(prompt):
    """Minta input stok dan ulangi sampai berupa bilangan bulat >= 0.

    Mengembalikan: int (stok tidak negatif).
    """
    while True:
        teks = input(prompt).strip()
        try:
            stok = int(teks)
        except ValueError:
            print("Error: stok harus berupa angka bulat (contoh: 50).")
            continue

        if stok < 0:
            print("Error: stok tidak boleh negatif.")
        else:
            return stok


def input_konfirmasi(prompt):
    """Minta konfirmasi y/n dan ulangi sampai jawaban valid.

    Mengembalikan: True jika 'y', False jika 'n'.
    """
    while True:
        jawaban = input(prompt).strip().lower()
        if jawaban == "y":
            return True
        if jawaban == "n":
            return False
        print("Error: jawab dengan 'y' (ya) atau 'n' (tidak).")