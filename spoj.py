#task1
# a, b, c = map(int, input().split())
# p = a + b + c
# print(p)

# task2
# a, b = map(int, input().split())
# n = (a + b)
# print(n)

# task3
# a = int(input())
# v = a ** 3
# s = 6 * a ** 2
# print(v, s)

# task4
# a, b = map(int, input().split())
# s = a * b
# p = (a + b)*2
# print(s, p)

# task5
# x = int(input())
# y = 3 * x - 5
# print(y)

# task6
# x = int(input())
# a = x ** 2
# b = 4 * a
# c = 3 * x
# print(b - c + 5)

# task7
# a = int(input())
# print(a % 10)

# task8
# a = int(input())
# print(a // 10 % 10)

# task9
# a = int(input())
# print(a // 10 * (a % 10))

# task10
# a, b, c = map(int, input().split())
# h = (a + b + c)
# print(h)

# task11
# a = int(input())
# print(a // 60, a % 60)

# task12
# a = int(input())
# print(a // 3600, a % 3600 // 60, a % 60)

# task13
# a, b = map(int, input().split())
# print(a * 60 + b)

# task14
# a, b, c = map(int,input().split())
# print(a * 3600 + b * 60 + c)

# task15
# a = int(input())
# print(a // 24, a % 24)

# task16
# a, b = map(int, input().split())
# print(a * 24 + b)

# task17
# a = int (input())
# print(a // 12, a % 12)

# task18
# a, b = map(int, input().split())
# print(a * 12 + b)

# task19
# a, b = map(int, input().split())
# if a > b:
#     print(a)
# else:
#     print(b)

# task20
# a, b = map(int, input().split())
# if a < b:
#     print(a)
# else:
#     print(b)

# task21
# a, b, c = map(int, input().split())
# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# else:
#     print(c)

# task22
# a, b, c, d = map(int, input().split())
# if a < b and a < c and a < d:
#     print(a)
# elif b < a and b < c and b < d:
#     print(b)
# elif c < a and c < b and c < d:
#     print(c)
# else:
#     print(d)

# task23
# a = list(map(int, input().split()))
# s = 0
# for i in a:
#     if i > 80:
#         s += i
# print(s)

# task24
# a = list(map(int, input().split()))
# p = 1
# for i in a:
#     if i < 5:
#         p *= i
# print(p)

# task25
# a = list(map(int, input().split()))
# s = 0
# for i in a:
#     if i % 2 == 0:
#         s += i
# print(s)

# task26
# a = list(map(int, input().split()))
# p = 1
# for i in a:
#      if i % 2 != 0:
#          p *= i
# print(p)

# task27
# a, b, c = map(int, input().split())
# count = 0
# if a == 5:
#     count += 1
# if b == 5:
#     count += 1
# if c == 5:
#     count += 1
# print(count)

# task28
# a, b, c, d = map(int, input().split())
# count = 0
# if a % 3 == 0:
#     count += 1
# if b % 3 == 0:
#     count += 1
# if c % 3 == 0:
#     count += 1
# if d % 3 == 0:
#     count += 1
# print(count)

# task29
# a, b, c, d = map(int, input().split())
# sum = 0
# if a % 11 != 0:
#     sum += a
# if b % 11 != 0:
#     sum += b
# if c % 11 != 0:
#     sum += c
# if d % 11 != 0:
#     sum += d
# print(sum)

# task30
# a = int(input())
# if a > 10:
#     print("yes")
# else:
#     print("no")

# task31
# a = int(input())
# if a < 5:
#     print("yes")
# else:
#     print("no")

# task32
# for i in range(3):
#     a = int(input())
#     if a % 2 == 0:
#         print("yes")
#     else:
#         print("no")

# task33
# print("lol")

# task34
# print("lol")
# print("lol")
# print("lol")

# task35
# n = int(input())
# for i in range (n):
#     print("lol")

# task36
# n = int(input())
# s = 0
# for i in range(1, n + 1):
#     s +=i
# print(s)

# task37
# n = int(input())
# s = 1
# for i in range(1, n + 1):
#     s *= i
#     print(s)

# task38
# n = int(input())
# s = 0
# for i in range(100):
#     s += n
# print(s)

# task39
# a, n = map(int, input().split())
# s = 0
# for i in range(n):
#     s += a
# print(s)

# task40
# n = int(input())
# s = 1
# for i in range(n):
#     s *= 2
# print(s)

# task41
# a, n = map(int, input().split())
# s = 1
# for i in range(n):
#     s *= a
# print(s)

# task42
# a = int(input())
# if a == 5:
#     print("onts")
# elif a == 4:
#     print("sain")
# elif a == 3:
#     print("dund")
# else: 
#     print("muu")

# task43
# a = int(input())
# if a > 89:
#     print("a")
# elif a > 79:
#     print("b")
# elif a > 69:
#     print("c")
# elif a > 59:
#     print("d")
# else:
#     print("f")

# task44
# n = int(input())
# if n== 1:
#     print("monday")
# elif n== 2:
#     print("tuesday")
# elif n== 3:
#     print("wednesday")
# elif n== 4:
#     print("thursday")
# elif n== 5:
#     print("friday")
# elif n== 6:
#     print("saturday")
# else:
#     print("sunday")

# task45
# n = int(input())
# if n in (1, 11, 12):
#     print("winter")
# elif n in (2, 3, 4):
#     print("spring")
# elif n in(5, 6, 7):
#     print("summer")
# else:
#     print("autumn")

# task46
# a, b, c = map(int, input().split())
# s = a + b + c
# print("yes")

# task47
# for i in range(1, 11):
#     print(3, "*", i, "=", 3 * i)

# task48
# n = int(input("toogoo oruul"))
# for i in range(1, 11):
#     print(n, "^", i, "=", n ** i)

# task49
# a, b, c = map(int, input().split())
# s = a * b - c
# print(s)






##################################################
# 2 HESEG

# task1
# n, m = map(int, input().split())
# k = int(input())
# dawhar = (k - 1) // m + 1
# haalga = (k - 1) % m + 1
# print(dawhar, haalga)

# task2
# n, m, k = map(int, input().split())
# o = (k - 1) // (n * m) + 1
# d = (k - 1) // m % n + 1
# h = (k - 1) % m + 1
# print(o, d, h)

# task3
# n = int(input())
# n = n * (n + 1) // 2
# print(n)

# task4
# n = int(input())
# s = 0
# for i in range(1, n + 1):
#     s += i * i
# print(s)

# task5
# n = int(input())
# s = n * n + n
# print(s // 2)

# task6
# n = int(input())
# while n >= 10:
#     n //= 10
# print(n)

# task7
# n = int(input())
# s = 0
# while n > 0:
#     s += n % 10
#     n //= 10
# print(s)

# task8
# n = int(input())
# s = 0
# while n > 0:
#     d = n % 10
# if d % 2 == 0:
#     s = s + d 
# n = n // 10
# print(s)

# task9
# n = int(input())
# s = 0
# while n > 0:
#     d = n % 10
# if d % 2 == 1:
#     s = s + 1
#     n = n // 10
# print(s)

# task10
# n, d = map(int, input().split())
# c = 0
# while n > 0:
#     if n % 10 == d:
#         c += 1
#     n //= 10
# print(c)

# task11
# n = int(input())
# m_d = 0
# while n > 0:
#     d = n % 10
#     if d > m_d:
#         m_d - d
#     n //= 10
# print(m_d)

# task12
# n = int(input())
# min_d = 9
# while n > 0:
#     d = n % 10
#     if d < min_d:
#         min_d = d
#     n //= 10
# print(min_d)

# task13
# n = int(input())
# r = 0
# while n > 0:
#     d = n % 10
#     r = r *10 + d
#     n //= 10
# print(r)

# task14
# n = int(input())
# o = n 
# r = 0
# while n > 0:
#     d = n % 10
#     r = r * 10 + d 
#     n //= 10
# if o == r:
#     print("yes")
# else:
#     print("no")

# task15
# n = int(input())
# while n % 2 == 0:
#     n //= 2
# if n == 1:
#     print("yes")
# else:
#     print("no")

# task16
# n = int(input())
# while n % 3 == 0:
#     n //= 3
# print(n)

# task17
# n = int(input())
# i = 1
# while n % i == 0:
#     n //= i 
#     i += 1
# if n == 1:
#     print(i - 1)
# else:
#     print("no")

# task18
# a, b = map (int, input().split())
# while b != 0:
#     a, b = b, a%b 
# print(a)

# task19
# a, b = map(int, input().split())
# x = a 
# y = b 
# while a != b:
#     if a < b:
#         a += x
#     else:
#         b += y 
# print(a)

# task20
# a, b = map(int, input().split())
# x = a
# y = b 
# while y != 0:
#     x, y = y, x%y 
#     print(a // x, "/", b // x, sep="")

# task21
# n = int(input())
# i = 0
# r = ""
# while i < n:
#     r += str(n)
#     i += 1
#     print(r)

# task22
# n = int(input())
# for i in range(n):
#     print(i, end="")

# task23
# n = int(input())
# for i in range(9, n - 1, -1):
#     print(i)

# task24
# n = int(input())
# for i in range(n):
#     for j in range(1, n + 1):
#        print(j, end=" ")
#        print()

# task25
# n = int(input())
# for i in range(n):
#     for j in range(n, 0, -1):
#         print(j, end=" ")
#     print()

# task26
# n = int(input())
# for i in range(n, 0, -1):
#     for j in range(n, i -1, -1):
#         print(j, end=" ")
#     print()

# task27
# k = int(input())
# a = (k + 1) * (k + 2) * (k + 3) // 6
# print(a)

# task28
# a, b, c = map(int, input().split())
# if a * a + b * b == c * c:
#     print("right")
# elif a * a + c * c == b * b:
#     print("right")
# elif b * b + c * c == a * a:
#     print("right")
# elif a * a + b * b > c * c and a * a + c * c > b * b and b * b + c * c > a * a:
#     print("acute")
# else:
#     print("obtuse")

# task29
# import math
# a, b, c = map(int, input().split())
# x = math.gcd(a, b)
# x = math.gcd(x, c)
# print(x)

# task30
# a, b = map(int, input().split())
# while a > 0 and b > 0:
#     if a > b:
#         print(b, a // b)
#         a = a % b
#     else:
#         print(a, b // a)
#         b = b % a 

# task31
# n = int(input())
# s = "1" + str(n) + "1"
# a = int(s)
# print(a * a)

# task32
# import math 
# a, b = map(float, input().split())
# c = math.sqrt(a * a + b * b)
# print(round(c, 1))

# task33
# import math 
# a, b, c = map(float, input(). split())
# p = (a + b + c)/2
# s = math.sqrt(p * (p - a) * (p - b) * (p - c))
# print(round(s, 2))

# task34
# r = float(input())
# pi = 3.141592
# s = pi * r * r 
# print(round(s, 4))

# task35
# import math 
# a, b = map(float, input().split())
# a = (a + b)/2
# g = math.sqrt(a * b)
# print(f"{a:.2f} {g:.2f}")

# task36
# n = int(input())
# s = 0
# for i in range(1, n + 1):
#     s += 1 ** 3
# print(s)

# task37
# r = float(input())
# p = 3.141592
# s = p *r * r 
# l = 2 * p * r 
# print(f"{s:.1f} {l:.1f}")

# task38
# n = int(input())
# s = 0
# for i in range(n):
#     s += int(input())
#     print(s)

# task39
# n = int(input())
# s = 0
# for i in range(n):
#     x = int(input())
#     if x > 0:
#         s += x
# print(s)

# task40
# n = int(input())
# c = 0
# for i in range(n):
#     s = int(input())
#     if s < 60:
#         c += 1
# print(c)

# task41
# n = int(input())
# a = []
# for i in range(n):
#     a.append(int(input()))
# if a[-1] > max(a[:-1]):
#     print("yes")
# else:
#     print("no")

# task42
# n = int(input())
# a = list(map(int, input().split()))
# print(max(a))

# task43
# n = int(input())
# a = list(map(int, input().split()))
# print(min(a))

# task44
# n = int(input())
# a = list(map(int, input().split()))
# x = int(input())
# c = 0
# for i in a:
#     if i == x:
#         c += 1
# print(x, c)

# task45
# n = int(input())
# a = list(map(int, input().split()))
# m = max(a)
# p = a.index(m) + 1
# print(m, p)

# task46
# n = int(input())
# a = list(map(int, input().split()))
# m = max(a)
# p = a.count(m)
# print(m, p)

a = input()
b = a.split()
ner = []
dvn = []
for i in b:
    c = i.split(":")
    ner.append(c[0])
    dvn.append(int(c[1]))
print("highest:", end=" ")
m = max(dvn)
for i in range(len(dvn)):
    if dvn[i] == m:
        print(ner[i], end=" ")
print()
d = sum(dvn) / len(dvn)
print("avarage:", round(d, 1))
print("above avarage:", end=" ")
for i in range(len(dvn)):
    if dvn[i] > d:
        print(ner[i], end=" ")
print()
print("failed:", end=" ")
for i in range(len(dvn)):
    if dvn[i] < 60:
        print(ner[i], end=" ")