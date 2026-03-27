# while yordamida ro'yhatni to'ldirish

ismlar = []

print("Yaqin do'stlaringiz ro'yhatini yuzing: ")
n=1
while True:
    savol = f"{n} do'stingiz ismini kiriting: "
    ism = input(savol)
    ismlar.append(ism)
    javob = input("Yana do'stingizni qo'shmoqchisizmisiz? (ha/yo'q)>>> ")
    if javob == 'ha':
        n+=1
        continue
    else:
        break

print("Do'stlaringiz ro'yhati:")
for ism in ismlar:
    print(f"{ism.title()}")

print("Do'stlaringiz yoshini saqlaymiz.")
dostlar = {}
ishora = True

while ishora:
    ism = input("Do'stingizni ismini kiriting>>> ")
    yosh = input(f"{ism.title()}ning yoshini kiriting>>> ")
    dostlar[ism] = int(yosh)

    javob = input("Yana ma'lumot saqlamoqchimisiz? (ha/yo'q)>>> ")
    if javob == 'yo\'q':
        ishora = False

for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")

cars = ['lacetti', 'nexia', 'cobalt', 'nexia', 'spark', 'nexia']
while 'nexia' in cars:
    cars.remove('nexia')
print(cars)

talabalar = ['mirzohid', 'alisher', 'doniyor', 'baxtiyor']
baholangan_tlabalar = {}
while talabalar:
    talaba = talabalar.pop()
    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
    print(f"{talaba.title()}ning bahosi {baho}")
    baholangan_tlabalar[talaba] = baho

print(talabalar)