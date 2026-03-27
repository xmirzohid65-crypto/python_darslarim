# key-value bilan ishlash

car_0 = {'model':'ferrari', 'rang':'qizil'}
print(car_0)
print(car_0['model'])
print(car_0['rang'])

talaba = {'ism':'mirzohid xusainov', 'yosh':15, 't_yil':2011}
talaba['kurs'] = 4
talaba['fakultet'] = 'IT'

print(talaba)

print(f"{talaba['ism'].title()},\
 {talaba['yosh']}-yoshda,\
 {talaba['t_yil']}-yilda tug'ilgan")

talaba_1 = {}
talaba_1['ism'] = 'mirzahid xusainov'
talaba_1['yosh'] = '25'
talaba_1['kurs'] = 3
print(talaba_1)
print(f"Talaba {talaba_1['ism']}, {talaba_1['yosh']}, {talaba_1['kurs']}-kurs")

talaba_1['kurs'] = 4
talaba_1['ism'] = 'alisher azatov'

print(f"Talaba {talaba_1['ism']}, {talaba_1['yosh']}, {talaba_1['kurs']}-kurs")

talaba_3 = {'ism':'mirzohid xusainov', 'yosh':15, 't_yil':2011}
print(talaba_3)
del talaba_3['yosh']
print(talaba_3)

telefonlar = {
    'xasan':'iphone x',
    'xusan':'redmi s9',
    'mirzohid':'redmi a10',
    'alisher':'ifinx s55'
}
phone = telefonlar['mirzohid']
print(phone)

phone_1 = telefonlar['alisher']
print(phone_1)

