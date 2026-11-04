# 20 BODLOGO

# task1
# too = [5, 3, 8, 1, 2]
# for i in range(len(too)):
#     for j in range(len(too) - 1 - i):
#         if too[j] > too[j + 1]:
#             tur = too[j]
#             too[j] = too[j + 1]
#             too[j + 1] = tur
# print(too)

# task2
# too = [4, 9, 2, 7, 1]
# for i in range(len(too)):
#     for j in range(len(too) - 1 - i):
#         if too[j] < too[j + 1]:
#             tur = too[j]
#             too[j] = too[j + 1]
#             too[j + 1] = tur
# print(too)

# task3
# too = [3, -2, 5, -7, 1]
# for i in range(len(too)):
#     for j in range(len(too) - 1 - i):
#         if too[j] > too[j + 1]:
#             tur = too[j]
#             too[j] = too[j + 1]
#             too[j + 1] = tur
# print(too)

# task4
# too = [4, 2, 4, 1, 2, 3]
# for i in range(len(too)):
#     for j in range(len(too) - 1 - i):
#         if too[j] > too[j + 1]:
#             tur = too[j]
#             too[j] = too[j + 1]
#             too[j + 1] = tur
# print(too)

# task5
# too = list(map(int, input().split()))
# for i in range(len(too)):
#     for j in range(len(too) - 1 - i):
#         if too[j] > too[j + 1]:
#             tur = too[j]
#             too[j] = too[j + 1]
#             too[j + 1] = tur
# print(too)

# task6
# ner = ["Saraa", "Bat", "Anu", "Bold"]
# for i in range(len(ner)):
#     for j in range(len(ner) - 1 - i):
#         if ner[j] > ner[j + 1]:
#             tur = ner[j]
#             ner[j] = ner[j + 1]
#             ner[j + 1] = tur
# print(ner)

# task7
# onoо = [75, 92, 60, 88, 70]
# for i in range(len(onoо)):
#     for j in range(len(onoо) - 1 - i):
#         if onoо[j] > onoо[j + 1]:
#             tur = onoо[j]
#             onoо[j] = onoо[j + 1]
#             onoо[j + 1] = tur
# print(onoо)

# task8
# too = [6, 2, 9, 1, 5]
# for j in range(len(too) - 1):
#     if too[j] > too[j + 1]:
#         tur = too[j]
#         too[j] = too[j + 1]
#         too[j + 1] = tur
# print(too)

# task9
# too = [5, 4, 3, 2, 1]
# toirog = 0
# for i in range(len(too)):
#     toirog += 1
#     for j in range(len(too) - 1 - i):
#         if too[j] > too[j + 1]:
#             tur = too[j]
#             too[j] = too[j + 1]
#             too[j + 1] = tur
# print(too)
# print(toirog)

# task10
# too = [5, 1, 4, 2, 8]
# swap_count = 0
# for i in range(len(too)):
#     for j in range(len(too) - 1 - i):
#         if too[j] > too[j + 1]:
#             tur = too[j]
#             too[j] = too[j + 1]
#             too[j + 1] = tur
#             swap_count += 1
# print(too)
# print(swap_count)

# task11
# too = [12, 5, 20, 8, 15]
# for i in range(len(too)):
#     for j in range(len(too) - 1 - i):
#         if too[j] < too[j + 1]:
#             tur = too[j]
#             too[j] = too[j + 1]
#             too[j + 1] = tur
# print(too[1])

# task12
# too = [4, -3, 0, -1, 7, -8, 2]
# for i in range(len(too)):
#     for j in range(len(too) - 1 - i):
#         if too[j] > too[j + 1]:
#             tur = too[j]
#             too[j] = too[j + 1]
#             too[j + 1] = tur
# print(too)

# task13
# too = [5, 3, 1, 4, 2]
# for i in range(len(too)):
#     for j in range(len(too) - 1 - i):
#         if too[j] > too[j + 1]:
#             tur = too[j]
#             too[j] = too[j + 1]
#             too[j + 1] = tur
#     print(too)

# task14
# too = [1, 2, 3, 4, 5]
# for i in range(len(too)):
#     solison = False
#     for j in range(len(too) - 1 - i):
#         if too[j] > too[j + 1]:
#             tur = too[j]
#             too[j] = too[j + 1]
#             too[j + 1] = tur
#             solison = True
#     if solison == False:
#         break
# print(too)

# task15
# too = [1, 2, 3, 5, 4]
# toirog = 0
# for i in range(len(too)):
#     solison = False
#     toirog += 1
#     for j in range(len(too) - 1 - i):
#         if too[j] > too[j + 1]:
#             tur = too[j]
#             too[j] = too[j + 1]
#             too[j + 1] = tur
#             solison = True
#     if solison == False:
#         break
# print(too)
# print(toirog)

# task16
# students = [
#     ["Bat", 75],
#     ["Saraa", 92],
#     ["Anu", 60],
#     ["Bold", 88]
# ]
# for i in range(len(students)):
#     for j in range(len(students) - 1 - i):
#         if students[j][1] > students[j + 1][1]:
#             tur = students[j]
#             students[j] = students[j + 1]
#             students[j + 1] = tur
# print(students)

# task17
# people = [
#     ["Bat", 19],
#     ["Anu", 17],
#     ["Bold", 21],
#     ["Saraa", 18]
# ]
# for i in range(len(people)):
#     for j in range(len(people) - 1 - i):
#         if people[j][1] > people[j + 1][1]:
#             tur = people[j]
#             people[j] = people[j + 1]
#             people[j + 1] = tur
# print(people[0][0])
# print(people[-1][0])

# task18
# too = [4, 2, 4, 1, 2, 4, 3]
# for i in range(len(too)):
#     for j in range(len(too) - 1 - i):
#         if too[j] > too[j + 1]:
#             tur = too[j]
#             too[j] = too[j + 1]
#             too[j + 1] = tur
# davhardсан = 0
# for i in range(len(too) - 1):
#     if too[i] == too[i + 1]:
#         davhardсан += 1
# print(too)
# print(davhardсан)

# task19
# products = [
#     ["Mouse", 25000],
#     ["Keyboard", 65000],
#     ["USB", 12000],
#     ["Headphone", 80000]
# ]
# for i in range(len(products)):
#     for j in range(len(products) - 1 - i):
#         if products[j][1] < products[j + 1][1]:
#             tur = products[j]
#             products[j] = products[j + 1]
#             products[j + 1] = tur
# for i in range(3):
#     print(products[i])

# task20
# too = [7, 3, 5, 1, 6, 2, 4]
# haritsuulalt = 0
# soliltsoo = 0
# toirog = 0
# for i in range(len(too) - 1):
#     toirog += 1
#     for j in range(len(too) - 1 - i):
#         haritsuulalt += 1
#         if too[j] > too[j + 1]:
#             tur = too[j]
#             too[j] = too[j + 1]
#             too[j + 1] = tur
#             soliltsoo += 1
# print("Jagsaalt:", too)
# print("Haritsuulalt:", haritsuulalt)
# print("Soliltsoo:", soliltsoo)
# print("Toirog:", toirog)

# task21
# toonuud = [7, 4, 9, 2, 6, 1, 8, 3]
# for i in range(len(toonuud)):
#     for j in range(len(toonuud)-1):
#         if toonuud[j] > toonuud[j+1]:
#             toonuud[j], toonuud[j+1] = toonuud[j+1], toonuud[j]
# print(toonuud)

# task22
ugnuud = ["apple", "hi", "banana", "cat", "python"]
for i in range(len(ugnuud)):
    for j in range(len(ugnuud)-1):
        if len(ugnuud[j]) > len(ugnuud[j+1]):
            ugnuud[j], ugnuud[j+1] = ugnuud[j+1], ugnuud[j]
print(ugnuud)