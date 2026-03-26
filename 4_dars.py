mevalar = ["olma", "shaftoli", "o'rik", "banan"]
narxlar = [12000, 10900, 18000, 22000]
sonlar = [1, 2, 3, 4, 5]
ismlar = []

print(mevalar, narxlar, sonlar, ismlar)

print("Birinchi meva", mevalar[0].title())
print("Ikkinchi meva", mevalar[1].upper())

narxlar = [12000, 10900, 18000, 22000]
narxlar[0] = 13000
narxlar[1] = 11000
narxlar[3] = narxlar[3] + 2000

print(narxlar)

mevalar = ["olma", "shaftoli", "o'rik", "banan"]
mevalar.append("tarvuz")
print(mevalar)

cars = []
cars.append("Lacetti")
cars.append("Damas")
cars.append("Malibu")
print(cars)

cars = ["Lacetti", "Damas", "Malibu"]
cars.insert(0, "Cobalt")
cars.insert(2, "Nexia2")
print(cars)

del mevalar[1]
print(mevalar)

mevalar.remove("tarvuz")
print(mevalar)

hayvonlar = ['mushuk', "it", 'ot', "qo'y", 'echki', 'ot']
hayvonlar.remove('ot')
print(hayvonlar)

bozorlik = ["go'sht", "yog'", 'banan', 'non', 'guruch']
mahsulot = bozorlik.pop(3)
print("Men", mahsulot ," sotib oldim")
print("Olinmagan mahsulotlar", bozorlik)