class Avto:
    def __init__(self, model, rang, korobka, narh, kilometr=0):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.kilometr = kilometr

    def get_info(self):
        return f"{self.rang} {self.model}, {self.korobka} kоrobkа, narxi: {self.narh}$, yurgan: {self.kilometr} km"

    def update_km(self, km):
        if km >= self.kilometr:
            self.kilometr = km
        else:
            print("Kilometrni kamaytirib bo'lmaydi!")

class Avtosalon:
    def __init__(self, nomi, manzil):
        self.nomi = nomi
        self.manzil = manzil
        self.avtolar = []

    def add_avto(self, avto):
        self.avtolar.append(avto)

    def get_avtolar(self):
        return [avto.get_info() for avto in self.avtolar]

avto1 = Avto("Cobalt", "oq", "avtomat", 12000)
avto2 = Avto("Malibu", "qora", "avtomat", 25000, 5000)

avto1.update_km(100)
avto2.update_km(6000)

salon = Avtosalon("GM Uzbekistan", "Toshkent")

salon.add_avto(avto1)
salon.add_avto(avto2)

print(avto1.get_info())
print(avto2.get_info())

print("\nAvtosalondagi avtomobillar:")
for info in salon.get_avtolar():
    print(info)

print("\nAvto klass atributlari:")
print(dir(avto1))