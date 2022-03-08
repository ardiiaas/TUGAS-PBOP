# 5210411205_ ASRIL LINTANG ARDIAS
# Variabel bersifat Public

class mobil:
    def __init__(self,kapasitas_mesin,pintu,bahan_bakar):
        self.kapasitas_mesin = kapasitas_mesin
        self.pintu = pintu
        self.bahan_bakar = bahan_bakar
innova = mobil(3000,4,"Dexlite")
print(innova.kapasitas_mesin)
print(innova.pintu)
print(innova.bahan_bakar)