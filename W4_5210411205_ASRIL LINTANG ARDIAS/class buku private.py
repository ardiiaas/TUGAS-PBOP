# 5210411205_ASRIL LINTANG ARDIAS
# variabel bersifatprivate

class buku:
    def __init__(self,judul,pengarang,tahun_terbit):
        self.__judul = judul
        self.__pengarang = pengarang
        self.__tahun_terbit = tahun_terbit
    def tampilkan_buku(self):
        print(f'\nJudul \t\t: {self.__judul}')
        print(f'Pengarang \t: {self.__pengarang}')
        print(f'Tahun Terbit \t: {self.__tahun_terbit}')

# Daftar Objek
bk1 = buku("Tenggelamnya Kapal Van Der Wijck","Hamka",1938)
bk2 = buku("The God Father","Mario Puzo",1969)
bk3 = buku("Dilan tahun 1990","Paidi Baiq",2014)

# Menampilkan Objek
bk = [bk1,bk2,bk3]
print("="*20,"DAFTAR BUKU","="*20)
for data in bk:
    data.tampilkan_buku()
