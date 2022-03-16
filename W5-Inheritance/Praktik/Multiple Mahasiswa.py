# 5210411205_ASRIL LINTANG ARDIAS
# Multiple Inheritance

class Mahasiswa1():
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

class Mahasiswa2():
    def __init__(self, alamat, jurusan):
        self.alamat = alamat
        self.jurusan = jurusan

class Siswa(Mahasiswa1, Mahasiswa2):
    def __init__(self, nama, nim, alamat, jurusan):
        Mahasiswa1.__init__(self, nama, nim)
        Mahasiswa2.__init__(self,alamat, jurusan)

mhs = Siswa('Asril',5210411205,'Banjarnegara','Informatika')

print(f'NIM \t: {mhs.nim}')
print(f'Nama \t: {mhs.nama}')
print(f'Tahun \t: {mhs.alamat}')
print(f'Prodi \t: {mhs.jurusan}')