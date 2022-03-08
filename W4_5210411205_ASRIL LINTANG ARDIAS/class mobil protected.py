# 5210411205_ASRIL LINTANG ARDIAS
# Variabel bersifat Protected
class mobil:
    def __init__(self,jendela,pintu,mesin):
        self._jendela = jendela
        self._pintu = pintu
        self._mesin = mesin
class truk(mobil):
    def __init__(self,jendela,pintu,mesin,tipe):
        super().__init__(jendela,pintu,mesin)
        self._tipebak = tipe

trek = truk(4,4,"Diesel","Bak Terbuka")
print(trek._mesin)
print(trek._tipebak)

audi=mobil(4,4,"Bensin")
print(audi._mesin)