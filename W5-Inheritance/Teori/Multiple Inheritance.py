# 5210411205_ASRIL LINTANG ARDIAS
# Multiple Inheritance

# Parent 1
class Perhitungan1:
    def penjumlahan(self, a, b):
        return a+b

# Parent 2
class Perhitungan2:
    def perkalian(self, a ,b):
        return a*b

# Child
class Hitung(Perhitungan1, Perhitungan2):
    def pembagian(self, a, b):
        return a/b

H = Hitung()

print(H.penjumlahan(66, 77))
print(H.pembagian(300, 25))
print(H.perkalian(43, 17))