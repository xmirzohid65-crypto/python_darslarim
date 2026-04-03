import vazifa_funksiya

natija_son = vazifa_funksiya.sonlar_kopaytmasi(2, 3, 4)
print(natija_son)  

talaba1 = vazifa_funksiya.talaba_info('Ali', 'Palvanov', tel='997977959', email='ali@mail.com')
talaba2 = vazifa_funksiya.talaba_info('Vali', 'Mansurov', kurs=3, fakultet='Informatika')

print(talaba1)
print(talaba2)

vazifa_funksiya.discount(100000, 120000, 200000)

from vazifa_funksiya import join_words

print(join_words("Python", "is", "awesome", delimiter="-"))