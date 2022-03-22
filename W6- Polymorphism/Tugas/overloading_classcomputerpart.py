# 5210411205_ASRIL LINTANG ARDIAS
# Implementasi Overloading di class computerpart

class ComputerPart:
    def __init__(self,pabrikan, nama, jenis, harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.jenis = jenis
        self.harga = harga

class Processor(ComputerPart):
    def __init__(self,pabrikan,nama,harga,jumlahCore):
        super().__init__(pabrikan, nama, "Processor", harga)
        self.jumlahCore = jumlahCore

    #overloading
    def kecepatanProcessor(self, speed):
        if(speed >= 3):
            print("Kecepatan Processor sangat cepat")
        else :
            print("Kecepatan processor normal")

class RAM(ComputerPart):
    def __init__(self,pabrikan, nama, harga, kapasitas):
        super().__init__(pabrikan,nama,"RAM",harga)
        self.kapasitas = kapasitas

    #overloading
    def totalHarga(self, jumlah):
        total = self.harga * jumlah
        print('Total harga :', total)

class SSD(ComputerPart):
    def __init__(self, pabrikan, nama, harga, read_write):
        super().__init__(pabrikan, nama, "SSD", harga)
        self.read_write = read_write

    #overloading
    def kapasitasPenyimpanan(self, kapasitas):
        if(kapasitas >= 500):
            print("Penyimpanannya Banyak")
        else:
            print("Penyimpanannya Kurang")

processor = Processor('Intel', 'Core i5 8520', 2500000, 8)
ram = RAM('V-Gen', 'DDR4 SODimm 2400Mhz', 380000, '8GB')
ssd = SSD('Seagate', 'HDD 2,5 Inch', 290000,7200)

print("\n---------------------------------------------------------------------------------")
print("\t\t\tPart Komputer Overriding")
print("---------------------------------------------------------------------------------")
parts = [processor]
for part in parts:
    print(f'\n{part.jenis} {part.nama} Produksi {part.pabrikan} :')
    processor.kecepatanProcessor(4)
parts = [ram]
for part in parts:
    print(f'\n{part.jenis} {part.nama} Produksi {part.pabrikan}:')
    ram.totalHarga(2)

parts = [ssd]
for part in parts:
    print(f'\n{part.jenis} {part.nama} Produksi {part.pabrikan}:')
    ssd.kapasitasPenyimpanan(1000)
print("\n---------------------------------------------------------------------------------")