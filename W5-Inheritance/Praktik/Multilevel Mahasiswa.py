# 5210411205_ASRIL LINTANG ARDIAS
# Multilevel Inheritance

class Mahasiswa():
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

class Siswa1(Mahasiswa):
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

class Siswa2(Siswa1):
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim


mhs1 = Mahasiswa('Asril', 5210411205)
mhs2 = Siswa1('Dian', 5210411245)
mhs3 = Siswa2('Riski',5210411499)

print(mhs1.nama , mhs1.nim)
print(mhs2.nama)
print(mhs3.nim)