cars = ['bmw', 'toyoto', 'mersedes-benz', 'volvo']
cars.sort()
print(cars)

mehmonlar = ["Jonibek", 'Asadbek', 'Donyor', 'Mahmud', 'Bexruz']
print("sorted() qaytargan ro'yhat:", sorted(mehmonlar))
print("sorted()+reverse=true qaytargan ro'yhat:", sorted(mehmonlar, reverse=True))
print("Asl o'zgarmagan ro'yhat:", mehmonlar)

ages = [12, 13, 23, 26, 56, 67, 47, 98]
ages.sort()
print(ages)
print(sorted(ages, reverse=True))

fruits = ['shaftoli', 'olma', 'nok', 'banan', 'tarvuz']
fruits.reverse()
print(fruits)

print(list(range(1,10)))
print(list(range(50,100)))

juft_sonlar = list(range(0,20,2))
toq_sonlar = list(range(1,20,2))
print("Juft sonlar:", juft_sonlar)
print("Toq sonlar:", toq_sonlar)

print(list(range(20)))

narhlar = [12000, 23000, 5600, 15500, 100000]
arzon = min(narhlar)
qimmat = max(narhlar)
jami = sum(narhlar)

print("Eng arzon qiymat", arzon, ".Eng qimmat qiymat", qimmat , ".Umumiy summa:",jami )

cars = ['bmw', 'toyoto', 'mersedes-benz', 'volvo', 'generalmotors']
my_cars = cars[0:3]
a_cars = cars[2:5]

print(my_cars)
print(a_cars)

print(cars[:4])
print(cars[2:])

sonlar = [1, 2, 3, 4, 5]
sonlar2 = sonlar[:]
sonlar2.append(6)
sonlar2.append(7)

print("Bu sonlardagi ro'yhat:",sonlar)
print("Bu sonlar2dagi ro'yhat:",sonlar2)

tomonlar = (20, 30, 40)
print(tomonlar)

toys = ('bus', 'car', 'bear', 'dino', 'snake', 'lizard')
print(toys[0])
print(toys[3])
print(toys[2])

toys = list(toys)
toys.append("daragon")
toys.remove("lizard")
toys[1] = 'raptor'
toys = tuple(toys)
print(toys)

thisset = {'olma', 'banan', 'olcha'}
print(thisset)
print("banan" in thisset)
