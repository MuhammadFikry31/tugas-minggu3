"""Data mahasiswa dan helper input untuk aplikasi SehatMahasiswa."""


PROGRAM_STUDI = (
    "D3 Teknik Informatika",
    "D4 1A Teknik Informatika",
    "D4 1B Teknik Informatika",
)

_LOGO_ALKACARE = {
    "A": (".###.", "#...#", "#####", "#...#", "#...#"),
    "L": ("#....", "#....", "#....", "#....", "#####"),
    "K": ("#...#", "#..#.", "###..", "#..#.", "#...#"),
    "C": (".####", "#....", "#....", "#....", ".####"),
    "R": ("####.", "#...#", "####.", "#..#.", "#...#"),
    "E": ("#####", "#....", "####.", "#....", "#####"),
}


def tampilkan_judul():
    """Menampilkan judul ASCII ALKACARE pada layar aplikasi."""
    for baris in zip(*(_LOGO_ALKACARE[huruf] for huruf in "ALKACARE")):
        print("  ".join(baris).replace(".", " ").replace("#", "8"))
    print("  ALKACARE")
    print("  APLIKASI KESEHATAN MAHASISWA")
    print()


def input_teks_wajib(prompt):
    """Meminta teks yang tidak boleh kosong."""
    while True:
        nilai = input(prompt).strip()
        if nilai:
            return nilai
        print("Input tidak boleh kosong.")


def input_angka(prompt, minimum, maksimum):
    """Meminta bilangan bulat pada rentang yang ditentukan."""
    while True:
        try:
            nilai = int(input(prompt))
        except ValueError:
            print("Masukkan angka bulat.")
            continue

        if minimum <= nilai <= maksimum:
            return nilai
        print(f"Masukkan angka antara {minimum} dan {maksimum}.")


def input_jam_tidur(prompt):
    """Meminta durasi tidur dalam jam, maksimal satu angka desimal."""
    while True:
        try:
            nilai = float(input(prompt).replace(",", "."))
        except ValueError:
            print("Masukkan jumlah jam yang valid, misalnya 7 atau 7.5.")
            continue

        if 0 < nilai <= 24:
            return nilai
        print("Durasi tidur harus lebih dari 0 dan tidak lebih dari 24 jam.")


def login_mahasiswa():
    """Mengumpulkan identitas mahasiswa untuk sesi aplikasi."""
    print("\n=== FORM LOGIN MAHASISWA ===")
    nim = input_teks_wajib("NIM: ")
    nama = input_teks_wajib("Nama: ")

    print("\nPilih program studi:")
    for nomor, program_studi in enumerate(PROGRAM_STUDI, start=1):
        print(f"{nomor}. {program_studi}")

    pilihan = input_angka("Pilihan program studi: ", 1, len(PROGRAM_STUDI))
    return {
        "nim": nim,
        "nama": nama,
        "prodi": PROGRAM_STUDI[pilihan - 1],
    }


def buat_catatan_kesehatan():
    """Membuat catatan kesehatan sementara untuk satu sesi."""
    return {
        "aktivitas": [],
        "air_ml": 0,
        "tidur_jam": None,
        "ckg": {"janji": [], "rujukan": [], "imt": None, "survey": None},
    }