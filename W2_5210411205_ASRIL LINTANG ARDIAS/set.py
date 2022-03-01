#5210411205_ASRIL LINTANG ARDIAS

# set dengan nlai campuran
data = {'peter','robben','skye',10,20,30}
print ("Data = ",data)
 
# 1. Menambahkan nama juan untuk anggota set dengan menggunakan fungsi add()
data.add('juan')
print("\nHasil add = ",data)
 
# 2. Menambahkan nilai  untuk anggota set dengan menggunakan fungsi update()
data.update([40,80,100])
print("Hasil Update = ",data)

# 3. Menghapus anggota menggunakan fungsi remove()
data.remove(10)
print("Hasil Remove = ",data)

# 4. Menghapus anggota menggunakan fungsi discard()
data.discard('skye')
print("Hasil discard = ",data)

print("\n-------------------------------------------------------------------------------")

print("\nOperasi Set diPython")
data1 = {4,1,6,3}
data2 = {1,4,7,8}
print("\nData 1 = ",data1)
print("Data 2 = ",data2)
# 1. Operasi Gabungan (Union)
# menggunakan tanda palang |
print("\nHasil gabungan dengan tanda | = ",data1|data2)
# menggunakan fungsi union
data3 = data1.union(data2)
print ("Hasil gabungan dengan union = ",data3)

# 2.  Operasi Irisan (Intersection)
# menggunakan tanda &
print("Hasil irisan dengan tanda & = ",data1 & data2)
# menggunakan fungsi intersection
data3 = data1.intersection(data2)
print ("Hasil irisan dengan intersection",data3)

# 3. Operasi selisih (Difference)
# menggunakan tanda min -
print("Hasil selisih dengan tanda - = ",data1 - data2)
# menggunakan fungsi difference
data3 = data1.difference(data2)
print ("Hasil selisih dengan difference = ",data3)