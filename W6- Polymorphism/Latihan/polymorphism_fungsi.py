# 5210411205_ASRIL LINTANG ARDIAS
# Polymorphism dengan menggunakan fungsi

print(len('Polymorphism')) # Output 12
print(len([1,2,3,4,5])) # Output 5

# Using Class
class Indonesia:
    def ibukota(self):
        print('Jakarta adalah ibukota negara Indonesia')

class Malaysia:
    def ibukota(self):
        print('Kuala Lumpur adalah ibukota neraga Malaysia')

negara1 = Indonesia()
negara2 = Malaysia()

for country in (negara1, negara2):
    country.ibukota()