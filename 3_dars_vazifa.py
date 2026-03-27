# Kvadrat va hisoblovchi 

print(" Sonning kvadratni topish uchun")

kvadrat = float(input("Sonni kiriting: "))
son_kvadrati = kvadrat ** 2

print("Sonning kvadrati", son_kvadrati, "ga teng")

# Kubni hisoblovchi

print("Sonning kubini topish uchun")

kub = float(input("Sonni kiriting: "))
son_kubi = kub ** 3

print("Sonning kubi", son_kubi, "ga teng")

# Inson yoshini aniqlovchi

yosh = input("Yoshingizni kiriting: ")

t_yil = 2026 - int(yosh)

print("Siz", t_yil, "yilda tug'ilgan ekansiz")

# Hisoblovchi

print("Sonlar ustida amal bajarish uchun")

amal = str(input("Bajarmoqchi bo'lgan amalni kiriting: "))

javob = eval(amal)

print("Javob:", javob)