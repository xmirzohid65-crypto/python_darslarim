# OOP bilan ishlash va tushunchalri

class Talaba:
    """Talaba haqida class yaratamiz"""
    def init(self,ism,familiya,tyil):
        """Talaba classini qaytaruvchi"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil

    def get_name(self):
        """Talaba ismini qaytaruvchi"""
        return self.ism

    def get_last_name(self):
        """Talaba familiyasini qaytaruchi"""
        return self.familiya

    def get_age(self, yil=2026):
        """Talaba yoshini qaytaruvchi"""
        return yil - self.tyil

    def get_full_name(self):
        return f"{self.ism} {self.familiya}"

    def tanishtir(self):
        """Talabani tanishtirib beruvchi"""
        print(f"Ismim {self.ism} {self.familiya}, {self.tyil}-yilda tu'g'ilganman")

talaba1 = Talaba('Ali', 'Valiyev', 2011)

print(talaba1.ism)
print(talaba1.familiya)
print(talaba1.tyil)

talaba2 = Talaba('Mirzohid', 'Xusainov', 2011)
talaba3 = Talaba('Mansur', 'Palvanov', 2000)
talaba4 = Talaba('Maxmud', 'Otabayev', 2012)

print(talaba4.tanishtir())
print(talaba2.familiya)
print(talaba3.ism)

print(talaba1.get_full_name())
print(talaba3.get_age())
print(talaba2.get_name())
print(talaba4.get_last_name())

# class User:
#     def init(self,ism,familiya,email):
#         self.ism = ism
#         self.familiya = familiya
#         self.email = email
        
#     def describe():
#         pass
#     def get_email():
#         pass