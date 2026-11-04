# PYTHON TUPLE BA UNPACKING 24 BODLOGO

# task1
# ongvvd = ("ulaan", "nogoon", "tsenher")
# print(ongvvd)

# task2
# amitad = ("nohoi", "muur", "tuulai", "mori")
# n, m, f, g = amitad
# print(n)
# print(m)
# print(g)

# task3
# n = (100,)
# print(type(n))

# task4
# hicheelvvd = ("matematik", "mongol hel", "angli hel", "python")
# print(hicheelvvd[0])
# print(hicheelvvd[2])
# print(hicheelvvd[3])

# task5
# toonuud = (10, 20, 30, 40, 50)
# print(toonuud[0:3])

# task6
# toonuud = (10, 20, 30, 40, 50)
# print(toonuud[-3:])

# task7
# jimsvvd = ("alim", "banana", "jvrj", "usan vzem")
# print(len(jimsvvd))

# task8
# toonuud = (45, 12, 89, 23, 7)
# print("hamgiin ih:", max(toonuud))
# print("hamgiin baga:", min(toonuud))

# task9
# onoonuud = (80, 90, 70, 100)
# print("niilber:", sum(onoonuud))
# print("dundaj:", sum(onoonuud) / len(onoonuud))

# task10
# toonuud = (50, 10, 40, 20, 30)
# print(sorted(toonuud))

# task11
# toonuud = (10, 20, 10, 30, 10, 40)
# print(toonuud.count(10))

# task12
# jimsvvd = ("alim", "banana", "jvrj", "usan vzem")
# print(jimsvvd.index("jvrj"))

# task13
# amitad = ("nohoi", "muur", "tuulai")
# n = input("amitnii ner oruulna:")
# if n in amitad:
#     print("baina")
# else:
#     print("baihgui")

# task14
# suragch = ("anu", 12, "7a")
# name, age, suragch_angi = suragch
# print("ner:", name)
# print("nas:", age)
# print("angi:", suragch_angi)

# task15
# koordinat = (15, 25)
# x, y = koordinat
# print("x =", x)
# print("y =", y)

# task16
# nomnuud = ("python surah", "bat", 250)
# title, author, pages = nomnuud
# print("nom:", title)
# print("zohiolch:", author)
# print("huudas:", pages)

# task17
# n = 5
# m = 10
# n, m = m, n 
# print("n =", n)
# print("m =", m)

# task18
# toonuud = (10, 20, 30, 40, 50)
# first, *others = toonuud
# print("ehnii utga:", first)
# print("vldsen utga:", others)

# task19
# toonuud = (1, 2, 3, 4, 5, 6)
# first, *middle, last = toonuud
# print("ehnii utga:", first)
# print("dundah utga:", middle)
# print("svvliin utga:", last)

# task20
# suragch = ("temvvlen", "matematik", "python", "angli hel")
# name, *subjects = suragch
# print("suragch:", name)
# print("hicheelvvd:", subjects)

# task21
# bvteegdehvvn= ("dewter",3500, 4)
# name, price, quantity = bvteegdehvvn
# niit_dvn = price * quantity
# print("bvteegdehvvn:", name)
# print("negj vne:", price)
# print("shirheg:", quantity)
# print("niit vne:", niit_dvn)

# task22
# suragch = (
#     ("Ану", 90),
#     ("Бат", 75),
#     ("Сараа", 100)
# )
# for ner, onoo in suragch:
#     print(ner, ":", onoo)

# task23
# suragch = (
#     ("Ану", 90),
#     ("Бат", 75),
#     ("Сараа", 100)
# )
# for ner, onoo in suragch:
#     if onoo >= 80:
#         print(ner)

# task24
ongvvd = ("улаан", "ногоон", "цэнхэр")
n = list(ongvvd)
n.append("shar")
ongvvd = tuple(n)
print(ongvvd)