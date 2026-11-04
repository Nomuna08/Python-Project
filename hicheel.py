# PYTHON SET BA DICTIONARY DASGALUUD

# task1
# nums = [1, 2, 2, 3, 4, 4, 5]
# nums = set(nums)
# print(nums)

# task2
# fruits = {"apple", "banana"}
# fruits.add("oronge")
# print(fruits)

# task3
# fruits = {"apple", "banana", "orange"}
# fruits.remove("banana")
# print(fruits)

# task4
# nums = {10, 20, 30, 40}
# if 20 in nums:
#     print("yes")
# else:
#     print("no")

# task5
# n = input().split()
# n = set(n)
# print(len(n))

# task6
# names = ["Bat", "Sara", "Bat", "Bold", "Sara", "Anu"]
# names = set(names)
# print(len(names))

# task7
# a = {1, 2, 3}
# b = {3, 4, 5}
# n = a | b 
# print(n)

# task8
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# n = a & b
# print(n)

# task9
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# n = a - b
# print(n)

# task10
# python_students = {"Bat", "Sara", "Bold", "Anu"}
# java_students = {"Sara", "Bold", "Temuulen"}
# suragchid = python_students & java_students
# print(suragchid)

# task11
# python_students = {"Bat", "Sara", "Bold", "Anu"}
# java_students = {"Sara", "Bold", "Temuulen"}
# suragchid = python_students ^ java_students
# print(suragchid)

# task12
# word = input()
# letters = set(word)
# print(len(letters))

# task13
# suragch = {"name": "bat",
#            "age": 18,
#            "score": 95
#            }
# print(suragch)

# task14
# student = {
#     "name": "Sara",
#     "age": 19,
#     "score": 90
# }
# print(student["name"])

# task15
# student = {
#     "name": "Bat",
#     "age": 18,
#     "score": 85
# }
# student["score"] = 98
# print(student)

# task16
# student = {
#     "name": "Anu",
#     "age": 18
# }
# student["city"] = "ulaanbaatar"
# print(student)

# task17
# student = {
#     "name": "Bold",
#     "age": 20,
#     "score": 88
# }
# del student["age"]
# print(student)

# task18
# car = {
#     "brand": "Toyota",
#     "model": "Prius",
#     "year": 2015
# }
# print(car.keys())

# task19
# car = {
#     "brand": "Toyota",
#     "model": "Prius",
#     "year": 2015
# }
# print(car.values())

# task20
# student = {
#     "name": "Bat",
#     "age": 18,
#     "score": 95
# }
# for key, value in student.items():
#     print(key, value)

# task21
# student = {
#     "name": "Sara",
#     "age": 19,
#     "score": 92
# }
# if "score" in student:
#     print("yes")
# else:
#     print("no")

# task22
# product = {
#     "name": "Keyboard",
#     "price": 120000,
#     "stock": 5
# }
# if product["stock"] > 0:
#     print("available")
# else:
#     print("out of stock")

# task23
# scores = {
#     "Bat": 80,
#     "Sara": 95,
#     "Bold": 70,
#     "Anu": 88
# }
# for name, score in scores.items():
#     if score >= 80:
#         print(name)

# task24
# scores = {
#     "Bat": 80,
#     "Sara": 95,
#     "Bold": 70,
#     "Anu": 88
# }
# print(max(scores.values()))

# task25
# sales = {
#     "Monday": 10,
#     "Tuesday": 15,
#     "Wednesday": 20
# }
# print(sum(sales.values()))

# task26
# n = input().split()
# a = {}
# for u in n:
#     if u in a:
#         a[u] += 1
#     else:
#         a[u] = 1
# for u, num in a.items():
#     print(u, num)

# task27
# students = {
#     "Bat": ["Python", "Java"],
#     "Sara": ["Python", "C++"],
#     "Bold": ["Java", "Python"]
# }
# hicheelvvd = set()
# for student in students:
#     for hicheel in students[student]:
#         hicheelvvd.add(hicheel)
# for hicheel in hicheelvvd:
#     print(hicheel)

# task28
# students = {
#     "Bat": "Ulaanbaatar",
#     "Sara": "Darkhan",
#     "Bold": "Ulaanbaatar",
#     "Anu": "Erdenet",
#     "Temuulen": "Darkhan"
# }
# hotuud = set(students.values())
# print(len(hotuud))

# task29
# students = {
#     "Bat": "Ulaanbaatar",
#     "Sara": "Darkhan",
#     "Bold": "Ulaanbaatar",
#     "Anu": "Erdenet"
# }
# for ner , hot in students.items():
#     if hot == "ulaanbaatar":
#         print(ner)

# task30
# data = {
#     "a": 10,
#     "b": 20,
#     "c": 10,
#     "d": 30,
#     "e": 20
# }
# values = set(data.values())
# print(values)





###########################################################################

# DUND TVWSHINII BODLOGO

# task1
# user1 = {"Bat", "Sara", "Bold", "Anu"}
# user2 = {"Bold", "Anu", "Temuulen", "Naraa"}
# result = user1 & user2 
# print(result)

# task2
# players = {"Bat", "Sara", "Bold", "Anu", "Naraa", "Temuulen"}
# played = {"Bat", "Bold", "Naraa"}
# result = players - played
# print(result)

# task3
# team_a = {"Bat", "Bold", "Anu", "Sara"}
# team_b = {"Anu", "Sara", "Naraa", "Temuulen"}
# result = (team_a - team_b) | (team_b - team_a)
# print(result)

# task4
# known = {"Python", "HTML", "CSS"}
# required = {"Python", "JavaScript", "SQL"}
# result = required - known 
# for u in result:
#     print(u)

# task5

# subjects = [
#     "Python",
#     "Math",
#     "Python",
#     "English",
#     "Math",
#     "Physics"
# ]
# u = set(subjects)
# print("oor hicheel too:", len(u))
# for v in u:
#     print(v)

# task6
# password = input("password")
# l = set(password)
# print(l)
# print(len(l))

# task7
# n = input()
# m = input()
# r = set(n)| set(m)
# print(len(r))

# task8
# students = {
#     "Bat": 75,
#     "Sara": 92,
#     "Bold": 61,
#     "Anu": 88,
#     "Naraa": 54
# }
# for name, score in students.items():
#     if score >= 90:
#         print(name, "- excellent")
#     elif score >= 60:
#         print(name, "-pass")
#     else:
#         print(name, "-fail")

# task9
# products = {
#     "apple": 3000,
#     "banana": 2500,
#     "milk": 4500,
#     "bread": 3500
# }
# n = input()
# m = int(input())  
# too = products[n] * m
# print("toonuud:", too)

# task10
# sales = {
#     "keyboard": 15,
#     "mouse": 23,
#     "monitor": 8,
#     "headset": 17
# }
# max_n = ""
# max_t = 0
# for n, t in sales.items():
#     if t > max_t:
#         max_t = t 
#         max_n = n
# print(max_n, max_t)

# task11
# employees = {
#     "Bat": 1500000,
#     "Sara": 1800000,
#     "Bold": 1300000,
#     "Anu": 2100000
# }
# for n, s in employees.items():
#     if s < 1500000:
#         s = s * 1.2
#         print(n, s)

# task12
# people = {
#     "Bat": 17,
#     "Sara": 21,
#     "Bold": 19,
#     "Anu": 16,
#     "Naraa": 25
# }
# for ner, nas in people.items():
#     if nas >= 18:
#         print(ner)

# task13
# scores = {
#     "Bat": 70,
#     "Sara": 85,
#     "Bold": 60,
#     "Anu": 95
# }
# for ner in scores:
#     scores[ner] = scores[ner] + 5 
#     if scores[ner] > 100:
#         scores[ner] = 100
#     print(ner, "->", scores[ner])

# task14
# products = {
#     "keyboard": 120000,
#     "mouse": 50000,
#     "monitor": 450000,
#     "headset": 80000
# }
# n = int(input())
# for ner, value in products.items():
#     if value == n:
#         print(ner)

# task15
# students = {
#     "Bat": "Ulaanbaatar",
#     "Sara": "Darkhan",
#     "Bold": "Ulaanbaatar",
#     "Anu": "Erdenet",
#     "Naraa": "Darkhan",
#     "Temuulen": "Ulaanbaatar"
# }
# n = input()
# m = set()
# for ner, u in students.items():
#     if u == n:
#         m.add(ner)
# print(m)

# tsk16
# games = {
#     "Bat": {"CS2", "Dota2"},
#     "Sara": {"Valorant", "CS2"},
#     "Bold": {"Dota2", "WoW"},
#     "Anu": {"CS2", "WoW"}
# }
# for ner, togloom in games.items():
#     if "CS2" in togloom:
#         print(ner)

# task17
# games = {
#     "Bat": {"CS2", "Dota2"},
#     "Sara": {"Valorant", "CS2"},
#     "Bold": {"Dota2", "WoW"},
#     "Anu": {"CS2", "WoW"}
# }
# n = set()
# for togloom in games.values():
#     n = n.union(togloom)
#     print(n)

# task18
# games = {
#     "Bat": {"CS2", "Dota2"},
#     "Sara": {"Valorant", "CS2"},
#     "Bold": {"Dota2", "WoW"},
#     "Anu": {"CS2", "WoW"}
# }
# for ner, togloom in games.items():
#     if "CS2" in togloom and "WoW" in togloom:
#         print(ner)

# task19
# skills = {
#     "Bat": {"Python", "HTML", "CSS"},
#     "Sara": {"Python", "JavaScript"},
#     "Bold": {"HTML", "CSS", "JavaScript"},
#     "Anu": {"Python", "SQL", "JavaScript"}
# }
# for ner, chadwar in skills.items():
#     if "Python" in chadwar and "JavaScript" in chadwar:
#         print(ner)

# task20
# employees = {
#     "Bat": {"English", "Mongolian"},
#     "Sara": {"English", "Korean"},
#     "Bold": {"Mongolian", "Japanese"},
#     "Anu": {"English", "Japanese"}
# }
# for ner, hel in employees.items():
#     if "English" in hel and "Korean" not in hel:
#         print(ner)

# task21
# web_users = {"Bat", "Sara", "Bold", "Anu"}
# mobile_users = {"Sara", "Anu", "Naraa"}
# n = web_users & mobile_users 
# print(n)
# print("niit:", len(n))

# task22
# status = {
#     "Bat": "online",
#     "Sara": "offline",
#     "Bold": "online",
#     "Anu": "offline",
#     "Naraa": "online"
# }
# online = set()
# for ner, u in status.items():
#     if u == "online":
#         online.add(ner)
# print(online)
# ner = input("heree oruulaarai:")
# if status[ner] == "online":
#     print("online")
# else:
#     print("offline")

# task23
# courses = {
#     "Python": {"Bat", "Sara", "Bold"},
#     "JavaScript": {"Sara", "Anu", "Bold"},
#     "SQL": {"Bat", "Anu"}
# }
# n = input("neree oruulaarai:")
# for course, suragch in courses.items():
#     if n in suragch:
#         print(course)

# task24
courses = {
    "Python": {"Bat", "Sara", "Bold"},
    "JavaScript": {"Sara", "Anu", "Bold"},
    "SQL": {"Bat", "Anu"}
}
suragchid = {}
for course, nersvvd in courses.items():
    for ner in nersvvd:
        if ner not in suragchid:
            suragchid[ner] = 0
        suragchid[ner] += 1
max_count = max(suragchid.values())
for ner, count in suragchid.items():
    if count == max_count:
        print(ner, count)