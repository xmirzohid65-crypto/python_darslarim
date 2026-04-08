# def bahalor(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()} ning bahosi kirirting>>> ")
#         baholar[ism] = baho
#
#     return baholar
#
# talablar = ['ali', 'vali', 'xasan']
# baholar = bahalor(talablar)
# print(baholar)
#
# talablar = ['ali', 'vali', 'xasan']
# baholar = bahalor(talablar[:])
# print(baholar)

# def katta_harf(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i] = matnlar[i].title()
#     return matnlar
#
# ismlar = ['mirzohid', 'alish', 'yasin']
# katta_harf(ismlar)
# print(ismlar)

# def katta_harf(matnlar):
#     matnlar = matnlar[:]
#     for i in range(len(matnlar)):
#         matnlar[i] = matnlar[i].title()
#     return matnlar
#
# ismlar = ['mirzohid', 'alish', 'yasin']
# yangi_ismlar = katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)

# talabalar = ['ali', 'vali', 'hasan', 'xusan']
#
# def baholar(ismlar):
#     baholar = {}
#     for i in ismlar:
#         print(f"Talaba {i}ning bahosini kiritng: ")


# def summa(*sonlar):
#     """Kiritgan sonlarni yig'indisini chiqaruvchi funksiya"""
#     yigindi = 0
#     for son in sonlar:
#          yigindi += son
#     return yigindi
# print(summa(1,2))
# print(summa(1,2,3,4))

# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini chiqaruvchi funksiya osonlashtirilgan turi"""
#     return sum(sonlar)
#
# print(summa(1,2,3,4,5,6,7))

# def avto_info(kompaniya,model,**malumotlar):
#     """Avtolar haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     malumotlar['kompaniya'] = kompaniya
#     malumotlar['model'] = model
#     return malumotlar
#
# def avto_qoshish():
#     kompaniya = input('Kompaniya: ').title()
#     model = input('Model: ').title()
#     rang = input('Rang: ').title()
#     yil = input('Yili: ')
#     narx = input('Narxi: ')
#
#     return avto_info(kompaniya,model, rang = rang, yil = yil, narx = narx)
#
# avto = avto_qoshish()
# print(avto)

# def avto_info(kompaniya,model,**malumotlar):
#     """Avtolar haqidagi ma'lumotlarni qaytaruvchi funksiya"""
#     info = {}
#     info['kompaniya'] = kompaniya
#     info['model'] = model
#     info.update(malumotlar)
#     return info
#
# avto1 = avto_info('GM', 'Malibu', rang = 'Qora', yil = 2020)
# avto2 = avto_info('BMW', 'M5 F90', rang = 'darkmoon', yil = 2025)
#
# avtolar = [avto1, avto2]
#
# for i, avto in enumerate(avtolar, 1):
#     print(f"\n{i}-mashina:")
#     for k, v in avto.items():
#         print(f"{k}: {v}")

# def summa(x,y,*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblovchi funksiya"""
#     return x+y+sum(sonlar)
#
# print(summa(1,26))
#
# def avto_info(kompaniya,model,**malumotlar):
#     """Avtolar haqidagi ma'lumotlarni qaytaruvchi funksiya"""
#     malumotlar['kompaniya'] = kompaniya
#     malumotlar['model'] = model
#     return malumotlar
#
# avto1 = avto_info('GM', 'Jentra', rang = 'Qora', yil = 2020)
# avto2 = avto_info('Kia', 'K5', rang = 'Oq', yil = 2025)
#
# print(avto1)
# print(avto2)