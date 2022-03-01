#5210411205_ASRIL LINTANG ARDIAS


class titik:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class garis:
    def __init__(self,titik_pertama,titik_kedua):
        self.titik_pertama = titik_pertama
        self.titik_kedua = titik_kedua
    
    def panjang(self):
        panjang_a = self.titik_kedua.x - self.titik_pertama.x
        panjang_b = self.titik_kedua.y - self.titik_pertama.y
        hasil = (panjang_a**2 + panjang_b**2) ** 0.5
        return hasil

titik_a = titik(0,0)
titik_b = titik(3,4)
garis_ab = garis(titik_a,titik_b)
print('Panjang garis ab adalah {}'.format(garis_ab.panjang()))