import random


#
# # list1 = [1, 2]
# # list2 = [0]
# # print(list1 > list2)
#
#
# class Punt:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __add__(self, other):
#         x = self.__x + other.__x
#         y = self.__y + other.__y
#         return Punt(x, y)
#
#     def __str__(self):
#         return f"({self.__x})({self.__y})"
#
#
# punt1 = Punt(2, 3)
# punt2 = Punt(1, 0)
# punt3 = punt1 + punt2
#
#
# # print(punt3)
#
#
# class Student:
#     def __init__(self, naam, leeftijd, richting):
#         self.__naam = naam
#         self.__leeftijd = leeftijd
#         self.__richting = richting
#
#     def __lt__(self, other):
#         if self.__leeftijd < other.__leeftijd:
#             return True
#         else:
#             return False
#
#
# student1 = Student("Fransisco", 16, "MT")
# student2 = Student("Gabriel", 17, "ICW")
#
#
# class Fraction:
#     def __init__(self, teller, noemer):
#         self.__teller = teller
#         self.__noemer = noemer
#
#     def __add__(self, other):
#         teller = self.__teller + other.__teller
#         if self.__noemer == other.__noemer:
#             noemer = self.__noemer
#         else:
#             noemer = self.__noemer + other.__noemer
#         return Fraction(teller, noemer)
#
#     def __sub__(self, other):
#         teller = self.__teller - other.__teller
#         if self.__noemer == other.__noemer:
#             noemer = self.__noemer
#         else:
#             noemer = self.__noemer - other.__noemer
#
#         return Fraction(teller, noemer)
#
#     def __mul__(self, other):
#         teller = self.__teller * other.__teller
#         if self.__noemer == other.__noemer:
#             noemer = self.__noemer
#         else:
#             noemer = self.__noemer * other.__noemer
#         return Fraction(teller, noemer)
#
#     def __truediv__(self, other):
#         teller = self.__teller * other.__noemer
#         noemer = self.__noemer * other.__temmer
#         return Fraction(teller, noemer)
#
#     def __str__(self):
#         return f"{self.__teller}/{self.__noemer}"
#
#
# lijstje = [4, 2, 0]
# iterator = iter(lijstje)
# # next iterator geeft ons de eerstvolgende element in de lijst
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))
# lijst = [4, 2, 5, 8, 9, 5, 4, 8, 9, 5, 7, 5, 4, 2, 6, 8]
# for i in range(len(lijst)):
#     pass
#
#
# # simple for loop
# def funkyforloop(iterable, todo):
#     for element in range(len(iterable)):
#         todo(element)
#
#
# # uses an iterator in a while loop
# def funkyforloop2(iterable, todo):
#     # maak een iterator van een iterable.
#     iterator = iter(iterable)
#     done_looping = False
#     while not done_looping:
#         try:
#             element = next(iterator)
#         #     StopIteration is een error die gethrowt wordt aan het einde van je lijst
#         except StopIteration:
#             done_looping = True
#         #     als je geen error hebt dan wordt de actie gedaan op je element
#         # except:
#         #     todo(element)
#
#
# # funkyforloop(lijst, print)
# # funkyforloop2(lijst, print)
#
# infiniteiterator = count(1)
# for i in range(5):
#     print(next(infiniteiterator))
#
#
# # deze class gaat een oneindige iterator met daarin een tweede macht
# # van elk element lange iterator
# class Squared:
#     # numbers is in dit geval dus (hopelijk) een iterator
#     def __init__(self, numbers):
#         self.__numbers = numbers
#
#     # om een tweede macht te kunne gebruiken als een iterator, heeft die klasse een methode 'next' nodig
#     def __next__(self):
#         return next(self.__numbers) ** 2
#
#     # zodat we van een tweedemacht en iterator kunnen maken (al is het eigenlijk dat al)
#     # technisch gezien moeten we iterators ook in iterators veranderd worden
#     def __iter__(self):
#         return self
#
#
# klasse = Squared(infiniteiterator)
# newIterator = iter(klasse)
# # print(next(klasse))
# # print(next(klasse))
# # print(next(klasse))
# # print(next(klasse))
# # print(next(klasse))
# #
# # numbers is weeral een infinite iterator
# # reset numbers
# numbers = count(1)
#
#
# def square(numbers):
#     for i in numbers:
#         yield i ** 2
#
#
# # elke functie die 'yield' gebruikt is een GENERATOR functie. nieuwe soort functie
# # een generator is een functie die functioneert als iterator
# newIterator = square(numbers)
# print(next(newIterator))
# print(next(newIterator))
# print(next(newIterator))
# print(next(newIterator))
#
#
# def square3(numbers):
#     return (n ** 2 for n in numbers)
#
#
# newlist = [n for n in range(20)]
# print(newlist)
# # reset numbers
# numbers = count(1)
# # gebruik generator 'tweedemacht'
# newnumbers = square3(numbers)
# # print(next(newnumbers))
# # print(next(newnumbers))
# # print(next(newnumbers))
# readings = [100, 66, 59, 55, 54, 54, 52, 51, 50, 50, 50, 50]
#
#
# # for i in readings:
# #     if len(readings) < i + 1:
# #         for j in range(readings[i + 1]):
# #             print(i - j)
# #     else:
# #         j = readings[i - 1]
# #         print(i - j)
# # newlist = []
# # current = readings[0]
# # for next_item in readings[1:]:
# #     newlist.append(next_item - current)
# #     next_item = current
# # print(newlist)
#
# def returntwoitems(iterable):
#     iterator = iter(iterable)
#     current = next(iterator)
#     for nextitem in iterator:
#         # deze yield gaat een tuple teruggeven. Je mag er ronde haakjes rond zetten maar dat hoeft niet
#         # een komma tussen twee objecten gaat altijd geinterpreteerd worden als een tuple
#         yield current, nextitem
#         current = nextitem
#
#
# differences = []
# for first, second in returntwoitems(readings):
#     differences.append(first - second)
#
#
# # print(differences)
#
#
# def squares(list):
#     return (n ** 2 for n in list)
#
#
# if 9 in squares(lijst):
#     pass
#     # print("jop")
# # print(list(squares(lijst)))
# standarsset = {1, 2, 3, 4, 5}
# # als we niet zeker weten hoe lang een dataset is, en we willen die opslaan
# # gebruik * voor je variabele
# # enkel gebruiken wanneer je een dataset opslaat in MEERDERE variabelen
# a, b, *c = standarsset
# # print(a)
# # print(b)
# # print(*c)
# # * voor een variabele print elk element apart
# randomstring = ["Dit is een zin ", "dit ook ", "dit daaarentegen niet"]
#
#
# # print(*randomstring)


def infinite_random_number():
    while True:
        yield random.randint(1, 100), random.choice(True, False)


newnewlist = infinite_random_number()
print(newnewlist)

# for i in range(len(newnewlist)):
#     for j in range(len(newnewlist[i])):
#         if newnewlist[i][j] is True:
#             print(f'here is a true printed')

belgium = []
for i in range(10000000):
    belgium.append((i, True))

vlaanderen = []
for j in range(len(belgium)):
    if belgium[j][1]:
        vlaanderen.append(belgium[j][0])


def only_true_numbers(infinite_number):
    return (number for number in infinite_number if number[1])
