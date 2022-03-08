# 5210411205_ASRIL LINTANG ARDIAS
# variabel bersifat public

class segitiga:
    def __init__(self,alas,tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0.5 * alas * tinggi

#Akses variabel publik: alas, tinggi dan luas segitiga dari luar kelas segitiga
segitiga_A = segitiga(80,50)
print("Alas \t: ",segitiga_A.alas)
print("Tinggi \t: ",segitiga_A.tinggi)
print("Luas \t: ",segitiga_A.luas)