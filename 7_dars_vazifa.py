pochtalar = ['user1@gmail.com', 'qwerty123@gmail.com', 'python23gmail.com']

for email in pochtalar:
        if "@" not in email:
             print(f"Email noto'g'ri {email}")


parollar = ["password123", "Qwerty!", "admin", "StrongPass1!"]

for parol in parollar:
    if len(parol) < 8:
        print("Juda qisqa:", parol)
    elif not any(c.isdigit() for c in parol) or not any(not c.isalnum() for c in parol):
        print("Kuchsiz parol:", parol)
    else:
        print("Kuchli parol:", parol)

ob_havo = [20, 22, 19, 24, 25, 23, 21]
umumiy = 0

for gradus in ob_havo:
    umumiy = gradus
    if umumiy > 22:
        print(f"Bugun havo issiq, {gradus}-gradus")
    else:
        print(f"Bugun havo salqin, {gradus}-gradus")

ortacha = sum(ob_havo) / len(ob_havo)
print(f"Haftalik o'rtacha havo harorati {ortacha}")

taomlar = ["Shashlik", 'Manti', 'Kabob', 'Lag\'mon']
buyurtma = input("Buyurtmangizni kiriting:>>> ")

bor = False

for taom in taomlar:
    if buyurtma.lower() == taom.lower():
        bor = True

if bor:
        print(f"Buyurtmangiz qabul qilindi")
else:
        print(f"Kechirasiz bizda bunday taom qolmagan edi")

yoshlar = [16, 21, 17, 30, 25]

for yosh in yoshlar:
    if yosh < 18:
        print(f"Yosh chegarasi yetmagan, siz {yosh} yoshda siz")
    else:
        print(f"Xush kelibsiz, siz {yosh} yoshda ekan siz")

xabarlar = ['Yangi xabar', 'Batareya past', 'Yangilash mavjuyd']

for kam in xabarlar:
    if kam == 'Batareya past':
        print("Telefoningizni quvvatlang!")

fayllar = ['kitob.jpg', 'ko\'kjiguli.mp3', 'tabiat.jpg', 'malohat.mp3', 'iphone16.jpg']
musiqalar = []
rasmlar = []

for fayl in fayllar:
    if fayl.find('.jpg') != -1:
        rasmlar.append(fayl)
    elif fayl.find('.mp3') != -1:
        musiqalar.append(fayl)

print(f"Rasmlarning fayllari {rasmlar}")
print(f"Musiqalarning fayllari {musiqalar}")