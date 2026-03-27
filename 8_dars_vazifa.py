oilam = {
    'otam':'mansur', 'tu\'lgan_1':'1981-yil', 'viloyat_1':'xorazm',
    'onam':'aqiljon', 'tu\'lgan_2':'1986-yil', 'viloyat_2':'xorazm',
    'opam':'sagdiana', 'tu\'lgan_3':'2008-yil', 'viloyat_3':'xorazm'
}

print(f"Otam {oilam['otam'].title()}, {oilam['tu\'lgan_1']}da {oilam['viloyat_1'].title()}da tavallud topgan")
print(f"Onam {oilam['onam'].title()}, {oilam['tu\'lgan_2']}da {oilam['viloyat_2'].title()}da tavallud topgan")
print(f"Opam {oilam['opam'].title()}, {oilam['tu\'lgan_3']}da {oilam['viloyat_3'].title()}da tavallud topgan")

print()

oilam_taomlar = {
    'otam_taomi':'manti',
    'onam_taomi':'chuchvara',
    'opam_taomi':'kabob',
    'ali_taomi':'osh',
    'vali_taomi':'lag\'mon'
}

print(f"Otam {oilam_taomlar['otam_taomi'].title()} yaxshi ko'radi")
print(f"Onam {oilam_taomlar['onam_taomi'].title()} yaxshi ko'radi")
print(f"Opam {oilam_taomlar['opam_taomi'].title()} yaxshi ko'radi")
print(f"Ali {oilam_taomlar['ali_taomi'].title()} yaxshi ko'radi")
print(f"Vali {oilam_taomlar['vali_taomi'].title()} yaxshi ko'radi")

print()

izohli_lugat = {
    'lug\'at_1':'for',
    'lug\'at_2':'if',
    'lug\'at_3':'elif',
    'lug\'at_4':'else',
    'lug\'at_5':'input',
    'lug\'at_6':'integer',
    'lug\'at_7':'float',
    'lug\'at_8':'string',
    'lug\'at_9':'f-string',
    'lug\'at_10':'get'
}

print(izohli_lugat)

print()

sorov = input("Tepadagi lug'atdan bittasini yozing: ")

if sorov == 'for':
    print("For bu takrorlash aperatori")
elif sorov == 'if':
    print("If bu shart berish va tekshirish aperatori")
elif sorov == 'elif':
    print('Elif yordamida bir nechta shartlarni ketme-ket tekshiish mumkin')
elif sorov == 'else':
    print("Else agar if yoki elif qismi tushmagan payt ishlovchi aperator")
elif sorov == 'input':
    print("Input bu so'rovchi aperator")
elif sorov == 'integer':
    print("integer bu butun son")
elif sorov == 'float':
    print("Float bu o'nlik son")
elif sorov == 'string':
    print("String bu ma'lumot turi")
elif sorov == 'f-string':
    print("F-string ichida o'zgaruvchilarni {} bunday qavus ichida yoziladi \n Va uni ichida turli methodlarni qo'llash oson bo'ladi")
elif sorov == 'get':
    print("Get bu lug'at bilan ishlatuvchi cod")
else:
    print("Bunday so'z lug'atda mavjud emas!")