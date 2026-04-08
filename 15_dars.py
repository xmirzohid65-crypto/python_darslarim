# # Modullar bilan ishlash
#
# a = 25 **(1/2)
# print(a)
#
# import math
#
# x=400
# print(math.sqrt(x))
#
# print(pow(5,3))
#
# from math import pi
#
# print(pi)
#
# print(math.log2(8))
# print(math.log10(100))
#
# import random as r
#
# son = r.randint(0,100)
# print(son)
#
# ismlar = ['mirzohid', 'alisher', 'muhammad', 'mahmud']
# ism = r.choice(ismlar)
# print(ism)
# print(r.choice(ism))
#
# x = list(range(10))
# print(x)
# r.shuffle(x)
# print(x)
#
# import math
# """Diametrni hisoblovchi"""
# diametr = lambda pi, r : 2*pi*r
# print(diametr(math.pi, 11))
#
# prodducts = lambda x,a : x**a
# print(prodducts(2,3))
#
# def daraja(n):
#     """Xning yginchi darajasini qaytaruvchi funksiya"""
#     return lambda x : x ** n
#
# kvdrt = daraja(2)
# kub = daraja(3)
# print(f"3-ning kvadrati: {kvdrt(3)}, kubi esa: {kub(3)}")
#
# from math import sqrt
#
# sonlar = list(range(11))
# ildizlar = list(map(sqrt, sonlar))
# print(sonlar)
# print(ildizlar)
#
# def daraja2(x):
#     """Sonning kvadratini qaytaruvchi funksiya"""
#     return x*x
#
# print(list(map(daraja2,sonlar)))
#
# """Sonning kvadratini qaytaruvchi funksiya, lambda usuli"""
# kvadratlar = list(map(lambda x : x*x, sonlar))
# print(kvadratlar)
#
# sonlar = list(range(11))
#
# kvadratlar = []
# for son in sonlar:
#     kvadratlar.append(son*son)
# print(kvadratlar)
#
# a = [4,5,6]
# b = [7,8,9]
# a_plyus_b = list(map(lambda x,y:x+y,a,b))
# print(a_plyus_b)
#
# ismlar = ['hasan', 'xusan', 'ali', 'vali']
# print(list(map(lambda matn:matn.upper(), ismlar)))
#
# import random as r
# sonlar = r.sample(range(100), 10)
#
# def juftlik(x):
#     """x, juft bo'lsa, aks xolda False qaytaruvchi funksiya"""
#     return x%2 == 0
#
# juft_sonlar = list(filter(juftlik, sonlar))
# print(sonlar)
# print(juft_sonlar)
#
# juft_sonlar2 = list(filter(lambda son: son%2 == 0, sonlar))
# print(sonlar)
# print(juft_sonlar2)
#
# mevalar = ['olma', 'shaftoli', 'o\'rik', 'tarvuz', 'banana', 'qovun']
# mevalar_harf = list(filter(lambda meva:meva.startswith('b'), mevalar))
# print(mevalar_harf)
#
# mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
# print(mevalar2)