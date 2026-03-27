davlatlar = ['Russia', 'Bulgaria', 'Uzbekistan', "Aqsh", 'Kanada', 'Mexico']

print(sorted(davlatlar))
print(sorted(davlatlar, reverse=True))
print(davlatlar)

davlatlar.reverse()
print(davlatlar)

davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

juft_sonlar = list(range(120, 1201, 2))
print(juft_sonlar)

jami = sum(juft_sonlar)
print(jami)

ayirma = 1200 - 120
print("Eng katta qiymatdan eng kichik qiymat ayirmasi ", ayirma, "ga teng")

print("Ro'yhat ichida", (len(juft_sonlar)), "element bor")

print("Boshidagi 20ta qiymat", juft_sonlar[:20])
print("Oxiridagi 20ta qiymat", juft_sonlar[-20:])
 
taomlar = ['qovrilgan tuxum', 'palov', 'chuchvara', "makaron", "sho'rva"]
print(taomlar)

nonushta = taomlar[:]
print(nonushta)

nonushta.remove("palov")
nonushta.remove("chuchvara")
nonushta.remove("makaron")
nonushta.remove("sho'rva")

nonushta.append("saryog'")
nonushta.append("asal")

print(nonushta)

print(taomlar, "va", nonushta)

nonushta[0] = 'qaymoq va non'
nonushta = (tuple(nonushta))
print(nonushta)