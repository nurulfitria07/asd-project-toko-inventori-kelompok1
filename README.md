# Sistem Manajemen Toko / Inventori

## 1. Nama dan Anggota

**Kelompok:1** 

| No|            Nama            |      NIM      |
|---|----------------------------|---------------|
| 1 | Ikhwan Nurhakim Pratidina  | [25083000003] |
| 2 | Nurul Fitria               | [25083000005] |
| 3 | Angga Faisal Abi           | [25083000054] |
| 4 | Raysah Naysila Ulima Bahri | [25083000056] |
| 5 | Nala Adyuta Insani         | [25083000057] |

## 2. Deskripsi

Sistem Manajemen Toko / Inventori adalah program berbasis terminal yang ditulis dengan Python untuk membantu operator mengelola data produk toko. Data produk disimpan dalam list berisi dictionary (array of struct) dengan atribut kode, nama, kategori, harga, dan stok. Program dilengkapi validasi input agar data yang masuk selalu benar dan konfirmasi sebelum penghapusan agar tidak terjadi salah hapus.

## 3. Cara Menjalankan

```bash
git clone https://github.com/nurulfitria07/asd-project-toko-kelompok1.git
cd asd-project-toko-kelompok1
python main.py
```

Pastikan Python 3.8 atau lebih sudah terpasang. Program tidak membutuhkan library tambahan.

Struktur folder:

```
asd-project-toko-kelompok1/
├── main.py         # menu utama & routing
├── produk.py       # data store + struct + tambah produk baru
├── validasi.py     # semua validasi input
├── update.py       # update stok & update harga
├── tampilan.py     # format tabel & rupiah + tampilkan semua produk
├── pencarian.py    # cari produk
├── hapus.py        # hapus produk
└── README.md
```

## 4. Fitur yang Sudah Ada

| Menu |                                               Fitur                                                        |      File      |
|------|------------------------------------------------------------------------------------------------------------|----------------|
|   1  | Tambah produk baru (kode tidak boleh kosong dan tidak boleh duplikat)                                      | `produk.py`    |
|   2  | Tampilkan semua produk dalam bentuk tabel rapi                                                             | `tampilan.py`  |
|   3  | Cari produk berdasarkan kode (persis sama) atau nama (mengandung kata kunci, tidak peka huruf besar/kecil) | `pencarian.py` |
|   4  | Update stok produk (mengganti dengan nilai baru)                                                           | `update.py`    |
|   5  | Update harga produk (harus lebih dari 0)                                                                   | `update.py`    |
|   6  | Hapus produk setelah operator konfirmasi y/n                                                               | `hapus.py`     |
|   0  | Keluar dari program                                                                                        | `main.py`      |

Fitur pendukung: validasi input teks, harga, stok, dan konfirmasi (`validasi.py`), serta format harga rupiah (contoh: `Rp 15.000`).

## 5. Pembagian Tugas

|      Anggota    |                                        Tugas                                          |            File            |
|-----------------|---------------------------------------------------------------------------------------|----------------------------|
| Nurul Fitria    | Membuat menu utama dan routing (`MENU`, `tampilkan_menu`, `jeda`, `main`).            | `main.py`, `produk.py`     |
|                 | Membuat data store `daftar_produk`, struct `buat_produk`, fungsi `cari_index_by_kode` |                            |
|                 | dan `kode_sudah_ada`, serta Fitur 1 (`tambah_produk`)                                 |                            |
| Angga Faisal    | Membuat semua validasi input (`input_tidak_kosong`, `input_harga`, `input_stok`,      |                            |
|                 | `input_konfirmasi`). Membuat Fitur 4 (`update_stok`) dan Fitur 5 (`update_harga`)     | `validasi.py`, `update.py` |
| Raysah Naysila  | Membuat Fitur 6 (`hapus_produk`) dengan tampilan detail produk dan konfirmasi         |                            |
|                 | sebelum hapus. Menulis dokumentasi proyek                                             | `hapus.py`, `README.md`    |
| Nala Adyuta     | Membuat `format_rupiah`, `cetak_header`, `cetak_tabel`, dan Fitur 2                   |                            |
|                 | (`tampilkan_semua_produk`)                                                            | `tampilan.py`              |
| Ikhwan Nurhakim | Membuat Fitur 3: `cari_by_kode`, `cari_by_nama`, dan `cari_produk`                    | `pencarian.py`             |
# asd-project-toko-inventori-kelompok1