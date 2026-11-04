# BODLOGO

# task1
# nas = int(input("toogoo oruul:"))
# if nas >= 18:
#     print("oroh bolomjtoi")
# else:
#     print("oroh bolomjgui")

# task2
# n = int(input("toogoo oruul:"))
# if n % 2 == 0:
#     print("tegsh")
# else:
#     print("sondgoi")

# task3
# too1 = int(input("ehnii too:"))
# too2 = int(input("daraagiin too:"))
# if too1 > too2:
#     print(too1)
# elif too2 > too1:
#     print(too2) 
# else:
#     print("tentsvv")

# task4
# odorvvd = int(input("7 too oruul:"))
# if odorvvd == 1:
#     print("davaa")
# elif odorvvd == 2:
#     print("mygmar")
# elif odorvvd == 3:
#     print("lhawga")
# elif odorvvd == 4:
#     print("pvrew")
# elif odorvvd == 5:
#     print("baasan")
# elif odorvvd == 6:
#     print("bymba(amraltiin odor)")
# elif odorvvd == 7:
#     print("nym(amraltiin odor)")
# else:
#     print("buruu too")

# task5
# km = int(input())
# hour = int(input())
# if km <= 2:
#     vne = 3000
# else:
#     vne = 3000 + (km - 2) * 1500
# if hour >= 22 or hour < 6:
#     vne = vne * 1.2
# print(int(vne))

# task6
# kbt = int(input())
# if kbt <= 150:
#     price = kbt * 100
# elif kbt <= 300:
#     price = 150 * 100 + (kbt - 150) * 150
# else:
#     price = 150 * 100 + 150 * 150 + (kbt - 300) * 200
# print(price)

# task7
username = "admin"
password = "1234"
failed_attempts = 0
while failed_attempts < 3:
    name = input("Hereglegchiin ner: ")
    pw = input("Nuuts ug: ")
if name == username and pw == password:
        print("Amjilttai nevterlee")
        break
    else:
        failed_attempts += 1
        print("Nuuts ug buruu")
if failed_attempts == 3:
    print("Tanii erh haagdsan baina")


# 2.1 – 1-ees N hurtel hevleh

```python
n = int(input("Too oruul: "))

for i in range(1, n + 1):
    print(i)
```

# 2.2 – Tegsh toonuudiin niilber

```python
n = int(input("Too oruul: "))
s = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        s += i

print("Niilber:", s)
```

# 2.3 – Urjih hvsnegt

```python
n = int(input("Too oruul: "))

for i in range(1, 11):
    print(n, "*", i, "=", n * i)
```

# 2.4 – Mungunii osolt

```python
money = float(input("Munguu oruul: "))

for i in range(1, 6):
    money = money * 1.12
    print(i, "jil:", money)
```

# 2.5 – Anhnii too esehiig shalgah

```python
n = int(input("Too oruul: "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Anhnii too")
else:
    print("Anhnii too bish")
```

# 2.6 – 3-t huvaagddag toog algasah

```python
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)
```

# 2.7 – Odtoi shat

```python
n = int(input("Too oruul: "))

for i in range(1, n + 1):
    print("*" * i)
```

# 2.8 – Too taah

```python
number = 42

while True:
    guess = int(input("Too taana uu: "))

    if guess == number:
        print("Zov taalaa")
        break
    elif guess < number:
        print("Ih too oruul")
    else:
        print("Baga too oruul")
```

# 2.9 – Tsifruudiin niilber

```python
n = int(input("Too oruul: "))

while n >= 10:
    s = 0

    while n > 0:
        s += n % 10
        n //= 10

    n = s

print("Hariу:", n)
```

# 3.1 – Jagsaaltiin niilber, dundaj

```python
a = [10, 20, 30, 40, 50]

s = sum(a)
avg = s / len(a)

print("Niilber:", s)
print("Dundaj:", avg)
```

# 3.2 – Hamgiin ih too, bairlal

```python
a = [10, 25, 5, 40, 15]

m = max(a)
print("Hamgiin ih too:", m)
print("Bairlal:", a.index(m))
```

# 3.3 – Ner haih

```python
names = ["Bat", "Saraa", "Dorj", "Naraa"]

name = input("Ner oruul: ")

if name in names:
    print("Hereglegch oldloo")
else:
    print("Hereglegch oldsongui")
```

# 3.4 – Vniig 10 huviar buuruulah

```python
prices = [1000, 2000, 3000, 4000]

for i in range(len(prices)):
    prices[i] = prices[i] * 0.9

print(prices)
```

# 3.5 – Tentssen dvngvvdiig gargah

```python
scores = [45, 80, 65, 90, 30]

for score in scores:
    if score >= 60:
        print(score)
```

# 3.6 – Borluulaltiin orlogo

```python
orders = [1000, 2000, 3000, 4000]

total = sum(orders)

print("Niit orlogo:", total)
```

# 3.7 – Oyutnii dvn

```python
students = [
    ["Bat", 80, 90],
    ["Saraa", 70, 85],
    ["Dorj", 60, 75]
]

for student in students:
    avg = (student[1] + student[2]) / 2
    print(student[0], avg)
```

# 4.1 – Neriin ehnii useg tom bolgoh

```python
name = input("Neree oruul: ")

print(name.capitalize())
print("Usegnii too:", len(name))
```

# 4.2 – Useg tooloh

```python
text = input("Ug oruul: ")
letter = input("Useg oruul: ")

print(text.count(letter))
```

# 4.3 – Email shalgah

```python
email = input("Email oruul: ")

if "@" in email and "." in email:
    print("Email zuv")
else:
    print("Email buruu")
```

# 4.4 – Muuhai vg solih

```python
text = input("Ug oruul: ")

bad_words = ["muuhai", "teneg"]

for word in bad_words:
    text = text.replace(word, "***")

print(text)
```

# 4.5 – Palindrome shalgah

```python
text = input("Ug oruul: ")

if text == text[::-1]:
    print("Palindrome mun")
else:
    print("Palindrome bish")
```

# 5.1 – Kvadrat oloh function

```python
def square(n):
    return n * n

a = int(input("Too oruul: "))

print(square(a))
```

# 5.2 – Mendchilgee function

```python
def greet(name):
    print("Sain baina uu", name)

greet("Bat")
```

# 5.3 – Nas shalgah

```python
def check_age(age):
    if age >= 18:
        print("Nasand hvrsen")
    else:
        print("Nasand hvreegui")

age = int(input("Nas oruul: "))
check_age(age)
```

# 5.4 – BMI tootsooloh

```python
def bmi(weight, height):
    return weight / (height * height)

w = float(input("Jin oruul: "))
h = float(input("Undur oruul: "))

print("BMI:", bmi(w, h))
```

# 5.5 – Tsaling tootsooloh

```python
def salary(hours, price):
    return hours * price

h = int(input("Ajillasan tsag: "))
p = int(input("Neg tsagiin tsalin: "))

print("Tsalin:", salary(h, p))
```

# 5.6 – Counter function

```python
def counter():
    count = 0

    def add():
        nonlocal count
        count += 1
        return count

    return add

a = counter()

print(a())
print(a())
print(a())
```

# 6.1 – Hereglegchiin dictionary

```python
user = {
    "name": "Bat",
    "age": 20,
    "city": "Ulaanbaatar"
}

print(user)
```

# 6.2 – Vniig hevleh

```python
products = {
    "Talh": 2000,
    "Su": 4000,
    "Undug": 500
}

for name, price in products.items():
    print(name, price)
```

# 6.3 – Hamgiin unetei baraa, niit vne

```python
products = {
    "Talh": 2000,
    "Su": 4000,
    "Undug": 500
}

print("Hamgiin unetei:", max(products, key=products.get))
print("Niit vne:", sum(products.values()))
```

# 6.4 – Sanal tooloh

```python
votes = ["Bat", "Saraa", "Bat", "Dorj", "Bat", "Saraa"]

for name in set(votes):
    print(name, votes.count(name))

print("Yalagch:", max(set(votes), key=votes.count))
```

# 6.5 – Oyutnuudiig angilalaar ni bvlgleh

```python
students = {
    "A": ["Bat", "Saraa"],
    "B": ["Dorj", "Naraa"]
}

for group, names in students.items():
    print(group, names)
```

# 6.6 – Angiin tailan

```python
students = {
    "Bat": 80,
    "Saraa": 90,
    "Dorj": 70
}

for name, score in students.items():
    print(name, score)

print("Angiin dundaj:", sum(students.values()) / len(students))
```

# 6.7 – Nom zeelvvleh

```python
books = {
    "Python": True,
    "English": True,
    "Math": False
}

name = input("Nomnii ner: ")
if name in books:
    if books[name] == True:
        books[name] = False
        print("Nom zeellee")
    else:
        print("Nom zeeltei baina")
else:
    print("Nom oldsongui")
print(books)