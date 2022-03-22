# 5210411205_ASRIL LINTANG ARDIAS
# Implementasi Overriding

class SegiEmpat():
    def __init__(self, panjang, lebar):
            self.panjang = panjang
            self.lebar = lebar

    def hitungLuas(self): # method overriding
        print("Luas Segi empat : ", self.panjang * self.lebar , "m2")

class BujurSangkar(SegiEmpat):
    def __init__(self, sisi):
            self.side = sisi
            SegiEmpat.__init__(self, sisi, sisi)

    def hitungLuas(self): # method overriding
        print("Luas Bujur sangkar : ", self.side * self.side , "m2")

B = BujurSangkar(4)
S = SegiEmpat(6,8)
B.hitungLuas()
S.hitungLuas()