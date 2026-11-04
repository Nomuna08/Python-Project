# task
# toonuud = [3, 7, 12, 18, 25, 31, 40]
# haih_too = int(input("Too oruul: "))
# ehlel = 0
# tugsgul = len(toonuud) - 1
# olson = False
# while ehlel <= tugsgul:
#     dund = (ehlel + tugsgul) // 2
#     if toonuud[dund] == haih_too:
#         olson = True
#         break
#     elif toonuud[dund] < haih_too:
#         ehlel = dund + 1
#     else:
#         tugsgul = dund - 1
# if olson:
#     print("Oldloo")
# else:
#     print("Oldsongui")

# task2
# toonuud = [5, 10, 15, 20, 25, 30]
# haih_too = int(input("Too oruul: "))
# ehlel = 0
# tugsgul = len(toonuud) - 1
# olson = False
# while ehlel <= tugsgul:
#     dund = (ehlel + tugsgul) // 2
#     if toonuud[dund] == haih_too:
#         print(dund)
#         olson = True
#         break
#     elif toonuud[dund] < haih_too:
#         ehlel = dund + 1
#     else:
#         tugsgul = dund - 1
# if olson == False:
#     print(-1)

# task3
# toonuud = [4, 9, 14, 19, 24, 29, 34]
# ehlel = 0
# tugsgul = len(toonuud) - 1
# while ehlel <= tugsgul:
#     dund = (ehlel + tugsgul) // 2
#     if toonuud[dund] == 4:
#         print(dund)
#         break
#     elif toonuud[dund] < 4:
#         ehlel = dund + 1
#     else:
#         tugsgul = dund - 1

# task4
# toonuud = [6, 12, 18, 24, 30, 36, 42]
# ehlel = 0
# tugsgul = len(toonuud) - 1
# while ehlel <= tugsgul:
#     dund = (ehlel + tugsgul) // 2
#     if toonuud[dund] == 42:
#         print(dund)
#         break
#     elif toonuud[dund] < 42:
#         ehlel = dund + 1
#     else:
#         tugsgul = dund - 1

# task5
# toonuud = [10, 20, 30, 40, 50, 60]
# haih_too = int(input("Too oruul: "))
# ehlel = 0
# tugsgul = len(toonuud) - 1
# olson = False
# while ehlel <= tugsgul:
#     dund = (ehlel + tugsgul) // 2
#     if toonuud[dund] == haih_too:
#         olson = True
#         break
#     elif toonuud[dund] < haih_too:
#         ehlel = dund + 1
#     else:
#         tugsgul = dund - 1
# if olson:
#     print("Oldloo")
# else:
#     print("Haih too baihgui")

# task6
toonuud = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32]

haih_too = int(input("Too oruul: "))

ehlel = 0
tugsgul = len(toonuud) - 1
alham = 0

while ehlel <= tugsgul:
    dund = (ehlel + tugsgul) // 2
    alham += 1

    if toonuud[dund] == haih_too:
        break
    elif toonuud[dund] < haih_too:
        ehlel = dund + 1
    else:
        tugsgul = dund - 1

print(alham)