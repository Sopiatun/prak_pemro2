# Import pustaka random untuk menghasilkan angka acak
import random

# Mendefinisikan kelas TebakAngkaGame untuk game Numero Uno
class TebakAngkaGame:
    # Konstruktor kelas, memerlukan nama pemain untuk inisialisasi objek game
    def __init__(self, nama):
        # Inisialisasi nama pemain
        self.nama = nama
        # Inisialisasi skor awal pemain
        self.score = 0
        # Batas maksimal angka yang akan digunakan dalam permainan (default 100)
        self.max_number = 100

    # Fungsi untuk memilih level kesulitan permainan
    def pilih_level(self):
        # Menampilkan pilihan level kesulitan kepada pemain
        print("\nPilih level kesulitan:")
        print("1. Easy (Tebakan Angka dari 1–25)")
        print("2. Medium (Tebakan Angka dari 1–50)")
        print("3. Hard (Tebakan Angka dari 1–100)")
        
        # Loop untuk mendapatkan input level yang valid dari pemain
        while True:
            # Meminta input level dari pemain
            level = input("Masukkan level yang diinginkan (1/2/3): ")
            # Jika level yang dipilih adalah 1, atur batas angka maksimum menjadi 25
            if level == "1":
                self.max_number = 25
                break
            # Jika level yang dipilih adalah 2, atur batas angka maksimum menjadi 50
            elif level == "2":
                self.max_number = 50
                break
            # Jika level yang dipilih adalah 3, atur batas angka maksimum menjadi 100
            elif level == "3":
                self.max_number = 100
                break
            # Jika input tidak valid, beri tahu pemain untuk memilih level yang tersedia
            else:
                print("Pilihan tidak valid. Silakan pilih level yang tersedia.")
        
        # Memberi tahu pemain tentang level yang dipilih dan batas angka yang akan ditebak
        print(f"\nLevel {['Easy', 'Medium', 'Hard'][int(level) - 1]} dipilih! Angka rahasia berada antara 1 dan {self.max_number}.")

    # Fungsi untuk menampilkan menu utama permainan
    def tampilkan_menu(self):
        print("\nMenu:")
        print("1. Mulai permainan")
        print("2. Lihat skor")
        print("3. Keluar")

    # Fungsi utama untuk menjalankan permainan tebak angka
    def mulai_permainan(self):
        # Menghasilkan angka rahasia secara acak dalam rentang yang telah ditentukan
        angka_rahasia = random.randint(1, self.max_number)
        # Menentukan jumlah kesempatan awal yang diberikan kepada pemain
        kesempatan = 5
        # Skor maksimal pada giliran pertama
        skor_giliran = 100  
        print(f"\nSaya sudah memilih angka antara 1 hingga {self.max_number}.")
        
        # Variabel untuk menghitung giliran pemain
        giliran = 1  
        # Loop yang berjalan selama pemain masih memiliki kesempatan
        while kesempatan > 0:
            # Jika giliran terakhir, tawarkan petunjuk
            if giliran == 5:
                # Menanyakan apakah pemain ingin menggunakan petunjuk
                gunakan_clue = input("Apakah Anda ingin menggunakan petunjuk terakhir? (y/n): ").lower()
                if gunakan_clue == 'y':
                    # Jika petunjuk digunakan, kurangi skor giliran sebesar 15 poin
                    skor_giliran -= 15
                    # Mengatur batas bawah dan atas untuk petunjuk
                    lower_bound = max(1, angka_rahasia - 5)
                    upper_bound = min(self.max_number, angka_rahasia + 5)
                    # Menampilkan petunjuk kepada pemain
                    print(f"Petunjuk: Angka yang benar berada antara {lower_bound} hingga {upper_bound}.")
                    print("Skor dikurangi -15 poin karena ini giliran terakhir dan kamu menggunakan petunjuk.")
                else:
                    # Jika petunjuk tidak digunakan, hanya kurangi skor sebesar 10 poin
                    skor_giliran -= 10
                    print("Skor dikurangi -10 poin karena ini giliran terakhir tanpa menggunakan petunjuk.")

            # Meminta pemain memasukkan tebakan
            try:
                tebakan = int(input("Masukkan tebakanmu: "))
            except ValueError:
                # Menampilkan pesan jika pemain tidak memasukkan angka yang valid
                print("Harap masukkan angka yang valid.")
                continue
            
            # Jika tebakan benar, tampilkan pesan sukses dan tambahkan skor
            if tebakan == angka_rahasia:
                print("Selamat! Kamu berhasil menebak angka dengan benar!")
                self.score += skor_giliran  # Tambahkan skor sesuai giliran
                break
            else:
                # Memberi petunjuk apakah angka rahasia lebih besar atau lebih kecil dari tebakan
                if tebakan < angka_rahasia:
                    print("Angka yang benar lebih besar!")
                else:
                    print("Angka yang benar lebih kecil!")
                
                # Pemberitahuan pengurangan skor sesuai giliran
                if giliran == 2:
                    skor_giliran -= 10
                    print("Skor dikurangi -10 poin untuk giliran ke-2.")
                elif giliran == 3:
                    skor_giliran -= 20
                    print("Skor dikurangi -20 poin untuk giliran ke-3.")
                elif giliran == 4:
                    skor_giliran -= 40
                    print("Skor dikurangi -40 poin untuk giliran ke-4.")
                
                # Mengurangi kesempatan pemain
                kesempatan -= 1
                # Naikkan giliran setiap tebakan salah
                giliran += 1  

                # Menampilkan jumlah kesempatan tersisa kepada pemain
                print(f"Kesempatan tersisa: {kesempatan}")

        # Menampilkan pesan jika pemain kehabisan kesempatan tanpa menebak angka dengan benar
        if kesempatan == 0 and tebakan != angka_rahasia:
            print(f"Maaf, kamu kehabisan kesempatan. Angka yang benar adalah {angka_rahasia}.")
        
        # Menampilkan skor akhir setelah permainan selesai
        print(f"\nSkor akhir kamu dalam permainan ini: {self.score}")

    # Fungsi untuk menampilkan skor saat ini
    def lihat_skor(self):
        print(f"\nSkor saat ini: {self.score}")

    # Fungsi utama untuk mengelola loop permainan
    def mainkan(self):
        # Menyapa pemain dengan namanya
        print(f"Selamat datang, {self.nama}!")
        
        # Loop menu utama permainan
        while True:
            # Menampilkan menu kepada pemain
            self.tampilkan_menu()
            # Meminta pemain memilih opsi menu
            pilihan = input("Pilih opsi (1/2/3): ")
            
            # Jika pemain memilih untuk mulai permainan
            if pilihan == "1":
                self.pilih_level()  # Memilih level kesulitan
                self.mulai_permainan()  # Memulai permainan
            # Jika pemain memilih untuk melihat skor
            elif pilihan == "2":
                self.lihat_skor()
            # Jika pemain memilih untuk keluar
            elif pilihan == "3":
                print("\nTerima kasih telah bermain!")
                # Menampilkan skor akhir sebelum keluar
                print(f"Skor akhir: {self.score}")
                break
            # Jika input tidak valid, beri pesan kepada pemain
            else:
                print("Pilihan tidak valid. Silakan pilih opsi yang tersedia.")

# Inisialisasi dan mulai permainan jika file ini dijalankan sebagai program utama
if __name__ == "__main__":
    # Meminta nama pemain saat permainan dimulai
    nama = input("Masukkan nama pemain: ")
    # Membuat objek game dengan nama pemain
    game = TebakAngkaGame(nama)
    # Memulai loop utama permainan
    game.mainkan()
