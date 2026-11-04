
# task1
# ner = input()
# print("sain uu,", ner + "!")

# task2
# a = int(input())
# b = int(input())
# print(a + b)

# task3
# une1 = float(input())
# une2 = float(input())
# dvn = une1 + une2
# print("niit dvn:", dvn)

# task4
# a = input()
# print(type(a))
# print(type(int(a)))

# task5
# t = input()
# print(len(t))

# task6
# t = input()
# print(t[0])
# print(t[-1])

# task7
# n = int(input())
# for i in range(1, n + 1):
#     print(i)

# task8
# a = input.split()
# too = []
# for x in a:
#     too.append(int(x))
#     print(sum(too))

# task9
# n = list(map(int, input().split()))
# print(min(n), max(n))

# task10
# n = list(map(int, input().split()))
# m = sum(n) / len(n)
# print(round(m, 2))

# task11
# n = input().split()
# m = input()
# n.append(m)
# print(n)

# task12
# n = input().split()
# b = input()
# n.insert(1, b)
# print(n)

# task13
# n = input().split()
# m = input()
# n.remove(m)
# print(n)

# task14
# n = input().split()
# m = int(input())
# f = n.pop(m)
# print(f)
# print(",".join(n))

# task15
# n = list(map(int, input().split()))
# n.sort()
# print(n)
# n.sort(reverse=True)
# print(n)

# task16
# n = list(map(int, input().split()))
# n.reverse()
# print(n)

# task17
# a = " hello "
# print("[" + a.strip() + "]")
# print("[" + a.lstrip() + "]")
# print("[" + a.rstrip() + "]")

# task18
# n = input()
# m = n.split()
# print(len(m))

# task19
# n = input().lower()
# m = input().lower()
# print(n.count(m))

# task20
# n = input()
# m = input()
# print(n.find(m))
# if m in n:
#     print(n.index(m))
# else:
#     print("oldsongui")

# task21
# n = input().split()
# m = []
# for u in n:
#     if u.startswith("report") and u.endswith(".pdf"):
#         m.append(u)
# if len(m) > 0:
#     for u in m:
#         print(u)
#     else:
#         print("oldsongui")

# task22
# n = input()
# m = input()
# f = input()
# print(n.replace(m, f))

# task23
# n = input().lower().split()
# m = input().lower()
# if m in n:
#     print("yes")
# else:
#     print("no")

# task24
# n = input()
# print(n[:3])
# print(n[-3:])

# task25
# n = input()
# m = n[::-1]
# if n.lower() == m.lower():
#     print("yes")
# else:
#     print("no")

# task26
# n = input().split()
# m = max(n, key=len)
# print(m)

# task27
# n = input().split(",")
# ner = n[0].strip()
# nas = int(n[1].strip())
# hot = n[2].strip()
# print(ner + " | ireh jil:", nas + 1, "|", hot)

# task28
# n = input().lower().split()
# m = []
# for u in n:
#     if u not in m:
#         m.append(u)
# m.sort()
# print(" ".join(m))

# task29
# n = list(map(int, input().split()))
# m = []
# for u in n:
#     if u not in m:
#         m.append(u)
# m.sort()
# print(m[-2])

# task30
n = int(input())
ner =[]
onoo = []
for u in range(n):
    m = input().split(",")
    ner.append(m[0].strip())
    onoo.append(int(m[1].strip()))
d = round(sum(onoo) / n, 2)
ih = max(onoo)
y = onoo.index(ih)
ih_ner = ner[u]
ner.sort()
print("dundaj:", d)
print("hamgiin ondor:", ih_ner, ih)
print("nersvvd:", ",".join(ner))