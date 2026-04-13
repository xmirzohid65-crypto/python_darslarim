# Voris class va Super class


class Shaxs:
    """Shaxs haqidagi class"""
    def __init__(self,ism,faniliya,passport,tyil):
        self.ism = ism
        self.familiya = faniliya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        """Shaxs class methodi"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport: {self.passport}, {self.tyil}-yilda tug'ilgan"
        return info

    def get_age(self, yil=2026):
        """Yosh qaytaruvchi method"""
        return yil - self.tyil

# inson = Shaxs("Mirzohid", "Xusainov", "MM22XX0011", 1981)
# print(f"{inson.get_info()}, {inson.get_age()} yoshda")


class Ogil(Shaxs):
    """O'g'il classi"""
    def __init__(self,ism,familiya,passport,tyil,idraqam,manzil):
        """O'g'ilning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil

    def get_id(self):
        """Id raqamni qaytaruvchi method"""
        return self.idraqam

    def get_bosqich(self):
        """O'g'ilning nechanchi kursligini qaytaruvchi method"""
        return self.bosqich

    def get_info(self):
        """O'g'il class methodi"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-kurs talabasi, ID: {self.get_id()}"
        return info

# bola = Ogil("Otush", "Sharipov", 'FFG410607', 2006, 12325255437338)
# print(f"{bola.get_info()}, {bola.get_age()} yoshda")
# print(f"Id raqami {bola.get_id()}")
# print(f"Bola {bola.get_bosqich()}-kursda")
#
# print(bola.get_info())
# print(inson.get_info())


class Manzil:
    """Manzil qaytaruvchi class"""
    def __init__(self, viloyat,shahar,kocha,uy):
        self.viloyat = viloyat
        self.shahar = shahar
        self.kocha = kocha
        self.uy = uy
    def get_manzil(self):
        """Manzil qaytaruvchi method"""
        manzil = f"{self.viloyat} viloyati, {self.shahar} shahari, "
        manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
        return manzil

talaba_manzil = Manzil("Xorazm","Urganch", 'Sharq', 38)
talaba = Ogil("Salim", "Azimov", 'FFQ6706011', 2008, 12325212343733, talaba_manzil)
print(talaba.get_info())
print(talaba.manzil.get_manzil())

# Inkapsuliyatsiya

from uuid import uuid4

class Avto:
    __num_avto = 0
    """Avtomobil haqida ma'lumot qaytaruvchi class"""
    def __init__(self, make, model, rang, yil, narh, km=0):
        """Avto class xususiyati"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id

    def add_km(self,km):
        """Mashina kmni ustuga km qo'shuvchi method"""
        if km >= 0:
            self.__km += km
        else:
            print("Mashina kmni kamaytirib bo'lmaydi!!!")

    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto

# avto1 = Avto('GM', 'Malibu', 'qizil', '2025', 32000, 10000)
# print(avto1.get_km())
# print(avto1.get_id())
#
# avto1.add_km(10010)
# print(avto1.get_km())

avto2 = Avto('GM', 'Gentra', 'qora', '2023', 32000, 10000)
avto3 = Avto('GM', 'Nexia 3', 'oq', '2022', 18000, 12355)
avto4 = Avto('GM', 'Cobalt Midnight', 'darkmoon', '2025', 16000, 5000)
print(Avto.get_num_avto())