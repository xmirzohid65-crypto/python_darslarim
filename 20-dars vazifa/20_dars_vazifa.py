# Avto haqidagi ma'lumotlarni json faylga yukladim

import json

data = {'Model':'Malibu', 'Rang':'Qora', 'Yil':'2020', 'Narx':40000}

json_data = json.dumps(data)
print(json_data)
print(type(json_data))
data = json.loads(json_data)

json_fayl = 'data_avto.json'
with open(json_fayl, 'w') as f:
    json.dump(data, f)

# Talabani chaqirib json faylga yukladim

talaba_json = {'Ism':'Hasan', 'Familiya':'Husanov', 'Tyil':2000}
print(f"{talaba_json['Ism']} {talaba_json['Familiya']}")

json_talaba_info = 'talaba.json'

with open(json_talaba_info, 'w') as f:
    json.dump(talaba_json, f)

# Students jsondan pythonga  o'tirib chaqirdim

faylnomi = 'students.json'

with open(faylnomi, 'r') as f:
    students = json.load(f)

for talaba in students['student']:
    print(f"{talaba['name']} {talaba['lastname']}, {talaba['year']}-kurs, {talaba['faculty']} talabasi")

# Api-resueltni chaqirdim

faylname = 'api-result.json'

with open(faylname, 'r') as f:
    api = json.load(f)

for page in api['query']['pages'].values():
    print(f"Sarlavha {page['title']} \n{page['extract']}")