svetafor = [
    'qizil',
    'sariq',
    'yashil'
]
while True:
    sorash = input("Svetaforda qaysi rang? ")
    if sorash in svetafor:
        print("Rahmat, to'g'ri keladi")
        break
    else:
        print("Xato rang")

# import random

# tasodifiy_son = random.randint(1,10)

# while True:
#     topish_kerak = input("Random sonni toping ")
#     if topish_kerak == tasodifiy_son:
#         print("Tabriklaymiz siz random sonni topdingiz!👍👍👍")
#         break
#     else:
#         print("Kechirasiz, siz topa olmadingiz yana urinib ko'ring")

ismlar = []

print("Yaqin do'stlaringiz ro'yhatini yuzing: ")

while True:
    savol = f"Do'stingiz ismini kiriting: "
    ism = input(savol)
    ismlar.append(ism)
    javob = input("Yana do'stingizni qo'shmoqchisizmisiz? (agar kiritmoqchi bo'lsangiz yes/bo'lmasa stop)>>> ")
    if javob == 'stop':
        break
    else:
        continue

print("Do'stlaringiz ro'yhati:")
for ism in ismlar:
    print(f"{ism.title()}")



kurs = 12600

while True:
    summa = input("So'm kiriting (chiqish uchun exit yozing): ")

    if summa == "exit":
        print("Dastur ishlashdan to'xtadi")
        break

    summa = float(summa)
    dollar = summa / kurs

    print("Dollar:", dollar)