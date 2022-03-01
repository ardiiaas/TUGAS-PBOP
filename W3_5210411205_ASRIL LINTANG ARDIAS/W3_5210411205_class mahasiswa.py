#5210411205_ASRIL LINTANG ARDIAS

class mahasiswa:
    def __init__(self,nama,nim,prodi,tahun_masuk):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.tahun_masuk = tahun_masuk
        
mahasiswa1 = mahasiswa('Udin','5210411050','Sistem Informasi',2021)
teks = '{} adalah mahasiswa {} angkatan {} dengan nim {}'.format(mahasiswa1.nama,mahasiswa1.prodi,mahasiswa1.tahun_masuk,mahasiswa1.nim)
print(teks)
