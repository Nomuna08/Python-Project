# WHILE 20 BODLOGO

# task1
# n = int(input())
# i = 1
# while i <= n:
#     print(i)
#     i = i + 1

# task2
# n = int(input())
# while n >= 1:
#     print(n)
#     n = n - 1

# task3
# utga = int(input())
# i = 1 
# while i <= utga:
#     if i % 2 == 0:
#          print(i)
#     i = i + 1

# task4
# utga = int(input())
# i = 1 
# while i <= utga:
#     if i % 2 != 0:
#         print(i)
#     i = i + 1

# task5
# utga = int(input())
# i = 1
# a = 0
# while i <= utga:
#     a = a + i 
#     i = i + 1 
# print(a)

# task6
# utga = int(input())
# i = 1
# a = 0 
# while i <= utga:
#     if i % 2 == 0:
#         a = a + i 
#     i = i + 1
# print(a)

# task7
# utga = int(input())
# i = 1 
# while i <= utga:
#     if i % 3 == 0:
#         print(i)
#     i = i + 1
# print(i)

# task8
# n = int(input("heden too oruulah we:"))
# eyreg = 0
# sorog = 0
# teg = 0
# i = 1
# while i <= n:
#     toonuud = int(input("too oruulna uu:"))
#     if toonuud > 0:
#         eyreg = eyreg + 1
#     elif toonuud < 0:
#         sorog = sorog + 1
#     else:
#         teg = teg + 1
#     i = i + 1
# print("eyreg toonuud:", eyreg)
# print("sorog toonuud:", sorog)
# print("teg too:", teg)

# task9
# n = int(input("heden too oruulah uu:"))
# niit = 0
# i = 1
# while i <= n:
#     toonuud = int(input("too oruulna:"))
#     if toonuud > 0:
#         niit = niit + toonuud 
#     i = i + 1 
# print("eyreg toonuudiin niilber:", niit)

# task10
# n = int(input("heden too oruulah uu:"))
# i = 1 
# toonuud = int(input("too oruulna:"))
# ih = toonuud
# while i < n:
#     toonuud = int(input("too oruulna:"))
#     if toonuud > ih:
#         ih = toonuud
#     i = i + 1
# print("hamgiin ih too:", ih)

# task11
# n = int(input())
# baga = int(input())
# i = 1
# while i < n:
#     a = int(input())
#     if a < baga:
#         baga = a
#     i += 1 
# print(baga)

# task12
# n = int(input())
# i = 1
# while i <= n:
#     if i % 3 == 0 and i % 5 == 0:
#         print(i)
#     i += 1

# task13
# n = int(input())
# a = 0
# while n > 0:
#     a += 1
#     n //= 10
# print(a)

# task14
# n = int(input("toog oruulna:"))
# a = 0
# while n > 0:
#     d = n % 10
#     a = a + d
#     n = n // 10
# print(a)

# task15
# n = int(input("toog oruulna:"))
# urwuu = 0
# while n > 0:
#     d = n % 10
#     urwuu = urwuu * 10 + d 
#     n = n // 10
# print(urwuu)

# task16
# n = int(input("toog oruulna uu:"))
# o = n 
# urwuu = 0 
# while n > 0:
#     d = n % 10
#     urwuu = urwuu * 10 + d 
#     n = n // 10
# if o == urwuu:
#     print("palindrom")
# else:
#     print("palindrom bish)

# task17
# n = int(input())
# i = 1
# a = 0
# while i <= n:
#     if n % i == 0:
#         a = a + 1
#     i = i + 1
# if a == 2:
#     print("yes")
# else:
#     print("no")

# task18
# n = int(input())
# a = 2
# while a <= n:
#     i = 1
#     b = 0 
#     while i <= a:
#         if a % i == 0:
#             b = b + 1 
#         i = i + 1 
#     if b == 2:
#         print(a)
#     a = a + 1

# task19
# n = int(input())
# i = 1
# while i <= 10:
#     print(n, "*", i, "=", n*i)
#     i = i + 1

# task20
# n = input()
# while n != "python123":
#     n = input()
# print("zow")





##########################################################################################33

# BREAK CONTINUE 30 BODLOGO

# task1
# a = 0
# while True:
#     a += 1
#     if a > 10:
#         break
#     print(a)

# task2
# b = 0
# while True:
#     b += 1
#     if b > 20:
#         break
#     if b % 2 != 0:
#         continue
#     print(b)

# task3
# a = 0
# while True:
#     a += 1
#     if a > 20:
#         break 
#     if a % 2 == 0:
#         continue
#     print(a)

# task4
# a = 0
# while True:
#     a += 1
#     if a > 10:
#         break 
#     print("5 x", a, "=", 5 * a)

# task5
# n = int(input())
# a = 0
# while True:
#     a += 1
#     if a > n:
#         break 
#     print(a)

# task6
# n = int(input())
# while True:
#     if n < 1:
#         break 
#     print(n)
#     n -= 1

# task7
# a = 0
# while True:
#     a += 1
#     if a > 50:
#         break 
#     if a % 3 != 0:
#         continue
#     print(a)

# task8
# a = 0
# while True:
#     a += 1
#     if a > 30:
#         break 
#     if a % 5 == 0:
#         continue 
#     print(a)

# task9
# a = 0
# too =0
# while True:
#     a += 1
#     if a > 100:
#         break
#     if a % 2 != 0:
#         continue 
#     too += 1
# print(too)

# task10
# a = 0
# too = 0
# while True:
#     a += 1
#     if a > 100:
#         break 
#     if a % 7 != 0:
#         continue 
#     too += 1
# print(too)

# task11
# a = 1
# b = 0
# while True:
#     if a > 100:
#         break 
#     b = b + a 
#     a = a + 1
# print(b)

# task12
# a = 1
# b = 0
# while True:
#     if a > 50:
#         break 
#     if a % 2 != 0:
#         a = a + 1
#         continue 
#     b = b + a 
#     a = a + 1
# print(b)

# task13
# a = 1
# while True:
#     if a > 10:
#         break 
#     print(a)
#     a = a + 1

# task14
# a = 10
# while True:
#     if a < 1:
#         break 
#     print(a)
#     a = a - 1

# task15
# a = 1
# while True:
#     if a > 20:
#         break 
#     if a % 2 != 0:
#         a = a + 1
#         continue 
#     print(a)
#     a = a + 1

# task16
# n = int(input("n = "))
# a = 1
# b = 0 
# while True:
#     if a > n:
#         break 
#     b = b + a 
#     a = a + 1
# print(b)

# task17
# n = int(input("n = "))
# a = 0
# while True:
#     if n == 0:
#         break
#     a = a + 1
#     n = n // 10
# print(a)

# task18
# n = int(input("too = "))
# a = 0
# while True:
#     if n == 0:
#         break 
#     a = a + n % 10
#     n = n // 10 
# print(a)

# task19
# a = 1 
# while True:
#     if a == 5:
#         break 
#     print(a)
#     a = a + 1

# task20
# a = 10
# while True:
#     if a % 7 == 0:
#         print(a)
#         break
#     a = a + 1

# task21
# s = 0
# while True:
#     n = int(input("toogoo oruul = "))
#     if n == s:
#         break

# task22
# while True:
#     n = int(input("toog oruul = "))
#     if n == 0:
#         break 
#     print(n)

# task23
# a = 0
# while True:
#     n = int(input("toog oruul = "))
#     if n == 0:
#         break 
#     a = a + n 
# print(a)

# task24
# a = 0
# while a < 10:
#     a = a + 1
#     if a == 5:
#         continue 
#     print(a)

# task25
# a = 0
# while a < 20:
#     a = a + 1
#     if a % 2 == 0:
#         continue 
#     print(a)

# task26
# a = 0
# while a < 30:
#     a = a + 1 
#     if a % 3 == 0:
#         continue 
#     print(a)

# task27
# a = 0
# b = 0
# while b < 5:
#     n = int(input("toog oruul:"))
#     b = b + 1 
#     if n < 0:
#         continue 
#     a = a + n
# print(a)

# task28
# a = 1 
# b = 0 
# while True:
#     if a % 7 == 0:
#         print(a)
#         b = b + 1 
#     if b == 5:
#         break 
#     a = a + 1

# task29
# while True:
#     n = int(input("toog oruul = "))
#     if n == 0:
#         break 
#     if n < 0:
#         continue 
#     if n % 2 != 0:
#         continue 
#     print(n)

# task30
s = 17
while True:
    n = int(input("toog oruul:"))
    if n < 0:
        print("sorog too orohgui")
        continue 
    if n < s:
        print("baga")
    elif n > s:
        print("ih")
    else:
        print("zow taasan")
        break