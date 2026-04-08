class User:
    """User haqida class yaratdim"""
    def __init__(self,ism,familiya,email,tel,):
        self.ism = ism
        self.familiya = familiya
        self.email = email
        self.tel = tel

    def user_ism(self):
        """User ismini qaytaruvchi"""
        return self.ism

    def user_familiya(self):
        """User familiyasini qaytaruchi"""
        return self.familiya

    def user_age(self):
        """User emailini qaytaruvchi"""
        return self.email
    
    def telfon_r(self):
        """User telefon raqamini qaytaruvchi"""
        return self.tel    
    
    # Classga qo'shilgan metod
    def tanishtir(self):
        """Talabani tanishtirib beruvchi"""
        print(f"Foydalanuvchi {self.ism} {self.familiya}, email pochtangiz {self.email}, telefon raqaamingiz: {self.tel}")

user1 = User('Mirzohid', 'Xusainov', 'qwerty123@gmail.com', 995050599)
user2 = User('Alisher', 'Azatov', 'admin987@gmail.com', 997070799)
user3 = User('Maxmud', 'Otabaev', 'hacker@gmail.com', 979070979)
user4 = User('Bilol', 'Pulatov', 'gaming07@gmail.com', 779097808)

print(user1.tanishtir())
# Obyektlar

print(f"{user4.ism} {user4.familiya}")
print(f"{user3.ism} email: {user3.email}")
print(f"{user1.familiya}sizning emailingiz: {user1.email} va telefon raqamingiz {user1.tel}")