# 5210411205_ASRIL LINTANG ARDIAS
# Implementasi Overriding

class Mahasiswa:
    def __init__(self, nama, nim):
            self.nama = nama
            self.nim = nim

    def tampilMhs(self):
        print(f'Nama : {self.nama}')
        print(f'NIM  : {self.nim}')

    # method overloading
    def hitungSks(self, jmlsks = None, sks = None):
        if jmlsks != None and sks != None:
            totalsks = jmlsks + sks
            print("Total SKS = ", totalsks)
        else:
            totalsks = jmlsks
            print("Total SKS = ", totalsks)

class Mahasiswa2(Mahasiswa):
    def __init__(self, nama, nim):
            self.nama = nama
            self.nim = nim

    def tampilMhs(self):
        print(f'Nama : {self.nama}')
        print(f'NIM  : {self.nim}')

# memanggil class
mhs1 = Mahasiswa("Asril", 5210411205)
mhs2 = Mahasiswa2("Farhan", 5210411219)

mhs1.tampilMhs()
mhs2.tampilMhs()