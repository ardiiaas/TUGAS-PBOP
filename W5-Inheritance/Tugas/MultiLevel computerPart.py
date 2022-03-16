# 5210411205_ASRIL LINTANG ARDIAS
# Multilevel Inheritance

class ComputerPart:
    def __init__(self, pabrikan, nama, harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

class Processor(ComputerPart):
    def __init__(self, pabrikan, nama, harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

    def Tampilkan(self):
        print(f"{self.nama} produk dari {self.pabrikan} dijual dengan harga Rp.{self.harga}")

class RandomAccessMemory(Processor):
    def __init__(self, pabrikan, nama, harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

    def Tampilkan(self):
        print(f"{self.nama} produk dari {self.pabrikan} dijual dengan harga Rp.{self.harga}")

class Solid_State_Drive(RandomAccessMemory):
    def __init__(self, pabrikan, nama, harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.harga = harga

    def Tampilkan(self):
        print(f"{self.nama} produk dari {self.pabrikan} dijual dengan harga Rp.{self.harga}")

# Objek
processor = Processor('Intel', 'Core i5 11400H',3400000)
ram = RandomAccessMemory('Vgen','DDR4 SODimm PC 19200/2400MHz',560000)
hdd = Solid_State_Drive('Apocalypse', 'SSD RX7', 205000)

parts = [processor, ram, hdd]
print("\n=================================================================================")
print("\t\t\t\tCOMPUTER PART")
print("=================================================================================\n")
for part in parts:
    part.Tampilkan()
    print(" ")
print("=================================================================================\n")