ismlar = "Alisher, Donyor, Muhammad"
print("Alisher nima gap yaxshimisan ishlaring yaxshimi")
print("Donyar sog' omonmisan uyingdagilar yaxshimi")
print("Muhammad  qalaysan to'garaklar charchatmayapdimi")

sonlar = [1, 2, -3, 2.5, -0.6]

print(sonlar)

sonlar[1] = sonlar[1] + 2
sonlar[0] = 5
sonlar[4] = 0.6

print(sonlar)

print("5 + 2.5 - 0.6")
print("Javob:", 5 + 2.5 - (0.6))

print("4 - 0.6 * 3 // 5")
print("Javob:", 4 - 0.6 * 3 // 5)

print("4 // 4 + 5 * 2.5")
print("Javob:", 4 // 4 + 5 * 2.5)

t_shaxslar = ["Nikolas Tesla", "Albert Einstein", "Stalin"]
z_shaxslar = ["Elon Mask", "Jensen Huang", "Bill Gates"]

nikolas = t_shaxslar.pop(0)
jansen = z_shaxslar.pop(1)

print("Men qadimiy shaxslardan", nikolas , "va\n Zamonaviy shaxslardan", jansen , "bilan suhbatlashishni xohlardim")

friends = []

friends.append("Alisher")
friends.append("Maxmud")
friends.append("Behruz")
friends.append("Temur")
friends.append("Azim")

print(f"Mehmonga chaqirgan do'stlarim:{friends}")

friends.remove("Maxmud")
friends.remove("Azim")

print(f"Mehmonga kelo olgan do'stlarim:{friends}")

friends.append("Salim")
friends.insert(0, "Ahmat")
friends.insert(3, "Doniyor")

print(friends)