car0 = {
    'model':'nexia 1',
    'rang':'oq',
    'yil':'2011',
    'narh':'2000',
    'km':'120000',
    'karobka':'mexanik'
}
car1 = {
    'model':'nexia 2',
    'rang':'oq',
    'yil':'2014',
    'narh':'7000',
    'km':'90000',
    'karobka':'mexanik'
}
car2 = {
    'model':'nexia 3',
    'rang':'qora',
    'yil':'2020',
    'narh':'12000',
    'km':'15500',
    'karobka':'avtomat'
}

cars = [car0, car1, car2]
for car in cars:
    print(f"{car['model'].title()},"
          f"{car['rang']} rang,"
          f"{car['yil']}-yil, {car['narh']}$")

print(cars[0])
print(cars[0]['model'])
print(f"{cars[1]['model']} "
      f"{cars[1]['rang']}")

malibus = []
for n in range(10):
    new_car = {
        'model':'malibu',
        'rang':None,
        'yil':2025,
        'narh':None,
        'km':0,
        'karobka':'avtomat'
    }
    malibus.append(new_car)

print(malibus)

for malibu in malibus[:3]:
    malibu['rang'] = 'qizil'

print(malibus)

for malibu in malibus[3:6]:
    malibu['rang'] = 'qora'

print(malibus)

for malibu in malibus[6:]:
    malibu['rang'] = 'oq'
    malibu['karobka'] = 'mexanik'

for malibu in malibus:
    if malibu['karobka'] == 'avtomat':
        malibu['narh'] = 40000
    else:
        malibu['narh'] = 35000

print(malibus)

dasturchilar = {
    'mirzohid':['python', 'java'],
    'doniyor':['css', 'html', 'js'],
    'ortiq':['php', 'sql'],
    'alisher':['c++', 'c#']
}

# for ism, tillar in dasturchilar.items():
#     print(f"{ism.title()} quyidagi dasturlash tillarni biladi: ")
#     for til in tillar:
#         print(til.upper())

for ism, tillar in dasturchilar.items():
    print(f"{ism.title()} quyidagi dasturlash tillarni biladi: ", end='')
    for til in tillar:
        print(til.upper(), end='')

hamkasblar = {
    'alisher':{'familiya':'azatov',
               'tyil':'1997',
               'ma\'lumot':'oliy',
               'tillar':['c++', 'c#']
               },
    'mirzhid':{'familiya':'xusainov',
               'tyil':'1995',
               'ma\'lumot':'oliy',
               'tillar':['puthon', 'java']
               },
    'doniyor':{'familiya':'azatov',
               'tyil':'1996',
               'ma\'lumot':'oliy',
               'tillar':['html', 'css', 'js']
               },
}

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()},"
          f"{info['tyil']}-yilda tug'ilgan"
          f"Ma'lumoti: {info['ma\'lumot']}.\n"
          f"Quyidagi dasturlash tillarni biladi: ", end='   ')
    for til in info['tillar']:
        print(til.upper(), end='  ')
