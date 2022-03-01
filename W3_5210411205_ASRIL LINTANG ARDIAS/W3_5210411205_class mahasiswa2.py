#5210411205_ASRIL LINTANG ARDIAS

class mahasiswa:
    def __init__(self,nama,nim,prodi,tahun_masuk):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.tahun_masuk = tahun_masuk
        
mhs1 = mahasiswa('Udin','5210411050','Sistem Informasi',2021)
mhs2 = mahasiswa('Alex','5180411001','Informatika',2018)
mhs3 = mahasiswa('Zidane','5200411105','Informatika',2020)

data = [mhs1,mhs2,mhs3]
for mhs in data:
    teks = '{} adalah mahasiswa {} angkatan {} dengan nim {}'.format(mhs.nama,mhs.prodi,mhs.tahun_masuk,mhs.nim)
    print(teks)
