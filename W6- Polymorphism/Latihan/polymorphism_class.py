# 5210411205_ASRIL LINTANG ARDIAS
# Polymorphism dengan class

class Kucing:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bersuara(self):
        print("Meong...meong...")

class Anjing:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def bersuara(self):
        print("Guk...Guk...")

kucing1 = Kucing("Marry", 3)
anjing1 = Anjing("Gerry", 4)

for hewan in (kucing1, anjing1):
    hewan.bersuara()