# 5210411205_ASRIL LINTANG ARDIAS
# variabel bersifat private

class pegawai:
    __nama=""
    __alamat=""
    __gaji=0

    def __init__(self,nama,alamat):
        self.__nama=nama
        self.__alamat=alamat
    def __hitunggaji(self):
        upahlembur=25000
        gajipokok=3000000
        jmlhlembur=int(input("\nTotal Jam Lembur : "))
        self.__gaji=(upahlembur*jmlhlembur)+gajipokok
    def tampildetail(self):
        print("\n--Menghitung dan menampilkan detail gaji pegawai--")
        print("Nama \t: ",self.__nama)
        print("Alamat \t:",self.__alamat)
        self.__hitunggaji()
        print("\nTotal Gaji : Rp.",self.__gaji)

pgw1 = pegawai("Tom Cruise","jl.Washington DC no.24, Bandung")
pgw2 = pegawai("Peter Parker","jl.Jendral Ahmad Yani no 9, Karawang")
pgw1.tampildetail()
pgw2.tampildetail()