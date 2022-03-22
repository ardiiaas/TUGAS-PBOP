# 5210411205_ASRIL LINTANG ARDIAS
# Implementasi Overloading

class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def tampilMhs(self):
        print("Nama : ", self.nama, ", NIM : ",self.nim)

    def hitungSKS(self, jumlahsks=None, sks=None):
        if jumlahsks !=None and sks!=None:
            totalsks = jumlahsks+sks
            print("Total sks = ", totalsks)
        else:
            totalsks = jumlahsks
            print("Total sks = ",totalsks)

mhs1 = Mahasiswa("Asril", 1111111111)
mhs2 = Mahasiswa("Ardias", 222222222)
mhs1.tampilMhs()
mhs1.hitungSKS(80,40)# overloading
mhs2.tampilMhs()
mhs2.hitungSKS(85)# overloading