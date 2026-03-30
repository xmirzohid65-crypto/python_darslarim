# Funksiya python
# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu aleykum")
#
# salom_ber()
#
# def salom_ber(ism):
#     """Foydalanuvchidan ismini qabul qilib, unga salom beruvchi funksiya"""
#     print(f"Assalomu aleykum, hurmatli {ism.title()}")
#
# salom_ber('hasan')
# print(salom_ber.__doc__)

# def toliq_ism(ism, familiya):
#     """Foydalanuvchidan ismini va familiyasini qabul qilib, unga salom beruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
#
# toliq_ism('mirzohid', 'xusainov')

# def yosh_hisoblovchi(tugilgan_yil, joriy_yil=2026):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini topuvchi funksiya"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yildasiz")
#
# yosh_hisoblovchi(2011)

# def toliq_ism_yasa(ism, familiya, otasi_ismi = ''):
#     """To'liq ism, familiya va otasini ismini qaytaruvchi funksiya"""
#     if otasi_ismi:
#         toliq_ism = f"{ism.title()} {otasi_ismi.title()} {familiya.title()}"
#     else:
#         toliq_ism = f"{ism.title()} {familiya.title()}"
#     return toliq_ism.title()

# talaba1 = toliq_ism_yasa('alisher', 'qahramanovich', 'azatov')
# talaba2 = toliq_ism_yasa('mirzohid', 'xusainov')
# print(f"Darsga kirmagan o'quvchilar {talaba1} va {talaba2}")

def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rang':rangi,
            'korobka':korobka,
            'yil':yili,
            'narh':narhi
            }
    return avto

# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")


# def oraliq(min,max):
#     sonlar = [] # bo'sh ro'yxat
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar

# print(oraliq(1,10))

print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
avtolar = []  # salondagi avtolar uchun bo'sh ro'yxat
while True:
    print("\nQuyidagi ma'lumotlarni kiriting")
    kompaniya = input("Ishlab chiqaruvchi: ")
    model = input("Modeli: ")
    rangi = input("Rangi: ")
    korobka = input("Korobka: ")
    yili = input("Ishlab chiqarilgan yili: ")
    narhi = input("Narhi: ")

    # Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida
    # lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))

    # Yana avto qo'shish-qo'shmaslikni so'raymiz
    javob = input("Yana avto qo'shasizmi? (yes/no): ")
    if javob == 'no':
        break

print(avtolar)
