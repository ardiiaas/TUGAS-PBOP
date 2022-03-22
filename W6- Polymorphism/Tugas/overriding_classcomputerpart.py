# 5210411205_ASRIL LINTANG ARDIAS
# Implementasi Overriding di class computerpart

class ComputerPart:
    def __init__(self,pabrikan, nama, jenis, harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.jenis = jenis
        self.harga = harga

class Processor(ComputerPart):
    def __init__(self,pabrikan,nama,harga,jumlahCore, speed):
        super().__init__(pabrikan, nama, "Processor", harga)
        self.jumlahCore = jumlahCore
        self.speed = speed
    # Overriding
    def Tampil(self):
        print("\nTampil dari sub class Processor")
        print(f'Pabrikan \t: {self.pabrikan}')
        print(f'Nama \t\t: {self.nama}')
        print(f'Jumlah Core \t: {self.jumlahCore}')
        print(f'Speed \t\t: {self.speed}')
        print(f'Harga \t\t: Rp.{self.harga}')

class RAM(ComputerPart):
    def __init__(self,pabrikan, nama, harga, kapasitas):
        super().__init__(pabrikan,nama,"RAM",harga)
        self.kapasitas = kapasitas
    # Overriding
    def Tampil(self):
        print("\nTampil dari sub class RAM")
        print(f'Pabrikan \t: {self.pabrikan}')
        print(f'Nama \t\t: {self.nama}')
        print(f'Kapasitas \t: {self.kapasitas}')
        print(f'Harga \t\t: Rp.{self.harga}')

class SSD(ComputerPart):
    def __init__(self, pabrikan, nama, harga,  kapasitas, read_write):
        super().__init__(pabrikan, nama, "SSD", harga)
        self.kapasitas = kapasitas
        self.read_write = read_write
    # Overriding
    def Tampil(self):
        print("\nTampil dari sub class SSD")
        print(f'Pabrikan \t: {self.pabrikan}')
        print(f'Nama \t\t: {self.nama}')
        print(f'Kapasitas \t: {self.kapasitas}')
        print(f'Read/Write \t: {self.read_write}')
        print(f'Harga \t\t: Rp.{self.harga}\n')

# Object
processor = Processor('Intel', 'Core i9 12900K',9300000,'16 Core','5.20 GHz')
ram = RAM('Vgen','DDR4 SODimm PC 19200/2400MHz',560000,'8GB')
ssd = SSD('Samsung','980 PRO PCIe 4.0 NVMe SSD',3335000,'1TB','7000/5000 MB/s')

#Menampilkan
parts = [processor,ram,ssd]
print("\n---------------------------------------------------------------------------------")
print("\t\t\tPart Komputer Overriding")
print("---------------------------------------------------------------------------------")
for part in parts :
    part.Tampil()
print("---------------------------------------------------------------------------------")
