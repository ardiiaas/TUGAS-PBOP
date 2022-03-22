# 5210411205_ASRIL LINTANG ARDIAS
# Implementasi Overloading

class Pegawai:
    jumlah = 0

    def __init__(self,nama,gaji):
        self.nama = nama
        self.gaji = gaji
        Pegawai.jumlah += 1

    def tampilJumlah(self):
        print("Jumlah Pegawai", Pegawai.jumlah)

    def tampilPegawai(self):
        print("Nama : ",self.nama, ", Gaji : Rp.",self.gaji)

    def tunjangan(self, istri=None, anak=None):
        if anak != None and istri != None:
            total = anak + istri
            print("Tunjangan Anak + Istri =", total)
        else:
            total = istri
            print("Tunjangan istri = ", total)

peg1 = Pegawai("ardias", 3000)
peg2 = Pegawai("asril", 6000)
peg1.tampilPegawai()
peg2.tampilPegawai()
peg1.tunjangan(3000, 4000)
peg2.tunjangan(5000)

print("Total Pegawai : %d" % Pegawai.jumlah)
rataGaji =(peg1.gaji + peg2.gaji) / Pegawai.jumlah
print("Rata-rata gaji = " + str(rataGaji))