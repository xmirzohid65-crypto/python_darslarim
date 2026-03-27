# elifni ishlatish 

yosh = int(input("Yoshingizni nechida:>>>"))
if yosh <= 4:
    price = 0
elif yosh <= 12:
    price = 5000
elif yosh < 65:
    price = 10000
elif yosh >= 65:
    price = 8000
print(f"Siz uchun bilet narxi {price} so'm")

kun = input("Bugun qanday kun?>>> ")
if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
    print("Bugun dam olish kuni")
else:
    print("Bugun ish kuni")

kun = input("Bugun qanday kun?>>> ")
harorat = input("Havo qanday?: ")
if kun.lower() == 'yakshanba' and harorat >= 30:
    print("Cho'milishga ketdik")
elif kun.lower() == 'yakshanba' and harorat < 30:
    print("Uyda dam olamiz")
else:
    print("Bugun ish kuni, keyin dam olamiz")

kun = input("Bugun qanday kun?>>> ")
harorat = input("Havo qanday?: ")
if (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat >= 30:
    print("Cho'milishga ketdik")
elif (kun.lower() == 'shanba' or kun.lower() == 'yakshanba') and harorat < 30:
    print("Uyda dam olamiz")
else:
    print("Bugun ish kuni, keyin dam olamiz")

narh = 15000
choy = True
salat = False

if choy and salat:
    narh = narh + 10000
elif choy or salat:
    narh = narh + 5000

print(f"Jami summa {narh} so'm bo'ldi")

menu = ['osh', 'manti', 'baliq', 'sho\'rva', 'kabob']
ovqat = input("Qanday taom hohlaysiz:?>>> ")
if ovqat.lower() in menu:
    print("Buyurtmangiz qabul qilindi")
else:
    print("Afsuski bizda bunaqa taom yo'q")

menu = ['osh', 'manti', 'baliq', 'sho\'rva', 'kabob']
ovqat = input("Qanday taom hohlaysiz:?>>> ")
if ovqat.lower()  not in menu:
    print("Afsuski bizda bunaqa taom yo'q")
else:
    print("Buyurtmangiz qabul qilindi")

menu_2 = ['palov', 'shashlik', 'manti', 'salat', 'sho\'rva']
buyurtmam = ['palov', 'shashlik', 'barak', 'kampot', 'sho\'rva']

if buyurtmam:
 for taom in buyurtmam:
    if taom in menu_2:
        print(f"Menuda {taom} bor")
    else:
        print(f"Kechirasiz, bizda {taom} qolmagan edi")
else:
   print("Hali buyurma bermagansiz, iltimos buyurtmani bering!")