class Shaxs:
    """Shaxs haqidagi class"""
    __shaxs_num = 0
    def __init__(self, ism, familiya, tyil, passport = "FFG410607"):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.__passport = passport
        Shaxs.__shaxs_num += 1
    
    # Inkapsuliyatsiya
    def get_passport_shaxs(self):
        return self.__passport

    def get_ism(self):
        return self.ism
    
    def get_familiya(self):
        return self.familiya
    

    def get_malumot(self):
        return f"{self.get_ism()} {self.get_familiya()} sizning passport seriyangiz: {self.get_passport_shaxs()}"
    

    # @Class methodi
    @classmethod
    def get_shaxs_num(cls):
        return cls.__shaxs_num

from uuid import uuid4
class Talaba():
    """Talaba classi"""
    __talaba_num = 0
    def __init__(self, ism, familiya, tyil, sharif = 'Davronovich'):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.sharif = sharif
        self.__id = uuid4()
        Talaba.__talaba_num += 1
    
    # Inkapsuliyatsiya

    def get_sharif(self):
        return

    def get_id_talaba(self):
        return self.__id 

    def get_tyil_talaba(self):
        return self.tyil
    
    def get_ism_talaba(self):
        return self.ism
    
    def familiya_talaba(self):
        return self.familiya
    
    def get_talaba_son(self):
        return
    
    def get_info(self):
        return f"{self.get_ism_talaba()} siz {self.get_tyil_talaba()}-yilda tug'ilgansiz va passport id raqamingiz>>>{self.get_id_talaba()}"
    
    # @Class methodi
    @classmethod
    def get_talaba_num(cls):
        return cls.__talaba_num
    
inson = Shaxs("Alijon", 'Valiyev', 2000)
print(inson.get_malumot())
talaba1 = Talaba("Jahongir","Alijonov", 2006)
print(talaba1.get_info())

print(Shaxs.get_shaxs_num())
print(Talaba.get_talaba_num())