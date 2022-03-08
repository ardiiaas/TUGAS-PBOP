#5210411205_ASRIL LINTANG ARDIAS

class utama:
    def __init__(self):
        self._a = 2

class turunan:
    def __init__(self):
        utama.__init__(self)
        print("Memanggil variabel protekted pada class utama : ",self._a)
        self._a = 3
        print("Memanggil variabel protekted dimodifikasi dari luar class : ",self._a)

object1 = turunan()
object2 = utama()

print("mengakses variabel protected dari objek1: ",object1._a)
print("mengakses variabel protected dari objek2: ",object2._a)