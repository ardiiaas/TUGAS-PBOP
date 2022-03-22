# 5210411205_ASRIL LINTANG ARDIAS

from abc import ABC, abstractmethod

class Bentuk(ABC):
    @abstractmethod
    def luas(self):
        return self.__sisi * self.__sisi

    @abstractmethod
    def keliling(self):
        return 4 * self.__sisi

class persegi(Bentuk):
    def __init__(self, sisi):
        self.__sisi = sisi

    def luas(self):
        return self.__sisi * self.__sisi

    def keliling(self):
        return 4 * self.__sisi

Persegi = persegi(5)
print(Persegi.luas())
print(Persegi.keliling())