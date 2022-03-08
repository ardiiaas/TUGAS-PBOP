# 5210411205_ ASRIL LINTANG ARDIAS
# Variabel bersifat Private

class mobil:
    def __init__(self,merk,cc,code_mesin,HP,NM):
        self.__merk = merk
        self.__cc = cc
        self.__code = code_mesin
        self.__HP = HP
        self.__NM = NM
    def tampilkan_mobil(self):
        print(f'\nMerk \t\t: {self.__merk}')
        print(f'Kapasitas  \t: {self.__cc} CC')
        print(f'Code Mesin \t: {self.__code}')
        print(f'Tenaga \t\t: {self.__HP} HP {self.__NM} NM')

# Daftar Objek
Mobil1 = mobil('Innova',3000,'1KD FTV',450,980)
Mobil2 = mobil('Pajero Sport',2400,'4N15',180,540)
Mobil3 = mobil('Supra MK4',3000,'2JZGTE',1000,1100)

# Menampilkan Objek
Mobil = [Mobil1,Mobil2,Mobil3]
print("="*20,"DAFTAR MOBIL","="*20)
for data in Mobil:
    data.tampilkan_mobil()
