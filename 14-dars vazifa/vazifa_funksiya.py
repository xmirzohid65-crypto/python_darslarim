def sonlar_kopaytmasi(*sonlar):
    """Kiritilgan sonlarni kopaytirib beruvchi funksiya"""
    natija = 1
    for son in sonlar:
        natija *= son
    return natija

def talaba_info(ism, familiya, **malumotlar):
    """Talaba haqida ma'lumot qytaruvchi funksiya"""
    info = {'ism': ism, 'familiya':familiya}
    info.update(malumotlar)
    return info

def discount(*pullar):
    """Hisoblab keyin chegirma bilan chiqaruvchi funksiya"""

    jami = sum(pullar)

    sale = 10
    
    if jami >= 100000:
        chegirma = jami * sale / 100
    else:
        chegirma = 0

    barchasi = jami - chegirma
    print(f"Jami narx: {jami} so'm")
    print(f"Chegirma 10%: {chegirma} so'm")
    print(f"To'lov: {barchasi} so'm")

def join_words(*matn, **ajratuvchi):
    delimiter = ajratuvchi.get('delimiter', ' ')
    javob = ""
    for i, word in enumerate(matn):
        javob += word
        if i < len(matn) - 1:
            javob += delimiter
    return javob