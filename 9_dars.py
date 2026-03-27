# lug'at davomi

talaba = {
    'ism':'mirzohid',
    'familiya':'xusainov',
    'yosh':15,
    'faqultet':'kompyuter injeneriya',
    'kurs':2
}

# print(talaba)
# print(talaba.items())

for kalit, qiymat in talaba.items():
    print(f"Kalit:{kalit}")
    print(f"Qiymat:{qiymat}\n")

telefonlar = {
    'ali':'iphone x',
    'vali':'samsung a10',
    'alish':'novey 10pro',
    'orif':'nokia 3310',
    'doni':'iphone x',
    'hamdam':'samsung a10',
    'temur':'iphone x'
}

for k, q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")

mahsulotlar = {
    'anor': 25000,
    'olma': 15000,
    'banan': 25500,
    'shaftoli': 32300,
    'uzum': 40000
}

# print(mahsulotlar.keys())
#
# print("Do'kondagi mahsulotlar")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot)

bozorlik = ['anor', 'uzum', 'baliq', 'non']
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]}so'm")

for buyum in bozorlik:
    if buyum not in mahsulotlar:
        print(f"Iltimos, do'koningizga {buyum} ham olib keling!")

print("Do'konimizdagi mahsulotlar")
for mahsulot in sorted(mahsulotlar):
    print(mahsulot.title())

print(telefonlar.values())

print("Ishchilarimiz quyidagi telefonlardan foydalanishadi")
for tel in set(telefonlar.values()):
    print(tel.title())

meningset = {'olma', 'banan', 'anor'}
print(meningset)

for x in meningset:
    print(x)

print("banan" in meningset)

meningset.add("orange")

print(meningset)

meningset = {'olma', 'banan', 'anor'}
tropical = {'mango', 'anor', 'papaya'}

meningset.update(tropical)

print(tropical)

meningset.remove('olma')
print(meningset)

son = 1
while son<=5:
    print(son, end=" ")
    son = son +1

print("Istalgan sonning kvadratini topuvchi dastur")
savol = "Istalgan son kiriting: "
savol += "(dasturni to'xtatish uchun esa 'exit' deb yozing>>> "
qiymat = ''

while qiymat != 'exit':
    qiymat = input(savol)
    if qiymat != 'exit':
        print(float(qiymat)**2)

print("Istalgan sonning kvadratini topuvchi dastur")
savol = "Istalgan son kiriting: "
savol += "(dasturni to'xtatish uchun esa 'exit' deb yozing>>> "
ishora = True

while ishora:
    qiymat = input(savol)
    if qiymat == 'exit':
        ishora = False
    else:
        print(float(qiymat) ** 2)

while True:
    print('010101001000110100', end='')

print("Istalgan sonning kvadratini topuvchi dastur")
savol = "Istalgan son kiriting: "
savol += "(dasturni to'xtatish uchun esa 'exit' deb yozing>>> "

while True:
    qiymat = input(savol)
    if qiymat == 'exit':
        break
    else:
        print(float(qiymat) ** 2)

sonlar = list(range(1,11))
for son in sonlar:
    if son == 5:
        break
    else:
        print(f"{son} ning kvadrati {son**2} ga teng")