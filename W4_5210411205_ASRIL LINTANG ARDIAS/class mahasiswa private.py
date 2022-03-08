#5210411205_ASRIL LINTANG ARDIAS
# variabel bersifat private

class mahasiswa:
    def __init__(self,nama,nim,prodi,tahun_masuk):
        self.__nama = nama
        self.__nim = nim
        self.__prodi = prodi
        self.__tahun = tahun_masuk
    def tampilkan_mhs(self):
        print(f'\nNama \t: {self.__nama}')
        print(f'NIM \t: {self.__nim}')
        print(f'Prodi \t: {self.__prodi}')
        print(f'Tahun \t: {self.__tahun}')

# Daftar Objek
mhs1 = mahasiswa('Udin','5210411050','Informatika',2021)
mhs2 = mahasiswa('Peter','5190411459','Sistem Informasi',2019)
mhs3 = mahasiswa('Brian','5200411145','Teknik Sipil',2020)

# Menampilkan Objek
mhs = [mhs1,mhs2,mhs3]
print("="*10,"DAFTAR MAHASISWA","="*10)
for data in mhs:
    data.tampilkan_mhs()
