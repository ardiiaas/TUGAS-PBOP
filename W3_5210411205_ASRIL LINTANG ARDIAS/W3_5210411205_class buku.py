class buku:
    def __init__(self,judul,pengarang,tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
Buku = buku("Tenggelamnya Kapal Van Der Wijck","Hamka",1938)
x = ("Buku {} karangan {} pertama kali diterbitkan tahun {}".format(Buku.judul,Buku.pengarang,Buku.tahun_terbit))
print(x)