# 5210411205_ASRIL LINTANG ARDIAS
# Single Inheritance

# Parent Class
class hewan:
    def bersuara(self):
        print("Kucin Bersuara ")

# Child class mewarisi dari class hewan
class kucing(hewan):
    def suara(self):
        print('meong')

# Objek
k=kucing()
k.suara()
k.bersuara()