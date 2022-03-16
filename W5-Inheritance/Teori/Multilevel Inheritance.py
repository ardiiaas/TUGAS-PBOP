# 5210411205_ASRIL LINTANG ARDIAS
# Multilevel Inheritance

# Parent Class
class hewan:
    def bersuara(self):
        print("Kucing Bersuara ")

# child class mewarisi dari class hewan
class kucing(hewan):
    def suara(self):
        print('meong...meong')

# child class AnakKucing mewarisi class kucing
class AnakKucing(kucing):
    def minum(self):
        print('minum susu')

k = AnakKucing()
k.bersuara()
k.suara()
k.minum()