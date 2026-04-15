faylnomi = 'matn.txt'
with open(faylnomi, 'r') as fayl:
    matn = fayl.read()

print(matn)

print('-------------------------------')

fayl_pi = 'pi_million_digits.txt'
with open(fayl_pi) as pi:
    pi_million_digits = pi.read()
    if '14092011' in pi_million_digits:
        print("Sizning tug'ilgan yilingiz pi ichida bor ekan😊😊😊")
    else:
        print("Kechirasiz sizningtug'ilgan yilingiz yo'q ekan")

import pickle

pi_yangi = pi_million_digits
yangi_fayl = 'Pi_yangi.txt'
with open(yangi_fayl, 'wb') as fayl:
    pickle.dump(pi_yangi,fayl)

filename = "malumotlar.txt"

while True:
    data = input("Ma'lumot kiriting (chiqish uchun 'exit' deb yozing): ")
    
    if data.lower() == 'exit':
        print("Dastur tugadi.")
        break

    with open(filename, 'a') as file:
        file.write(data + "\n")

    print("Ma'lumot faylga saqlandi.\n")