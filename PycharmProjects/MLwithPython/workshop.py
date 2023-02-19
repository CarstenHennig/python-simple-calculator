# print("Hello World")
# # this is a comment
# print(20*5)
# age = 20
# print("Age is:", age)
# my_text_var = "Hello"
# print(my_text_var)
# print(type(my_text_var), type(age))

# age = 20
# share = 7.3
# print(type(share))
#
# n1 = 70
# n2 = 3
# print(n2 % 2)
# print(n1 // n2)
# print(n1 / n2 / n1)
# print(n1 % n2)
# print(n1 ** n2)

# greeting = "Hello"
# name = 'Devrim'
# print(greeting, name, "!")
# print(name * 3)
#
# my_integer = 20
# my_float = 7.3
# my_string = "Hello"

# name = input("Can you tell me your name? ")
# year_of_birth = int(input("What's your year of birth? "))
# age = 2022 - year_of_birth
# print(f"Hi {name}, your are {age} years old")

# n1, n2, n3 = 10, 6, 5
# print(n1, n2, n3)

# import random
#
# rand_number = random.randint(1, 10)
# print(rand_number)


# temperature = int(input("What is the temperature? "))
#
# unit_of_temperature = input("Is this in Fahrenheit (type F) or in Celsius (type C)? ")
#
# if unit_of_temperature == "C":
#     print(f"Temperate is {temperature} degree Celsius")
# elif unit_of_temperature == "F":
#     temp_f = temperature * 1.8
#     print(f"Temperatur is {temperature} degree Fahrenheit or {temp_f} degree Celsius")
# else:
#     print("No valid input")

# for i in [1, 2, 3, 4, 5]:
#     print(i)
#     for j in [1, 2, 3, 4, 5]:
#         print(j)
#         print(i + j)
#     print(i)
# print("done looping")

# interests = [
#     (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
#     (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
#     (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
#     (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
#     (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
#     (3, "statistics"), (3, "regression"), (3, "probability"),
#     (4, "machine learning"), (4, "regression"), (4, "decision trees"),
#     (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
#     (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
#     (6, "probability"), (6, "mathematics"), (6, "theory"),
#     (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
#     (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
#     (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
#     (9, "Java"), (9, "MapReduce"), (9, "Big Data")
# ]
#
# words_and_counts = Counter(word
#                            for user, interest in interests
#                            for word in interest.lower().split())
# for word, count in words_and_counts.most_common():
#     if count > 1:
#         print(word, count)


# long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 +
#                            13 + 14 + 15 + 16 + 17 + 18 + 19 + 20)
#
# list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# easier_to_read_list_of_lists = [[1, 2, 3],
#                                 [4, 5, 6],
#                                 [7, 8, 9]]
#
# for i in [1,2,3,4,5]:
#
#     print(i)

# import re
# my_regex = re.compile("[0-9]+", re.I)
#
# try:
#     print(0/0)
# except ZeroDivisionError:
#     print("cannot divide by zero")
#
# def my_print(message = "my default message"):
#     print(message)
# my_print("hello")   # prints 'hello'
# my_print()
#
# first_name = "Joel"
# last_name = "Grus"
# full_name3 = f"{first_name} {last_name}"
# print(full_name3)

# x = 10
# print("The answer is {x} today".format(x = x))
# print(f'The answer is {x: 08d} today')
#
# raise ValueError(f"Expected {x!r} to a float not a {type(x).__name__}")


from collections import Counter
from random import choices

# d = {}
# d['dragons']
# d = Counter()
# d['dragons'] += 1
# print(d)
#
# c = Counter('red green red blue red blue green'.split())
# print(c)
# print(c.most_common(1))
# print(c.most_common(2))
# print(list(c.elements()))
# print(list(c.values()))
# print(list(c.items()))


# from statistics import mean, median, mode, stdev, pstdev
# print(mean([50, 52, 53]))
# print(median([50, 52, 53]))
# print(mode([51, 50, 52, 53]))
# print(stdev([50, 52, 53]))
# print(pstdev([50, 52, 53]))
#
# u = [10, 20, 30]
# t = [40, 50, 60]
# z = u + t
# print(z)
# print(z[:2] + z[-2:])
# print(dir(list))


# s = 'abacadabra'
# c = s.index('c')
# print(c)
# print(s.count('a'))
#
#
# s = [5, 72, 300, -1, 2]
# s.sort()
# print(s)
# print(sorted("cat"))
#
# lambda a, b: a+b
# print((lambda x: x**2)(5))
#
# print(100 + (lambda x: x**2)(5) + 50)
#
# f = lambda x, y: 3*x +y
# print(f(3, 8))


# print((lambda x, y: x**y)(10, 20))
#
# x = 15
# print(x > 6 and x < 20)
# print(6 < x < 20)
#

from random import *
from statistics import *
from collections import *

#
# print(choice(['red', 'red', 'red', 'black', 'black', 'green']))
# print(['red'] * 18)
# print(choice(['red'] * 18 + ['black'] * 18 + ['green'] * 2))
# population = ['red'] * 18 + ['black'] * 18 + ['green'] * 2
# print(choice(population))
# print([choice(population) for i in range(6)])
# print(Counter([choice(population) for i in range(6)]))
# print(choices(population, k=6))
# print(Counter(choices(population, k=8)))
# print(choices(['red', 'black', 'green'], [18, 18, 2], k=4))
#
# deck = Counter(tens=16, low=36)
# deck = list(deck.elements())
# deal = sample(deck, 10)
# print(deal)
# print(Counter(deal))
# deal = sample(deck, 52)
# remainder = deal[20:]
# print(Counter(remainder))

# pop = ["heads", "tails"]
# wgt = [6, 4]
# cum_weights = [0.60, 1.00]
# trial = lambda: choices(["heads", "tails"], cum_weights=[0.60, 1.00], k=7).count("heads") >= 5
# print(trial())
# n = 100000
# print(sum(trial() for i in range(n)) / n)

# from math import factorial as fact
# print(fact(4))
# print(fact(5))
#
# def comb(n, r):
#         return fact(n) // fact(r) // fact(n - r)
# print(comb(10, 3))
# print(comb(10, 2))
#
# ph = 0.60
# print(ph ** 6 * (1 - ph) ** 1 * comb(7, 6))
#
# print(sorted(sample(range(100000), 5))[2])

# n = 100000
# trial = lambda : n // 4 < median(sample(range(100000), 5)) <=  3* n // 4
# print(sum(trial() for i in range(n)) / n)


# students = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2], ["Akriti", 41], ["Harsh", 39],]
# grades = []
# students_with_second_lowest_grade = []
#
# for i in range(len(students)):
#     # print(f"These are our students and their grades: {students[i][0]} - {students[i][1]}")
#     grades.append(students[i][1])
#
# sorted_grades = sorted(grades)
#
# second_lowest = sorted_grades[1]
#
# for i in range(len(students)):
#     if second_lowest in students[i]:
#         students_with_second_lowest_grade.append(students[i][0])
#
# sorted_students_with_second_lowest_grade = sorted(students_with_second_lowest_grade)
#
# for i in range(len(sorted_students_with_second_lowest_grade)):
#     print(sorted_students_with_second_lowest_grade[i])


A = ['a', 'b', 'a']
B = ['a', 'c']
for i in A:   if i in B:
        print(A.index(i) + 1)
    else:
        print("-1")