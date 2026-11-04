# BODLOGO

# task2
# class Student:
#     def __init__(self, ner, nas):
#         self.ner = ner
#         self.nas = nas
# suragch1 = Student("Нараа", 17)
# suragch2 = Student("Тэмүүлэн", 19)
# print(suragch1.ner)
# print(suragch1.nas)
# print(suragch2.ner)
# print(suragch2.nas)

# task3
# class Student:
#     def __init__(self, ner, nas, angi):
#         self.ner = ner
#         self.nas = nas
#         self.angi = angi
# suragch1 = Student("Бат", 18, "12А")
# print("Нэр:", suragch1.ner)
# print("Нас:", suragch1.nas)
# print("Анги:", suragch1.angi)

# task4
# class Student:
#     def __init__(self, ner, onoo):
#         self.ner = ner
#         self.onoo = onoo
# suragch1 = Student("Бат", 85)
# suragch2 = Student("Сараа", 95)
# print(suragch1.ner)
# print(suragch1.onoo)
# print(suragch2.ner)
# print(suragch2.onoo)

# task5
# class Student:
#     def __init__(self, ner, onoo):
#         self.ner = ner
#         self.onoo = onoo
#     def add_score(self):
#         self.onoo += 5
# suragch1 = Student("Бат", 80)
# suragch1.add_score()
# print(suragch1.onoo)

# task6
# class Student:
#     def __init__(self, ner, nas, angi):
#         self.ner = ner
#         self.nas = nas
#         self.angi = angi
#     def show_info(self):
#         print("Нэр:", self.ner)
#         print("Нас:", self.nas)
#         print("Анги:", self.angi)
# suragch1 = Student("Сараа", 19, "12Б")
# suragch1.show_info()

# task7
# class Student:
#     def __init__(self, ner, onoo):
#         self.ner = ner
#         self.onoo = onoo
#     def check_result(self):
#         if self.onoo >= 60:
#             print(self.ner + ": Тэнцсэн")
#         else:
#             print(self.ner + ": Тэнцээгүй")
# suragch1 = Student("Бат", 75)
# suragch2 = Student("Нараа", 45)
# suragch1.check_result()
# suragch2.check_result()

# task8
# class Student:
#     def __init__(self, ner, onoo):
#         self.ner = ner
#         self.onoo = onoo
#     def add_score(self):
#         self.onoo += 5
# suragch1 = Student("Бат", 80)
# suragch1.add_score()
# print(suragch1.onoo)

# task9
# class Student:
#     def __init__(self, ner, nas):
#         self.ner = ner
#         self.nas = nas
#     def birthday(self):
#         self.nas += 1
# suragch1 = Student("Сараа", 18)
# suragch1.birthday()
# suragch1.birthday()
# print(suragch1.nas)

# task10
# class Student:
#     def __init__(self, ner, onoo):
#         self.ner = ner
#         self.onoo = onoo
#     def get_grade(self):
#         if self.onoo >= 90:
#             print("A")
#         elif self.onoo >= 80:
#             print("B")
#         elif self.onoo >= 70:
#             print("C")
#         elif self.onoo >= 60:
#             print("D")
#         else:
#             print("F")
# suragch1 = Student("Бат", 95)
# suragch1.get_grade()

# task11
# class Student:
#     def __init__(self, ner):
#         self.ner = ner
#         self.irts = 0
#     def attend(self):
#         self.irts += 1
#     def show_attendance(self):
#         print(self.irts)
# suragch1 = Student("Бат")
# suragch1.attend()
# suragch1.attend()
# suragch1.attend()
# suragch1.show_attendance()

# task12
# class Student:
#     def __init__(self, ner, onoo, irts):
#         self.ner = ner
#         self.onoo = onoo
#         self.irts = irts
#     def check_result(self):
#         if self.onoo >= 60 and self.irts >= 80:
#             print("Хичээлд тэнцсэн")
#         else:
#             print("Хичээлд тэнцээгүй")
# suragch1 = Student("Бат", 75, 90)
# suragch2 = Student("Нараа", 50, 85)
# suragch1.check_result()
# suragch2.check_result()

# task13
# class Student:
#     def __init__(self, ner, onoonyyd):
#         self.ner = ner
#         self.onoonyyd = onoonyyd
#     def show_scores(self):
#         print(self.onoonyyd)
#     def add_score(self, onoo):
#         self.onoonyyd.append(onoo)
#     def average(self):
#         print(sum(self.onoonyyd) / len(self.onoonyyd))
# suragch1 = Student("Бат", [80, 90, 70])
# suragch1.show_scores()
# suragch1.add_score(100)
# suragch1.show_scores()
# suragch1.average()

# task14
# class Student:
#     def __init__(self, ner, nas, angi):
#         self.ner = ner
#         self.nas = nas
#         self.angi = angi
#     def show_info(self):
#         print("Нэр:", self.ner)
#         print("Нас:", self.nas)
#         print("Анги:", self.angi)
#     def change_name(self, shine_ner):
#         self.ner = shine_ner
#     def change_grade(self, shine_angi):
#         self.angi = shine_angi
# suragch1 = Student("Бат", 18, "12А")
# suragch1.change_name("Сараа")
# suragch1.change_grade("12Б")
# suragch1.show_info()

# task15
# class Student:
#     def __init__(self, ner, angi, onoo):
#         self.ner = ner
#         self.angi = angi
#         self.onoonyyd = [onoo]
#     def show_info(self):
#         print("Нэр:", self.ner)
#         print("Анги:", self.angi)
#         print("Оноо:", self.onoonyyd)
#     def add_score(self, onoo):
#         self.onoonyyd.append(onoo)
#     def check_result(self):
#         if sum(self.onoonyyd) / len(self.onoonyyd) >= 60:
#             print("Тэнцсэн")
#         else:
#             print("Тэнцээгүй")
#     def average(self):
#         print(sum(self.onoonyyd) / len(self.onoonyyd))
# suragch1 = Student("Бат", "12А", 80)
# suragch1.show_info()
# suragch1.add_score(90)
# suragch1.check_result()
# suragch1.average()
