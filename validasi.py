import math

def input_tidak_kosong(prompt):
    """Minta input teks dan ulangi sampai tidak kosong."""
    while True:
        teks = input(prompt).strip()
        if teks != "":
            return teks
        print("Error: input tidak boleh kosong.")

def input_konfirmasi(prompt):
    """Minta konfirmasi y/n dan ulangi sampai jawaban valid."""
    while True:
        jawaban = input(prompt).strip().lower()
        if jawaban == "y":
            return True
        if jawaban == "n":
            return False
        print("Error: jawab dengan 'y' (ya) atau 'n' (tidak).")