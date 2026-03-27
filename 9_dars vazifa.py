python_lugat = {
    'integer': 'Butun son',
    'float': "O'nlik son",
    'string': 'Matn',
    'if': 'Agar',
    'else': 'Aks holda',
    'boolean': 'Mantiqiy qiymat',
    'list': "Ro'yxat",
    'dictionary': "Lug'at",
    'tuple': "O'zgarmas ro'yxat",
    'for': 'Sikl (uchun)'
}

for python in python_lugat:
   if python in python_lugat:
    print(f"{python.title()}-{python_lugat[python]}")

davlatlar = {
'Aqsh':'Washington D.C.',
'Russiya':'Moskva',
'O\'zbakiston':'Toshkent',
'Qozog\'zton':'Ostana'
}

print("Dunyo davlatlar:")
for davlat in sorted(davlatlar.keys()):
    print(davlat)

print("Davlatlar poytaxtlari:")
for poytaxt in sorted(davlatlar.values()):
   print(poytaxt)

bilish = input("Qaysi davlatni poytaxtini nomini bilib olmoqchisiz?: ").title()
if bilish in davlatlar:
    print(f"{bilish.title()}ning poytaxti {davlatlar[bilish]}")
else:
    print("Kechirasiz, bizda bu davlat haqida ma'lumot yo'q")

taomlar = {
   'non':'4000',
   'choy':'6500',
   'osh':'35000',
   'manti':'12300',
   'somsa':'13000',
   'shashlik':'17000',
   'sho\'rva':'26000',
   'kabob':'55000',
   'salat':'8000',
   'gumma':'11000'
}

buyurtma = input("3 ta taom buyurtma bering>>> ").split()

for taom in buyurtma:
    if taom in taomlar:
        print(f"{taom} {taomlar[taom]} so'm")
    else:
        print(f"{taom} menyuda yo'q")