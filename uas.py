import random

# Kelas untuk merepresentasikan pemain
class Pemain:
    def _init_(self, nama):
        self.nama = nama
        self.score = 0

    # Fungsi untuk menambah skor pemain
    def tambah_skor(self, skor):
        self.score += skor

    # Fungsi untuk menampilkan skor saat ini
    def tampilkan_skor(self):
        print(f"\nSkor saat ini untuk {self.nama}: {self.score}")


# Kelas untuk logika permainan
class TebakAngkaGame:
    def _init_(self, pemain):
        self.pemain = pemain
        self.max_number = 100

    # Fungsi untuk memilih level kesulitan permainan
    def pilih_level(self):
        print("\nPilih level kesulitan:")
        print("1. Easy (Tebakan Angka dari 1-25)")
        print("2. Medium (Tebakan Angka dari 1-50)")
        print("3. Hard (Tebakan Angka dari 1-100)")
        
        while True:
            level = input("Masukkan level yang diinginkan (1/2/3): ")
            if level == "1":
                self.max_number = 25
                break
            elif level == "2":
                self.max_number = 50
                break
            elif level == "3":
                self.max_number = 100
                break
            else:
                print("Pilihan tidak valid. Silakan pilih level yang tersedia.")
        
        print(f"\nLevel {['Easy', 'Medium', 'Hard'][int(level) - 1]} dipilih! Angka rahasia berada antara 1 dan {self.max_number}.")

    # Fungsi utama untuk menjalankan permainan tebak angka
    def mulai_permainan(self):
        angka_rahasia = random.randint(1, self.max_number)
        kesempatan = 5
        skor_giliran = 100
        print(f"\nSaya sudah memilih angka antara 1 hingga {self.max_number}.")
        
        giliran = 1
        while kesempatan > 0:
            if giliran == 5:
                gunakan_clue = input("Apakah Anda ingin menggunakan petunjuk terakhir? (y/n): ").lower()
                if gunakan_clue == 'y':
                    skor_giliran -= 15
                    lower_bound = max(1, angka_rahasia - 5)
                    upper_bound = min(self.max_number, angka_rahasia + 5)
                    print(f"Petunjuk: Angka yang benar berada antara {lower_bound} hingga {upper_bound}.")
                    print("Skor dikurangi -15 poin karena ini giliran terakhir dan kamu menggunakan petunjuk.")
                else:
                    skor_giliran -= 10
                    print("Skor dikurangi -10 poin karena ini giliran terakhir tanpa menggunakan petunjuk.")

            try:
                tebakan = int(input("Masukkan tebakanmu: "))
            except ValueError:
                print("Harap masukkan angka yang valid.")
                continue
            
            if tebakan == angka_rahasia:
                print("Selamat! Kamu berhasil menebak angka dengan benar!")
                self.pemain.tambah_skor(skor_giliran)
                break
            else:
                if tebakan < angka_rahasia:
                    print("Angka yang benar lebih besar!")
                else:
                    print("Angka yang benar lebih kecil!")
                
                if giliran == 2:
                    skor_giliran -= 10
                    print("Skor dikurangi -10 poin untuk giliran ke-2.")
                elif giliran == 3:
                    skor_giliran -= 20
                    print("Skor dikurangi -20 poin untuk giliran ke-3.")
                elif giliran == 4:
                    skor_giliran -= 40
                    print("Skor dikurangi -40 poin untuk giliran ke-4.")
                
                kesempatan -= 1
                giliran += 1
                print(f"Kesempatan tersisa: {kesempatan}")

        if kesempatan == 0 and tebakan != angka_rahasia:
            print(f"Maaf, kamu kehabisan kesempatan. Angka yang benar adalah {angka_rahasia}.")
        
        print(f"\nSkor akhir kamu dalam permainan ini: {self.pemain.score}")

    # Fungsi untuk menampilkan skor saat ini
    def lihat_skor(self):
        self.pemain.tampilkan_skor()

    # Fungsi utama untuk mengelola loop permainan
    def mainkan(self):
        print(f"Selamat datang, {self.pemain.nama}!")
        
        while True:
            print("\nMenu:")
            print("1. Mulai permainan")
            print("2. Lihat skor")
            print("3. Keluar")
            pilihan = input("Pilih opsi (1/2/3): ")
            
            if pilihan == "1":
                self.pilih_level()
                self.mulai_permainan()
            elif pilihan == "2":
                self.lihat_skor()
            elif pilihan == "3":
                print("\nTerima kasih telah bermain!")
                print(f"Skor akhir: {self.pemain.score}")
                break
            else:
                print("Pilihan tidak valid. Silakan pilih opsi yang tersedia.")


# Inisialisasi dan mulai permainan jika file ini dijalankan sebagai program utama
if _name_ == "_main_":
    nama = input("Masukkan nama pemain: ")
    pemain = Pemain(nama)  # Membuat objek pemain
    game = TebakAngkaGame(pemain)  # Membuat objek game dengan pemain
    game.mainkan()
