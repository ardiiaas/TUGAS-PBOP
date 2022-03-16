# 5210411205_ASRIL LINTANG ARDIAS
# Multiple Inheritance

class ComputerPart1():
    def __init__(self, pabrikan, nama):
        self.pabrikan = pabrikan
        self.nama = nama

class ComputerPart2():
    def __init__(self, harga):
        self.harga = harga

class Processor(ComputerPart1, ComputerPart2):
    def __init__(self, pabrikan, nama, harga):
        ComputerPart1.__init__(self, pabrikan, nama)
        ComputerPart2.__init__(self, harga)

    def Tampil(self):
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"Harga : {self.harga}")


class RandomAccessMemory(ComputerPart1, ComputerPart2):
    def __init__(self, pabrikan, nama, harga):
        ComputerPart1.__init__(self, pabrikan, nama)
        ComputerPart2.__init__(self, harga)

    def Tampil(self):
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"Harga : {self.harga}")


class Solid_State_Drive(ComputerPart1, ComputerPart2):
    def __init__(self, pabrikan, nama, harga):
        ComputerPart1.__init__(self, pabrikan, nama)
        ComputerPart2.__init__(self, harga)

    def Tampil(self):
        print(f"{self.nama} produk dari {self.pabrikan}")
        print(f"Harga : {self.harga}")

# Objek
processor = Processor('Intel', 'Core i5 11400H',3400000)
ram = RandomAccessMemory('Vgen','DDR4 SODimm PC 19200/2400MHz',560000)
hdd = Solid_State_Drive('Apocalypse', 'SSD RX7', 205000)

parts = [processor, ram, hdd]
print("\n=================================================")
print("\t\t COMPUTER PART")
print("=================================================\n")
for part in parts:
    part.Tampil()
    print(" ")
print("=================================================\n")