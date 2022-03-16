# 5210411205_ASRIL LINTANG ARDIAS
# Hierarchical Inheritance

# Parent Class ComputerPart
class ComputerPart:
    def __init__(self,pabrikan, nama, jenis, harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.jenis = jenis
        self.harga = harga

# Child Class ComputerPart
class Processor(ComputerPart):
    def __init__(self,pabrikan,nama,harga,jumlahCore, speed):
        super().__init__(pabrikan, nama, "Processor", harga)
        self.jumlahCore = jumlahCore
        self.speed = speed

    def Detail_Processor(self):
        print('\n=============== Detail Processor ===============')
        print(f'Pabrikan \t: {self.pabrikan}')
        print(f'Nama \t\t: {self.nama}')
        print(f'Jumlah Core \t: {self.jumlahCore}')
        print(f'Speed \t\t: {self.speed}')
        print(f'Harga \t\t: Rp.{self.harga}')

# Child Class ComputerPart
class RAM(ComputerPart):
    def __init__(self,pabrikan, nama, harga, kapasitas):
        super().__init__(pabrikan,nama,"RAM",harga)
        self.kapasitas = kapasitas

    def Detail_RAM(self):
        print('\n================== Detail RAM ==================')
        print(f'Pabrikan \t: {self.pabrikan}')
        print(f'Nama \t\t: {self.nama}')
        print(f'Kapasitas \t: {self.kapasitas}')
        print(f'Harga \t\t: Rp.{self.harga}')

# Child Class ComputerPart
class Solid_State_Drive(ComputerPart):
    def __init__(self, pabrikan, nama, harga,  kapasitas, read_write):
        super().__init__(pabrikan, nama, "Sata", harga)
        self.kapasitas = kapasitas
        self.read_write = read_write

    def Detail_SSD(self):
        print('\n================== Detail SSD ==================')
        print(f'Pabrikan \t: {self.pabrikan}')
        print(f'Nama \t\t: {self.nama}')
        print(f'Kapasitas \t: {self.kapasitas}')
        print(f'Read/Write \t: {self.read_write}')
        print(f'Harga \t\t: Rp.{self.harga}\n')

# Object
processor = Processor('Intel', 'Core i9 12900K',9300000,'16 Core','5.20 GHz')
ram = RAM('Vgen','DDR4 SODimm PC 19200/2400MHz',560000,'8GB')
ssd = Solid_State_Drive('Samsung','980 PRO PCIe 4.0 NVMe SSD',3335000,'1TB','7000/5000 MB/s')

#Menampilkan
processor.Detail_Processor()
ram.Detail_RAM()
ssd.Detail_SSD()