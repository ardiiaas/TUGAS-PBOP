# 5210411205_ASRIL LINTANG ARDIAS
# Hierarchical Inheritance

# Class induk
class induk:
    def fungsiInduk(self):
        print('Fungsi pada class induk')

# Class turunan 1
class anak1(induk):
    def fungsiAnak1(self):
        print('Fungsi pada anak pertama')

# Class turunan 2
class anak2(induk):
    def fungsiAnak2(self):
        print('Fungsi pada anak kedua')

a1 = anak1()
a2 = anak2()

a1.fungsiAnak1()
a1.fungsiInduk()

a2.fungsiAnak2()
a2.fungsiInduk()