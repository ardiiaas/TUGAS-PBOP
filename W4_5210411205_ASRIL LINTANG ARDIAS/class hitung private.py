# 5210411205_ASRIL LINTANG ARDIAS
# variabel bersifat private

class hitung:
    def __init__(self):
        self.__angkaRahasia = 0
    def tampilkanhitung(self):
        self.__angkaRahasia +=1
        print(self.__angkaRahasia)

hasil = hitung()
hasil.tampilkanhitung()