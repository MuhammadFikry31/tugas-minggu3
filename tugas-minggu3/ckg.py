"""Menu simulasi layanan Cek Kesehatan Gratis (CKG)."""

from data import input_angka, input_teks_wajib, tampilkan_judul


PERTANYAAN_SURVEI = (
    "Apakah Anda Melakukan Pemeriksaan Kesehatan dalam 12 Bulan Terakhir?",
    "Apakah Anda Aktif Bergerak atau Berolahraga Secara Rutin?",
    "Apakah Anda biasanya mendapatkan waktu tidur yang cukup?",
    "Apakah Anda minum air secara berkala setiap hari?",
    "Apakah Anda mengonsumsi buah atau sayur setiap hari?",
)

PUSKESMAS_TERSEDIA = (
    "Puskesmas Sariwangi",
    "Puskesmas Bandung",
    "Puskesmas Cimahi",
)


def pilih_puskesmas():
    """Meminta pengguna memilih salah satu puskesmas yang tersedia."""
    print("Pilih puskesmas:")
    for nomor, puskesmas in enumerate(PUSKESMAS_TERSEDIA, start=1):
        print(f"{nomor}. {puskesmas}")
    pilihan = input_angka("Pilihan puskesmas (1-3): ", 1, len(PUSKESMAS_TERSEDIA))
    return PUSKESMAS_TERSEDIA[pilihan - 1]


def input_berat(prompt):
    """Meminta berat badan dalam rentang kilogram yang masuk akal."""
    while True:
        try:
            nilai = float(input(prompt).replace(",", "."))
        except ValueError:
            print("Masukkan berat dalam kilogram, misalnya 65.5.")
            continue

        if 2 <= nilai <= 300:
            return nilai
        print("Berat harus antara 2 dan 300 kg.")


def input_tinggi(prompt):
    """Meminta tinggi badan dalam rentang sentimeter yang masuk akal."""
    while True:
        try:
            nilai = float(input(prompt).replace(",", "."))
        except ValueError:
            print("Masukkan tinggi dalam sentimeter, misalnya 170.")
            continue

        if 50 <= nilai <= 250:
            return nilai
        print("Tinggi harus antara 50 dan 250 cm.")


def hitung_dan_tampilkan_imt(permintaan):
    """Menghitung IMT dari berat dan tinggi yang dimasukkan pengguna."""
    berat = input_berat("Berat badan (kg): ")
    tinggi_cm = input_tinggi("Tinggi badan (cm): ")
    imt = berat / (tinggi_cm / 100) ** 2
    permintaan["imt"] = {
        "berat_kg": berat,
        "tinggi_cm": tinggi_cm,
        "nilai": imt,
    }
    print(f"IMT Anda: {imt:.1f}")
    print("IMT adalah indikator sederhana, bukan diagnosis medis.")
    print("Konsultasikan hasilnya dengan tenaga kesehatan untuk interpretasi.")


def jalankan_survei_kesehatan(permintaan):
    """Mengumpulkan jawaban survei kebiasaan umum untuk sesi ini."""
    jawaban = []
    print("\nJawab 1 untuk Ya atau 2 untuk Tidak.")
    for pertanyaan in PERTANYAAN_SURVEI:
        print(pertanyaan)
        jawaban.append(input_angka("Jawaban (1-2): ", 1, 2))

    permintaan["survey"] = jawaban
    print("\n=== HASIL SURVEI KESEHATAN ===")
    print(f"Jawaban Ya: {jawaban.count(1)} dari {len(PERTANYAAN_SURVEI)}")
    print("Survei ini untuk refleksi kebiasaan dan bukan pemeriksaan medis.")


def tampilkan_status(permintaan):
    """Menampilkan janji dan permintaan konsultasi dalam sesi ini."""
    print("\n=== STATUS PERMINTAAN CKG ===")
    if not permintaan["janji"] and not permintaan["rujukan"]:
        print("Belum ada janji atau permintaan konsultasi.")
        return

    for nomor, janji in enumerate(permintaan["janji"], start=1):
        print(
            f"Janji {nomor}: {janji['puskesmas']} | "
            f"{janji['tanggal']} | Status: {janji['status']}"
        )

    for nomor, rujukan in enumerate(permintaan["rujukan"], start=1):
        print(
            f"Permintaan konsultasi {nomor}: {rujukan['keluhan']} | "
            f"Tujuan: {rujukan['tujuan']} | Status: {rujukan['status']}"
        )


def jalankan_menu_ckg(mahasiswa, permintaan):
    """Menjalankan menu CKG lokal; tidak menghubungi fasilitas kesehatan."""
    while True:
        tampilkan_judul()
        print("\n=== LAYANAN CKG ===")
        print(f"Mahasiswa: {mahasiswa['nama']} ({mahasiswa['nim']})")
        print("1. Catat janji CKG dengan puskesmas")
        print("2. Catat permintaan konsultasi rujukan")
        print("3. Lihat status janji dan permintaan")
        print("4. Hitung Indeks Massa Tubuh (IMT)")
        print("5. Isi survei kesehatan")
        print("6. Informasi CKG")
        print("7. Kembali ke menu utama")
        pilihan = input_angka("Pilih menu CKG (1-7): ", 1, 7)

        if pilihan == 1:
            puskesmas = pilih_puskesmas()
            tanggal = input_teks_wajib(
                "Tanggal yang diinginkan (contoh: 25-12-2026): "
            )
            permintaan["janji"].append(
                {
                    "puskesmas": puskesmas,
                    "tanggal": tanggal,
                    "status": "Belum dikonfirmasi",
                }
            )
            print(
                "Rencana janji dicatat di aplikasi. "
                "Hubungi puskesmas untuk membuat janji resmi."
            )
        elif pilihan == 2:
            keluhan = input_teks_wajib(
                "Topik yang ingin dikonsultasikan (tanpa detail sensitif): "
            )
            tujuan = pilih_puskesmas()
            permintaan["rujukan"].append(
                {
                    "keluhan": keluhan,
                    "tujuan": tujuan,
                    "status": "Menunggu konsultasi tenaga kesehatan",
                }
            )
            print(
                "Permintaan konsultasi dicatat di aplikasi. "
                "Rujukan resmi hanya dapat ditentukan oleh tenaga kesehatan."
            )
        elif pilihan == 3:
            tampilkan_status(permintaan)
        elif pilihan == 4:
            hitung_dan_tampilkan_imt(permintaan)
        elif pilihan == 5:
            jalankan_survei_kesehatan(permintaan)
        elif pilihan == 6:
            print(
                "\nCKG adalah pemeriksaan kesehatan gratis. "
                "Informasi syarat, jadwal, dan layanan dapat berbeda menurut "
                "wilayah; tanyakan langsung kepada puskesmas atau fasilitas "
                "kesehatan setempat. Menu ini tidak mengirim pendaftaran."
            )
        else:
            return