
# SHINE HICHEEEL

# def avg():
#     nums = list(map(int, input().split()))
#     return sum(nums)/len(nums)
# a = avg()
# print(a)


# def love(name="hvn bish"):
#     print("i love you", name)
# love("nomu")

# def love(*name):
#     print(name)
# love(1,2,3,4,5)

# def love(**name):
#     return name
# a = love(name = "amina", age= 23)
# print(a)


#  task1
# def gurwaljin():
#     a = list(map(int, input().split()))
#     return sum(a)
# b = gurwaljin()
# print(b)

# task2
# def niilber():
#     a = list(map(int, input().split()))
#     return sum(a)
# b = niilber()
# print(b)

# task3
# def kub():
#     a = int(input())
#     v = a ** 3
#     s = 6 * a ** 2
#     return v, s
# b = kub()
# print(b)

####################################################################33333

# task1
# def hello():
#     print(" hello python!")
# hello()

# # task2
# def greet(name = "bat!"):
#     print("sain baina uu?", name)
# greet()

# task3
# def introduce(name = "bat", age = 18):
#     print(name, "ni", age, "nastai.")
# introduce()

# task4
# def add(a, b):
#     print(a + b)
# add(10, 20)

# task5
# def square(num):
#     return num * num
# result = square(5)
# print(result)

# task6
# def max_num(a, b):
#     if a > b:
#         return a 
#     else:
#         return b 
# a, b = list(map(int, input().split()))
# print(max_num(a, b))

# task7
# def check_even(num):
#     if num % 2 == 0:
#         return "even"
#     else:
#         return "odd"
# c = int(input())
# print(check_even(c))

# task8
# def check_age(age):
#     if age >= 18:
#         return "adult"
#     else:
#         return "minor"
# age = int(input())
# print(check_age(age))

# task9
# def get_grade(score):
#     if score >= 90:
#         return "a"
#     elif score >= 80:
#         return "b"
#     elif score >= 70:
#         return "c"
#     elif score >= 60:
#         return "d"
#     else:
#         return "f"
# score = int(input())
# print(get_grade(score))

# task10
# def print_numbers(n):
#     for i in range(1, n + 1):
#         print(i, end=" ")
# a = int(input())
# print_numbers(a)

# task11
# def sum_numbers(n):
#     s = 0
#     for i in range(1, n + 1):
#         s = s + i
#     return s    
# b = int(input())
# print(sum_numbers(b))

# task12
# def count_even(n):
#     a = 0 
#     for i in range(1, n + 1):
#         if i % 2 == 0:
#             a = a + 1
#     return a 
# b = int(input())
# print(count_even(b))

# task13
# def count_digits(num):
#     a = 0 
#     while num > 0:
#         num = num // 10
#         a = a + 1
#     return a 
# b = int(input())
# print(count_digits(b))

# task14
# def find_max(nums):
#     max_num = nums[0]
#     for i in nums:
#         if i > max_num:
#             max_num = i
#     return max_num 
# nums = [4, 8, 2, 15, 6]
# print(find_max(nums))

# task15
# def find_max(nums):
#     min_num = nums[0]
#     for i in nums:
#         if i < min_num:
#             min_num = i 
#     return min_num 
# nums = [7, 3, 9, 1, 5]
# print(find_max(nums))

# task16
# def count_even(nums):
#     count = 0
#     for num in nums:
#         if num % 2 == 0:
#             count += 1
#     return count
# nums = [1, 2, 4, 7, 8, 10]
# print(count_even(nums))

# task17
# def list_sum(nums):
#     a = 0
#     for n in nums:
#         a += n
#     return a 
# nums = [10, 20, 30, 40]
# print(list_sum(nums))

# task18
# def get_age(students, name):
#     return students[name]
# students = {"bat": 18,
#             "sara": 19,
#             "bold": 20
#             }
# print(get_age(students, "sara"))

# task19
# def find_students(students, name):
#     if n in students:
#         return "found"
#     else:
#         return "not found"
# students = {}
# a = int(input("heden ner ogoh we?"))
# for i in range(n):
#     ners = input("ner:")
#     age = input("nas:")
#     students[ners] = age
# ner = input("oloh ner:")
# print(find_students(students, ners))

# task20
# def average_score(students):
#     return sum(students.values())/len(students.values())
# students = {}
# n = int(input("heden ner ogoh we?:"))
# for i in range(n):
#     ner = input("neree oruul:")
#     score = int(input("onoogoo oruul:"))
#     students[ner] = scores 
# print(average_score(students))

# task21
# def unique_count(nums):
#     a = set(nums)
#     return len(a)
# a = list(map(int, input("too:").split()))
# print(unique_count(a))

# task22
# def unique_numbers(nums):
#     return set(nums)
# a = list(map(int, input("too:").split()))
# print(unique_numbers(a))

# task23
# def greet(name="guest"):
#     print("hello", name)
# greet("bat")

# task24
# def power(num, exponent=2):
#     return num**exponent
# print(power(5))
# print(power(2, 3))

# task25
# def discount(price, percent=10):
#     discount = price * percent/ 100 
#     a = price - discount 
#     return a
# print(discount(10000))
# print(discount(10000, 20))

# task26
# def sum_all(*args):
#     s = 0 
#     for i in args:
#         s += i 
#     return s  
# print(sum_all(1, 2, 3,))
# print(sum_all(10, 20, 30, 40))

# task27
# def find_max(*args):
#     hamgiin_ih = args[0]
#     for i in args:
#         if i > hamgiin_ih:
#             hamgiin_ih = i 
#     return hamgiin_ih 
# args=list(map(int, input().split()))
# print(find_max(*args))

# task28
# def count_even(*args):
#     too = 0 
#     for i in args:
#         if i % 2 == 0:
#             too += 1 
#     return too 
# args=list(map(int, input().split()))
# print(count_even(*args))

# task29
# def show_into(**kwargs):
#     for key, value in kwargs.items():
#         print(key, ":", value)
# show_into(name="bat", age=18, city="ulaanbaatar")

# task30
# def calculate_total(**prices):
#     too = 0 
#     for key, value in prices.items():
#         too += value 
#     return too 
# apple = int(input("alim:")) 
# banana = int(input("gadil:"))
# orange = int(input("jvrj"))
# print(calculate_total(
#     apple=apple,
#     banana=banana,
#     orange=orange
# ))

# task31
# def analyze_numbers(nums):
#     n = 0
#     tegsh = 0
#     sondgoi = 0
#     for i in nums:
#         n += 1
#         if i % 2 == 0:
#             tegsh += 1
#         else:
#             sondgoi += 1
#     return {
#         "max": max(nums),
#         "min": min(nums),
#         "sum": sum(nums),
#         "even": tegsh,
#         "odd": sondgoi
#     }
# nums = [3, 8, 2, 7, 10]
# print(analyze_numbers(nums))

# task32
# def suragch_avarage(suragchid, ner):
#     n = 0
#     for i in suragchid[ner]:
#         n += i 
#     return n / len(suragchid[ner])
# suragchid = {
#     "Bat": [80, 90, 70],
#     "Sara": [100, 90, 95],
#     "Bold": [60, 70, 80]
# }
# print(suragch_avarage(suragchid, "Bat"))

# task33
# def best_suragch(students):
#     best = ""
#     max_a = 0
#     for ner in students:
#         a = sum(students[ner]) / len(students[ner])
#         if a > max_a:
#             max_a = a 
#             best = ner 
#     return best 
# students = {
#     "Bat": [80, 90, 70],
#     "Sara": [100, 90, 95],
#     "Bold": [60, 70, 80]
# }
# print(best_suragch(students))

# task34
def calculate(*args, **kwargs):
    n = 0
    for i in args:
        n += i
    n = n + kwargs["bonus"] - kwargs["tax"]
    return n 
print(calculate(10, 20, 30, bonus = 100, tax = 20))