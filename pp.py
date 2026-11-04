# NESTED FOR 10 BODLOGO 

# task1
# n = int(input())
# m = int(input())
# for i in range(1, n + 1):
#     a = 0
#     for j in range(1, m + 1):
#         b = int(input())
#         a = a + b 
#     d = a / m 
#     print(i, "r suragch: niit", a, ", dundaj", d)
#     if d >= 60:
#         print("tentssen")
#     else:
#         print("tentseegui")

# task2
# n = int(input())
# for i in range(1, n + 1):
#     m = int(input())
#     s = 0
#     for j in range(1, m + 1):
#         vne = int(input())
#         shirheg = int(input())
#         s = s + vne * shirheg 
#     print(i, "r toloh dvn:", s)
#     mongo = int(input())
#     if mongo >= s:
#         print("hariult:", mongo - s)
#     else:
#         print("dutuu mongo:", s - mongo)

# task3
# n = int(input("ajilchnii too:"))
# for i in range(n):
#     niit_tsalin = 0
#     for j in range(5):
#         tsag = int(input(str(j + 1) + "-r odriin ajilsan tsag:"))
#         if tsag <= 8:
#             niit_tsalin = niit_tsalin + tsag * 5000
#         else:
#             niit_tsalin = niit_tsalin + 8 * 5000 + (tsag - 8) * 7500
#     print(str(i + 1) + " r ajilchdiin niit tsalin:", niit_tsalin)

# task4
# n = int(input("hvnii too:"))
# m = int(input("sariin too:"))
# for i in range(n):
#     zeel = int(input("anhnii zeel:"))
#     niit = 0
#     for j in range(m):
#         tololtvvd = int(input("sariin tololtvvd"))
#         if zeel > 0:
#             zeel = zeel = tololtvvd 
#             niit = niit + tololtvvd 
#         print(str(i +  1) + "r hvmvvs, " + str(j + 1) + "r sariin daraa uldegdel:", zeel) 
#     print("bugdiine tolson:",  niit)

# task5
# n = int(input("odor too:"))
# m = int(input("odort uildwerleh too:"))
# for i in range(n):
#     niit = 0
#     for j in range(m):
#         toonuud = int(input("bvteegdehvvnii too:"))
#         niit = niit + toonuud
#     hairtsag = niit // 12 
#     vldegdelvvd = niit % 12
#     print(str(i + 1) + "r odor: niit", niit, ", bvten hairtsag", hairtsag, ", vldegdel", vldegdelvvd)

# task6
# n = int(input())
# m = int(input())
# for i in range(n):
#     hvmvvs = 0
#     niit = 0
#     for j in range(m):
#         a = int(input())
#         b = int(input())
#         hvmvvs = hvmvvs - a + b 
#         niit = niit + b 
#         print(j + 1, "r buudliin daraa:", hvmvvs, "hvn")
#     print("niit suusan:", niit)
#     print("orlogo:", niit * 1000)

# task7
# n = int(input("n = "))
# for i in range(1, n + 1):
#     t = 0
#     niit = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             t = t + 1
#             niit = niit + 1
#     print(str(i) + "i", t, "huwisagchtai, niilber", niit)

# task8
# n = int(input("n = "))
# too = 0
# for i in range(1, n + 1):
#     for j in range(i, n + 1):
#         if i + j == n:
#             print(i, "+", j, "=", n)
#             too = too + 1
# print("niit:", too, "hos")

# task9
# n = int(input("n = "))
# too = 0
# for i in range(0, n // 2000 + 1):
#     a = i * 2000
#     b = n - a
#     if b % 1000 == 0:
#         print("1000:", b // 1000, "2000:", i)
#         too = too + 1
# print("niit:", too)

# task10
n = int(input("n = "))
too = 0
for i in range(1, n + 1):
    for j in range(i, n + 1):
        if i * j == n:
            ylgaa = j - i 
            print(i, "x", j, "=", n, ", ylgawar", ylgaa)
            too = too + 1
print("niit:", too, "hos")