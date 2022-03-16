# 5210411205_ASRIL LINTANG ARDIAS
# Single Inheritance

class Mahasiswa:
    def __init__(self,nama,nim):
        self.nama = nama
        self.nim = nim

    def detail_mhs(self):
        return self.nama, self.nim

    def cek_mhs(self):
        if self.nim < 140000:
            return "Mahasiswa Aktif"
        else:
            return "Mahasiswa Tidak Terdaftar"

class Siswa(Mahasiswa):
    def End(self):
        print("Mahasiswa belum melakukan daftar ulang")

mhs1 = Mahasiswa("Mahasiswa 1 ", 135000)
mhs2 = Mahasiswa("Mahasiswa 2 ", 142400)

print(mhs1.detail_mhs(), mhs1.cek_mhs())
print(mhs2.detail_mhs(), mhs2.cek_mhs())