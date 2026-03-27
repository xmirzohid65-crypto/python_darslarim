foydalanuvchilar = ['admin123', 'login012', 'qwerty09', 'hacker001', 'python313']
foydalanuvchi = input("Yangi login yarating:>>>")
if foydalanuvchi in foydalanuvchilar:
    print("Bu login band, iltimos boshqa login yarating!")
elif len(foydalanuvchi)<=5:
    print("Login kamida 6 harfdan iborat bo'lishi kerak!")
else:
    print("Login muvoffaqiyatli yaratildi")

sonlar = float(input("Istalgan butun son kiriting:>>> "))
for n in range(2, 11):
    if sonlar % n == 0:
        print(f"{sonlar} soni {n} ga qoldiqsiz bo'linadi")

juft_sonlar = int(input("Juft son kiriting:>>> "))
if juft_sonlar % 2 == 0:
    print("Rahmat")
else:
    print("Iltimos juft son kiriting!")

yosh = int(input("Yoshingizni kiriting:>>> "))
if yosh <= 4 or yosh >=60:
    print("Sizga kirish bepul")
elif yosh < 18:
    print("Siz uchun bilet narxi 10.000 so'm")
else:
    print("Siz uchun bilet narxi 20.000 so'm")

son_1 = float(input("Birinchi sonni kiriting:>>> "))
son_2 = float(input("Ikkinchi sonni kiriting:>>> "))
if son_1 < son_2:
    print(f"{son_1}<{son_2} dan")
elif son_1 > son_2:
    print(f"{son_1}>{son_2} dan")
else:
    print(f"{son_1}={son_2} ga")