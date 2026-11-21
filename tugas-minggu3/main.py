"""Titik masuk aplikasi konsol SehatMahasiswa."""

from data import buat_catatan_kesehatan, login_mahasiswa, tampilkan_judul
from kesehatan import jalankan_menu


def main():
    tampilkan_judul()
    mahasiswa = login_mahasiswa()
    catatan = buat_catatan_kesehatan()
    jalankan_menu(mahasiswa, catatan)


if __name__ == "__main__":
    main()