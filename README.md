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

Pada Tahap 2, sistem mencatat **riwayat transaksi** setiap kali produk ditambah,
stok diubah, harga diubah, atau produk dihapus. Riwayat disimpan dalam
**Doubly Linked List** buatan sendiri (`riwayat.py`), bukan list atau deque bawaan
Python. Seluruh data hanya berada di memori, sehingga hilang saat program ditutup.

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
├── riwayat.py      # Node, Doubly Linked List, catat_riwayat() (R1)
├── riwayat_terbaru.py # R4
├── catatan-tahap2.md  # catatan teknis Tahap 2
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

### Fitur Tahap 2: Riwayat Transaksi (Linked List)

|Kode|          Fitur          |Menu|                        Keterangan                           |
|----|-------------------------|----|-------------------------------------------------------------|
| R1 | Pencatatan otomatis     | -  | Dicatat setelah F1, F4, F5, dan F6 berhasil                 |
|    |                         |    | Aksi gagal atau dibatalkan tidakdicatat.                    |
| R2 | Tampilkan semua riwayat | 7  | Dari terlama ke terbaru, dengan ringkasan jumlah per aksi   |
| R3 | Riwayat per produk      | 8  | Berdasarkan kode produk. Produk yang sudah dihapus tetap    |
|    |                         |    | bisa                                                        |
|    |                         |    | dicari.                                                     |
| R4 | Riwayat terbaru         | 9  | N riwayat terakhir, dari terbaru ke terlama (traversal      |
|    |                         |    | mundur lewat `tail` dan `prev`)                             |

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

### Tahap 2

|     Anggota    |     File            |                    Tanggung jawab                    |
|----------------|---------------------|------------------------------------------------------|
| Ikhwan Nurhakim| `riwayat.py`,       | Class `Node` dan `LinkedListRiwayat` (Singly, lalu   |
|                | `catatan-tahap2.md` | upgrade ke Doubly dengan `prev` dan `tail`)          |
| Nurul Fitria   | `riwayat.py`,       | R1: `catat_riwayat()`, pencatatan di F1, menu 7, 8, 9|
|                | `produk.py`,        |                                                      |
|                |  `main.py`          |                                                      |
| Raysah Naysila | `update.py`,        | R1: pencatatan di F4, F5, F6                         |
|                |  `hapus.py`,        | R4`tampilkan_riwayat_terbaru()`                      |
|                | `riwayat_terbaru.py`|                                                      |
|   Nala Adyuta  | `tampilan.py`,      | R2: `tampilkan_semua_riwayat()` dan helper tabel     |
|                | `README.md`         | riwayat                                              |
|  Angga Faisal  | `pencarian.py`,     | R3: `tampilkan_riwayat_produk()`, validator          |
|                |  `validasi.py`      | `input_jumlah_riwayat()`, pengujian                  |