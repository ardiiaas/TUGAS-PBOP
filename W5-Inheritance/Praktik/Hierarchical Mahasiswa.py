# 5210411205_ASRIL LINTANG ARDIAS
# Hierarchical Inheritance

class Mahasiswa():
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

class Siswa1(Mahasiswa):
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def detSiswa1(self):
        print(self.nama, 'alamat : Banjarnegara')

class Siswa2(Mahasiswa):
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def detSiswa2(self):
        print(self.nama, 'jurusan : Informatika')

mhs1 = Siswa1('Asril', 5210411205)
mhs2 = Siswa2('Dian',5210411245)

print(mhs1.nim)
mhs1.detSiswa1()

print(mhs2.nama)
mhs2.detSiswa2()