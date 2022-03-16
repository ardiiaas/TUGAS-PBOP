# 5210411205_ASRIL LINTANG ARDIAS

class Computer_Part:
    def __init__(self,pabrikan,nama,jenis,harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
class Processor(Computer_Part):
    def __init__(self,pabrikan,nama,harga,jumlah_core,speed):
        super().__init__(pabrikan,nama,'processor',harga)
        self.jumlah_core = jumlah_core
        self.speed = speed
class Random_Access_Memory(Computer_Part):
    def __init__(self,pabrikan,nama,harga,kapasitas):
        super().__init__(pabrikan, nama, 'RAM', harga)
        self.kapasitas = kapasitas
class Solid_State_Drive(Computer_Part):
    def __init__(self,pabrikan,nama,harga,kapasitas,read_write):
        super().__init__(pabrikan, nama, 'SSD', harga)
        self.kapasitas = kapasitas
        self.read_write = read_write
# Object
a = Processor('Intel','Core I9 12900K',9300000,'16 Core','5.20 GHz')
b = Random_Access_Memory('Vgen','DDR4 SODimm PC 19200/2400MHz',560000,'8GB')
c = Solid_State_Drive('Samsung','980 PRO PCIe 4.0 NVMe SSD',3335000,'1TB','7000/5000 MB/s')
parts = [a,b,c]
for part in parts:
    print('{} {} produksi {}'.format(part.jenis,part.nama,part.pabrikan))
