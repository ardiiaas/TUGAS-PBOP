#5210411205_ASRIL LINTANG ARDIAS
# variabel bersifat private

class menu_minuman:
    def __init__(self,nama,deskripsi,harga):
        self.__nama = nama
        self.__deskripsi = deskripsi
        self.__harga = harga
    def tampilkan_menu(self):
        print(f'\nNama \t\t: {self.__nama}')
        print(f'Harga \t\t: Rp.{self.__harga}')
        print(f'Deskripsi \t: {self.__deskripsi}')

# Daftar Objek
minum1 = menu_minuman('Jus Jambu','Jus Jambu merah tanpa gula',8500)
minum2 = menu_minuman('Jus alpukat ori','Jus dengan tambahan air gula merah',15000)
minum3 = menu_minuman('Jus alpukat xtra milk','Jus alpukat dengan campuran susu coklat dan taburan kepingan choco',15000)
minum4 = menu_minuman('Red & Smooth','Smoothy dengan pisang susu dan strawberry',17500)
minum5 = menu_minuman('Expresso','Kopi fresh tanpa gula',20000)
minum6 = menu_minuman('Es Kelapa Muda','Dengan Campuran sirup dan susu',5000)

# Menampilkan Objek
minum1.tampilkan_menu()
minum2.tampilkan_menu()
minum3.tampilkan_menu()
minum4.tampilkan_menu()
minum5.tampilkan_menu()
minum6.tampilkan_menu()