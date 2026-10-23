from produk import daftar_produk, cari_index_by_kode
from validasi import input_tidak_kosong, input_harga, input_stok
from tampilan import format_rupiah

def update_stok():
    """Fitur 4: mengganti stok produk dengan nilai baru (bukan penambahan)."""
    print("\n--- UPDATE STOK PRODUK ---")

    #cek apakah ada produk yang tersimpan
    if len(daftar_produk) == 0:
        print("Belum ada produk yang tersimpan.")
        return

    kode = input_tidak_kosong("Kode produk yang diupdate: ")
    index = cari_index_by_kode(kode)
    if index == -1:
        print(f"Error: produk dengan kode '{kode}' tidak ditemukan.")
        return

    produk = daftar_produk[index]
    print(f"Produk     : {produk['nama']}")
    print(f"Stok saat ini: {produk['stok']}")

    stok_baru = input_stok("Stok baru (angka bulat >= 0): ")

    stok_lama = produk["stok"]
    produk["stok"] = stok_baru
    print(f"Stok produk {produk['nama']} berhasil diperbarui: "
          f"{stok_lama} menjadi {stok_baru}")

def update_harga():
    """Fitur 5: mengganti harga satuan produk dengan nilai baru."""
    print("\n--- UPDATE HARGA PRODUK ---")

    #cek apakah ada produk yang tersimpan
    if len(daftar_produk) == 0:
        print("Belum ada produk yang tersimpan.")
        return

    kode = input_tidak_kosong("Kode produk yang diupdate: ")
    index = cari_index_by_kode(kode)
    if index == -1:
        print(f"Error: produk dengan kode '{kode}' tidak ditemukan.")
        return

    produk = daftar_produk[index]
    print(f"Produk     : {produk['nama']}")
    print(f"Harga saat ini: {format_rupiah(produk['harga'])}")

    harga_baru = input_harga("Harga baru (Rp, harus > 0): ")

    harga_lama = produk["harga"]
    produk["harga"] = harga_baru
    print(f"Harga produk {produk['nama']} berhasil diperbarui: "
          f"{format_rupiah(harga_lama)} menjadi {format_rupiah(harga_baru)}")