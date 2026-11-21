"""Menu dan fitur pencatatan kesehatan mahasiswa."""

from data import input_angka, input_jam_tidur, input_teks_wajib, tampilkan_judul
from ckg import jalankan_menu_ckg


TIPS_KESEHATAN = (
    "Bergerak atau berjalan kaki setidaknya 30 menit setiap hari.",
    "Minum air secara berkala; kebutuhan tiap orang dapat berbeda.",
    "Usahakan tidur cukup dan jaga jadwal tidur tetap teratur.",
    "Pilih makanan bergizi dan jangan melewatkan waktu makan.",
    "Atur waktu belajar, istirahat, dan penggunaan layar.",
    "Jika merasa tidak sehat, hubungi tenaga kesehatan atau layanan kampus.",
)


def tampilkan_ringkasan(mahasiswa, catatan):
    """Menampilkan profil dan catatan kesehatan selama sesi ini."""
    total_aktivitas = sum(item["menit"] for item in catatan["aktivitas"])
    print("\n=== RINGKASAN KESEHATAN ===")
    print(f"Mahasiswa : {mahasiswa['nama']} ({mahasiswa['nim']})")
    print(f"Prodi     : {mahasiswa['prodi']}")
    print(f"Aktivitas : {total_aktivitas} menit")
    print(f"Air       : {catatan['air_ml']} ml")

    if catatan["tidur_jam"] is None:
        print("Tidur     : Belum dicatat")
    else:
        print(f"Tidur     : {catatan['tidur_jam']:g} jam")

    if catatan["aktivitas"]:
        print("Rincian aktivitas:")
        for item in catatan["aktivitas"]:
            print(f"- {item['nama']}: {item['menit']} menit")
    else:
        print("Rincian aktivitas: Belum ada catatan")

    print("Catatan ini hanya tersimpan selama aplikasi berjalan.")


def jalankan_menu(mahasiswa, catatan):
    """Menjalankan menu fitur kesehatan hingga pengguna memilih keluar."""
    while True:
        tampilkan_judul()
        print("\n=== SEHAT MAHASISWA ===")
        print(f"Halo, {mahasiswa['nama']} | {mahasiswa['prodi']}")
        print("1. Catat aktivitas fisik")
        print("2. Catat konsumsi air")
        print("3. Catat durasi tidur")
        print("4. Lihat tips kesehatan")
        print("5. Lihat ringkasan kesehatan")
        print("6. Layanan CKG")
        print("7. Logout dan keluar")
        pilihan = input_angka("Pilih menu (1-7): ", 1, 7)

        if pilihan == 1:
            nama_aktivitas = input_teks_wajib("Jenis aktivitas (contoh: jalan kaki): ")
            menit = input_angka("Durasi aktivitas (menit, 1-600): ", 1, 600)
            catatan["aktivitas"].append(
                {"nama": nama_aktivitas, "menit": menit}
            )
            print("Aktivitas berhasil dicatat.")
        elif pilihan == 2:
            jumlah = input_angka("Jumlah air yang diminum (ml, 1-5000): ", 1, 5000)
            catatan["air_ml"] += jumlah
            print(f"Konsumsi air berhasil dicatat. Total sesi: {catatan['air_ml']} ml.")
        elif pilihan == 3:
            catatan["tidur_jam"] = input_jam_tidur(
                "Durasi tidur terakhir dalam jam (contoh: 7.5): "
            )
            print("Durasi tidur berhasil dicatat.")
        elif pilihan == 4:
            print("\n=== TIPS KESEHATAN ===")
            for nomor, tip in enumerate(TIPS_KESEHATAN, start=1):
                print(f"{nomor}. {tip}")
        elif pilihan == 5:
            tampilkan_ringkasan(mahasiswa, catatan)
        elif pilihan == 6:
            jalankan_menu_ckg(mahasiswa, catatan["ckg"])
        else:
            print(f"Logout berhasil. Sampai jumpa dan tetap sehat, {mahasiswa['nama']}!")
            return