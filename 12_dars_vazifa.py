def toliq_ism_yasa(ism, familiya, t_yil, t_joy, email, tel_raqam):
    """To'liq ism, familiya va tug'ilgan yil va hokazo ma'lumotlarni qaytaruvchi funksiya"""
    return f"{ism} {familiya}, {t_yil}-yilda {t_joy}da tug'ilgan, Email: {email}, Telefon raqam: {tel_raqam}"

print("Saytimizga hush kelibsiz, o'zingiz haqidagi ma'lumotlarni kiriting")

malumotlar = []

while True:
    print("\nMana shu ma'lumotlarni to'ldiring:")
    ism = input("Ismingizni kiriting: ").title()
    familiya = input("Familiyangizni kiriting: ").title()
    t_yil = input("Tug'ilgan yilingizni kiritng: ")
    t_joy = input("Tug'ilgan joyingizni kiriting: ").title()
    email = input("Elektron pochtangizni kiriting: ").lower()
    if email == None:
        print("Kechirasiz, email bo'lishi shart!")
        continue
    tel_raqam = input("Telefon raqamingizni kiriting: ")
    
    malumotlar.append(toliq_ism_yasa(ism, familiya, t_yil, t_joy, email, tel_raqam))
    
    yopish = input("Yana ma'lumot kiritasizmi (ha/yo'q): ").lower()
    if yopish == 'yo\'q':
        break

print("\nSiz haqingizdagi ma'lumotlar:")
for siz in malumotlar:
    print(siz)

print('----------------------------')

print("Mijozlar royhatini to'ldiring")

mijozlar = []

while True:
    print("\nMana shu joylarni to'ldiring:")
    ism = input("Mijoz ismini kiriting: ").title()
    familiya = input("Mijoz familiyani kiriting: ").title()
    t_yil = input("Tug'ilgan yilni kiritng: ")
    t_joy = input("Tug'ilgan joyini kiriting: ").title()
    email = input("Elektron pochtasini kiriting: ").lower()
    if email == None:
        print("Kechirasiz, email bo'lishi shart!")
        continue
    tel_raqam = input("Telefon raqamini kiriting: ")
    
    mijozlar.append(toliq_ism_yasa(ism, familiya, t_yil, t_joy, email, tel_raqam))
    
    yopish_2 = input("Yana ma'lumot kiritasizmi (ha/yo'q): ").lower()
    if yopish_2 == 'yo\'q':
        break

print("\nSiz haqingizdagi ma'lumotlar:")
for mehmon in mijozlar:
    print(mehmon)

print('----------------------------')

def eng_katta(son_1, son_2, son_3):
    """Eng katta sonni qaytaruvchi funksiya"""
    return max(son_1, son_2, son_3)

son1 = float(input("1-sonni kiriting>>> "))
son2 = float(input("2-sonni kiriting>>> "))
son3 = float(input("3-sonni kiriting>>> "))

katta_son = eng_katta(son1, son2, son3)
print(f"{katta_son} raqamlar ichida eng kattasi")

print('----------------------------')

def aylana(radiusi, diametri, yuzi, perimetri):
    """Aylanani yuzi, perimetri va diametrini qaytaruvchi funksiya"""
    return aylana

aylana_r = int(input("Aylana radiusini kiriting: "))
aylana_d = aylana_r * 2
p = 3.1416
aylana_p = 2 * p * aylana_r
aylana_y = aylana_d * (aylana_r ** 2)

print(f"Radiusi: {aylana_r}\n Diametri: {aylana_d}\n Perimetri: {aylana_p}sm\n Yuzi: {aylana_y}sm kvadrat")

def tub_sonlar(a, b):
    """Tub sonlarni chiqaruvchi funksiya"""
    natija = []
    for son in range(a, b+1):
        if son > 1:
            tub = True
            for i in range(2, son): 
                if son % i == 0:
                    tub = False
                    break
            if tub:
                natija.append(son)
    return natija

print("Faqat 20 magacha bo'lgan tub sonlar")
print(tub_sonlar(1, 20))

def fibonachchi(n):
    """Fibonachchi ketme-ketligini chiqaruvchi funksiya"""
    natija = []
    a, b = 1, 1
    
    while a <= n:
        natija.append(a)
        a, b = b, a + b
    
    return natija

print("Fibonachchi ketme-ketligi 60 gacha bo'lgan")
print(fibonachchi(60))