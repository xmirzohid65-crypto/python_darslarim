# Obyektlar bilan ishlash

class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1

    def get_info(self):
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi, {self.tyil}-yilda tug'ilgan"

    def set_bosqich(self,bosqich):
        """Talabani nechinchi bosqichda ekanligini qaytaruvchi"""
        self.bosqich = bosqich

    def update_bosqich(self):
        """Talabaning bosqichi ustiga birni qo'shib boradi"""
        self.bosqich += 1

    def get_name(self):
        """Talaba ismini qaytaruvchi"""
        return self.ism

    def last_name(self):
        """Talana familiyasini qaytaruvchi"""
        return self.familiya

    def get_full_name(self):
        """Talabani to'liq ism va familiyasini qaytaruvchi"""
        return f"{self.ism} {self.familiya}"

    def get_age(self, yil):
        """Talaba yoshini qaytaruvchi"""
        return yil - self.tyil

class Fan:
    def __init__(self,nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_students(self,talaba):
        """Fanga talabalarni qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_students(self):
        return [talaba.get_info() for talaba in self.talabalar]

    def get_students_num(self):
        """Talabalarni  oliy matematikadagi soni"""
        return self.talabalar_soni

# matematika = Fan('Oliy Matematika')
# talaba1 = Talaba('Karim', 'Salimov', 2011)
# talaba2 = Talaba('Ali', 'Valiyev', 2011)
# talaba3 = Talaba('Murod', 'Ahmadov', 2011)
#
# print(talaba1.get_age(2026))
# matematika.add_students(talaba1)
# matematika.add_students(talaba2)
# matematika.add_students(talaba3)
#
# print(matematika.get_students_num())
# print(matematika.talabalar_soni)
# mat_talabalar = matematika.get_students()
# print(mat_talabalar)

# talaba1 = Talaba('Mirzohid', 'Xusainov', 2011)
# print(talaba1.get_info())
#
# talaba1.bosqich = 2
# print(talaba1.get_info())
#
# talaba1.set_bosqich(3)
# print(talaba1.get_info())
#
# talaba1.update_bosqich()
# talaba1.update_bosqich()
# print(talaba1.get_info())
talaba5 = Talaba('Mirzohid', 'Xusainov', 2011)
print(dir(Talaba))

def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

print(see_methods(Talaba))
print(see_methods(talaba5))