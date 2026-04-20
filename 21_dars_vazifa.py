import datetime as dt

bugun = dt.date.today()

for n in range(10):
    sana = bugun + dt.timedelta(weeks=n)
    print(f"{n+1}-sana: {sana}")

bugun = dt.date.today()
ramazon = dt.date(2027,2,8)
farq = ramazon - bugun
print(f"Keyingi Ramazongacha: {farq} qoldi")

this_day = dt.date.today()
birthday = dt.date(2025,9,14)
farq = this_day - birthday
print(f"Tug'ilgan kunim o'tib ketganiga: {farq} qoldi")

bugun = dt.date.today()
hayt = dt.date(2026,5,27)
farq = hayt - bugun
print(f"Haytgacha: {farq} kun qoldi")

import re

savol = input("Telefon raqamingizni kiriting: ")

andoza = r"^\+998\d{9}$"

if re.match(andoza, savol):
    print("Rahmat sizning raqamingiz qabul qilindi")
else:
    print("Kechirasiz bu raqam mavjud emas yoki, \n Bu raqam O'zbekiston raqami emas")

matn = """Salom men sizni bugun smartphonelar bilan tanishtirib chiqaman. 
Bugun biz apple, https://www.apple.com/, samsung, https://www.samsung.com/ bilan tanishib chaqimiz.
Siz hozir  ikkita companiya saytlariga kirsangiz ular ishlab chiqaradigan telefonlarni ko'rishingiz mumkin"""

httpslar = r"https://[^\s,]+"

natija = re.findall(httpslar, matn)

if natija:
    print("Matnda https linklar bor ekan")
    print(natija)