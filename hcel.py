# PYTHON NESTED LIST 30 BODLOGO

# task1
# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# print(nums[1][2])

# task2
# students = [
#     ["Bat", 18],
#     ["Sara", 19],
#     ["Bold", 20]
# ]
# print(students[2][0])

# task3
# nums = [
#     [10, 20],
#     [30, 40],
#     [50, 60]
# ]
# print(nums[1])

# task4
# nums = [
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]
# print(nums[2][0])

# task5
# nums = [
#     [5, 10],
#     [15, 20]
# ]
# print(nums[0][0])

# task6
# nums = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
# print(nums[2][1])

# task7
# nums = [
#     [1, 2],
#     [3, 4],
#     [5, 6]
# ]
# for u in nums:
#     print(u)

# task8
# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# for u in nums:
#     for k in u:
#         print(k)

# task9
# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# for u in nums:
#     for k in u:
#         print(k, end=" ")

# task10
# nums = [
#     [3, 12, 5],
#     [20, 7, 15]
# ]
# for u in nums:
#     for k in u:
#         if k > 10:
#             print(k, end=" ")

# task11
# nums = [
#     [1, 2],
#     [3, 4, 5],
#     [6]
# ]
# n = 0
# for u in nums:
#     for k in u:
#         n += 1
# print(n)

# task12
# nums = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# n = 0
# for u in nums:
#     for k in u:
#         n += k
# print(n)

# task13
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for u in nums:
#     for k in u:
#         if k % 2 == 0:
#             print(k, end=" ")

# task14
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# n = 0
# for u in nums:
#     for k in u:
#         if k % 2 != 0:
#             n += 1
# print(n)

# task15
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8]
# ]
# n = 0
# for u in nums:
#     for k in u:
#         if k % 2 == 0:
#             n += k
# print(n)

# task16
# nums = [
#     [-3, 5, 0],
#     [7, -2, 8],
#     [-1, 4, 0]
# ]
# n = 0
# for u in nums:
#     for k in u:
#         if k > 0:
#             n += 1
# print(n)

# task17
# nums = [
#     [-2, 3, -5],
#     [4, -1, 6]
# ]
# m = 0
# for u in nums:
#     for k in u:
#         if k < 0:
#             m += k
# print(m)

# task18
# nums = [
#     [4, 8, 2],
#     [10, 3, 7],
#     [1, 6, 5]
# ]
# n = nums[0][0]
# for u in nums:
#     for k in u:
#         if k > n:
#             n = k 
# print(n)

# task19
# nums = [
#     [7, 2, 9],
#     [4, -3, 6],
#     [8, 1, 5]
# ]
# n = [0][0]
# for u in nums:
#     for k in u:
#         if k < n:
#             n = k 
# print(n)

# task20
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for u in nums:
#     n = 0
#     for k in u:
#         n += k
#     print(n)

# task21
# nums = [
#     [3, 8, 2],
#     [5, 1, 9],
#     [4, 7, 6]
# ]
# for u in nums:
#     n = u[0]
#     for k in u:
#         if k > n:
#             n = k
#     print(n)

# task22
# nums = [
#     [3, 8, 2],
#     [5, 1, 9],
#     [4, 7, 6]
# ]
# for u in nums:
#     n = u[0]
#     for k in u:
#         if k < n:
#             n = k 
#     print(n)

# task23
# nums = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# f = False
# for u in nums:
#     for k in u:
#         if k == 7:
#             f == True 
# if f:
#     print("yes")
# else:
#     print("no")

# task24
# nums = [
#     [1, 2, 3],
#     [2, 4, 2],
#     [5, 2, 6]
# ]

# target = 2
# c = 0
# for u in nums:
#     for k in u:
#         if k == target:
#             c += 1
# print(c)

# task25
# nums = [
#     [1, 7, 3],
#     [9, 2, 6],
#     [4, 8, 5]
# ]
# n = 0
# for u in nums:
#     for k in u:
#         if k > 5:
#             n += k
# print(n)

# task26
# nums = [
#     [1, 2, 3],
#     [10, 20, 30],
#     [4, 5, 6]
# ]
# max_row = nums[0]
# for row in nums:
#     if sum(row) > sum(max_row):
#         max_row = row
# print(max_row)

# task27
# students = [
#     ["Bat", 18],
#     ["Sara", 19],
#     ["Bold", 20]
# ]
# for suragch in students:
#     print(suragch[0], suragch[1])

# task28
# students = [
#     ["Bat", 17],
#     ["Sara", 19],
#     ["Bold", 20],
#     ["Anu", 16]
# ]
# for suragch in students:
#     if suragch[1] > 18:
#         print(suragch[0])

# task29
# students = [
#     ["Bat", 80, 90, 70],
#     ["Sara", 100, 90, 95],
#     ["Bold", 60, 70, 80]
# ]
# for suragch in students:
#     avg = (suragch[1] + suragch[2] + suragch[3])
#     print(suragch[0], avg)

# task30
students = [
    ["Bat", 80, 90, 70],
    ["Sara", 100, 90, 95],
    ["Bold", 60, 70, 80],
    ["Anu", 90, 90, 90]
]
max_a = 0
ner = 0
for suragch in students:
    a = (suragch[1] + suragch[2] + suragch[3]) / 3
    if a > max_a:
        max_a = a
        ner = suragch[0]
print(ner, max_a)