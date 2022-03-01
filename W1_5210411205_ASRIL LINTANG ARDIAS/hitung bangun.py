print("---Program Menghitung Luas, Volume & Keliling Balok---")

p = int(input("\nPanjang : "))
l = int(input("Lebar : "))
t = int(input("Tinggi : "))

luas = 2 * ( (p*l) + (p*t) + (l*t) )
volume = p * l * t
keliling = 4 * (p+l+t)

print("\nHasilnya")
print("Luas Balok = ", luas)
print("Volume Balok = ", volume)
print("Keliling Balok = ", keliling)

