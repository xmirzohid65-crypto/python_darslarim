# For bilan ishlash

mehmonlar = ['Jonibek', 'Temurbe', 'Bexruz', 'Doniyor']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon} sizni 20-mart kuni oshga taklif qilamiz")
    print(f"Hurmat bilan Palvanovlar oilasi")

sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati: {son**2} ga teng")

sonlar = list(range(11))
sonlar_kvdrt = []
for son in sonlar:
    sonlar_kvdrt.append(son**2)

print(sonlar)
print(sonlar_kvdrt)

dostlar = []
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5):
    dostlar.append(input(f"{n+1}-do'stingiz ismini kiriting: "))
print(f"Sizning 5ta eng yaqin do'stlaringiz {dostlar}")

avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
for avto in avtolar:
    if avto == 'bmw':
        print(avto.upper())
    else:
        print(avto.title())

ism = input("Ismingizni kiriting:\n>>>")
if ism.lower() != 'ali':
    print(f"Uzr, {ism.title()} biz Alini kutyapmiz.")
else:
    print("Salom, Ali")

javob = float(input("12x6 nechiga teng?>>>"))
if javob!=72:
    print("Javob xato!")
else:
    print("Javob to'g'ri")

yosh = int(input("Yoshingizni kiriting?>>>"))
if yosh>=18:
    print("Xush kelibsiz!")
else:
    print("Kirish taqiqlanadi!")

login = input("Yangi login yarating:>>>")
if len(login)<=5:
    print("Login 5 harfdan ko'p bo'lishi kerak!")
else:
    print("Login muvoffaqiyatli yaratildi")

yil = int(input("Tug'ilgan yilingizni kiriting:"))
if 2026-yil<18:
    print(f"Yoshingiz {2026-yil}da ekan.")
    print("Kirish mumkin emas")
else:
    print("Xush kelibsiz!")

yosh = int(input("Yoshingizni kiriting:"))
if yosh>65:
    print(f"Sizda COVID-19 alomatlari yuqori")
else:
    print("Siz hali sog'lom yoshda ekansiz")

x, y = 25, 50
print("x>y") if x>y else print("x<y")