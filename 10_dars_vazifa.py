# Quyidagi ma’lumotdan har bir o‘quvchining o‘rtacha bahosini hisoblang.

students = {
    "Ali": [80, 90, 85],
    "Vali": [70, 60, 75],
    "Sami": [95, 88, 92]
}

for ism, baho in students.items():
    print(f"{ism}ning o'rtacha bahosi", end=' ')
    print(f"{min(baho)}")

# Narxi 100 dan katta bo‘lgan mahsulotlarni chiqaring.

products = [
    {"name":"olma", "price":120},
    {"name":"anor", "price":90},
    {"name":"banan", "price":150}
]

for product in products:
    if product['price'] > 100:
        print(product)

# 18 yoshdan katta foydalanuvchilarni chiqaring.

users = [
    {"name":"Ali", "age":20},
    {"name":"Vali", "age":16},
    {"name":"Sami", "age":25}
]

for foydalanuvchi in users:
    if foydalanuvchi['age'] > 18:
        print(f"{foydalanuvchi}")

# Har bir kursdagi o‘quvchilar sonini aniqlang.

courses = {
    "python": ["Ali","Vali","Sami"],
    "django": ["Ali","Sami"],
    "ai": ["Vali","Sami","Jasur"]
}

for course, students in courses.items():
    print(f"{course} kursida {len(students)} ta o‘quvchi bor")

# Eng katta sonni toping:

numbers = [
    [4,7,2],
    [9,1,5],
    [3,8,6]
]

print(max(sum(numbers, [])))

# Faqat active foydalanuvchilarni chiqaring.

data = {
    "users":[
        {"name":"Ali", "active":True},
        {"name":"Vali", "active":False},
        {"name":"Sami", "active":True}
    ]
}

for active in data["users"]:
    if active['active'] == True:
        print(f"{active}")