#5210411205_ASRIL LINTANG ARDIAS

class buku:
    def __init__(self,judul,pengarang,tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit

bk1 = buku("Tenggelamnya Kapal Van Der Wijck","Hamka",1938)
bk2 = buku("The God Father","Mario Puzo",1969)
bk3 = buku("Dilan : Dia adalah Dilanku tahun 1990","Paidi Baiq",2014)

daftar_buku = [bk1,bk2,bk3]
for Buku in daftar_buku:
    Buku = ("Buku {} karangan {} pertama kali diterbitkan pada tahun {}".format(Buku.judul,Buku.pengarang,Buku.tahun_terbit))
    print(Buku)
