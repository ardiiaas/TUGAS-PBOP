#5210411205_ASRIL LINTANG ARDIAS

class menu_minuman:
    def __init__(self,nama,deskripsi,harga):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga
minum1 = menu_minuman('Jus Jambu','Jus Jambu merah tanpa gula',8500)
minum2 = menu_minuman('Jus alpukat ori','Jus dengan tambahan air gula merah',15000)
minum3 = menu_minuman('Jus alpukat xtra milk','Jus alpukat dengan campuran susu coklat dan taburan kepingan choco',15000)
minum4 = menu_minuman('Red & Smooth','Smoothy dengan pisang susu dan strawberry',17500)

pilihan_minuman = [minum1,minum2,minum3,minum4]
print("Daftar Menu Healthy Fruits")
for mn in pilihan_minuman:
    menu = '{} Harga Rp {}, {}'.format(mn.nama,mn.harga,mn.deskripsi)
    print(menu)