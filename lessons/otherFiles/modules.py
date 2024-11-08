# import GuessNumberGame
# modules importeren
from random import randint as ri

ri(2, 5)

# for element in dir(GuessNumberGame):
print(ri)

currentlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# import weird stuff
import ToDoList as projectje

print(dir(projectje))
print(currentlist)
currentlist = currentlist[1:-1]

print(currentlist)
print(currentlist.pop(6))
print(currentlist.index(5))
print(currentlist.count("dit staat achteraan"))

# weird ass for loop
poweroftwo = []
for n in range(1, 10):
    poweroftwo.append(n ** 2)

print(poweroftwo)

poweroftwo2 = [n ** 2 for n in range(1, 10)]

print(poweroftwo2)

# use tuples
standaardTuple = (1, 2, 3)
print(standaardTuple)
standaardTuple2 = 1, 2, 3, "vier", True
print(standaardTuple2)
standaardTuple3 = "vier"
print(standaardTuple3)

# to upper
originalString = "Ik ging gisteren naar de pizeria Milano"
print(originalString.upper())
print(originalString)
print(originalString.partition("naar"))
print(originalString.replace("Milano", "RealOGPizza"))
print(originalString.find("gisterenavond"))
# nuttig verdeelt de string in stukjes: scheiding op basis van ingegeven substring
print(originalString.split(" "))
numericString = "12345"
print(numericString.isnumeric())
ei = "String \"ei\""
print(ei)
# f string enable us to inject code into our string efficiently
print(f"Dit is een f string met een ei zoals dit: {ei}")

myfirstset = {"kat", "hond", "mens"}
mysecondset = {"kat", "leeuw", "panter"}

print(mysecondset)
myfirstset.add("walvis")
myfirstset.update(mysecondset)
print(myfirstset)
myfirstset.discard("walvis")
print(myfirstset)
myfirstset.add(True)
# max(), min() en sorted() returns an array
'''
if myfirstset.all():
    print("There is a true in our set")
else:
    print("Er is geen true in deze dataset")
'''

# combine the 2 sets
mysecondset.add("walvis")
unionset = myfirstset | mysecondset
print(unionset)

# haal alle elementen van de tweede set uit de eerste en bewaar ze in een nieuwe set
divisionset = myfirstset - mysecondset
print(divisionset)

interset = myfirstset & mysecondset
print(interset)

syndifset = myfirstset ^ mysecondset
print(syndifset)

if myfirstset.isdisjoint(mysecondset):
    pass


def compare(story1, story2):
    words1 = story1.split(" ")
    words2 = story2.split(" ")
    wordset1 = {}
    wordset2 = {}
    # method 2 for list to set
    wordset1alt = {item for item in words1}

    # method 3 for list to set
    wordset1simple = set(words1)
    wordset2simple = set(words2)

    # commonwords = interset(wordset1simple, wordset2simple)


print(compare("Ik ging naar eens naar een bakker en ze hadden daar geen croissant",
              "Jonas is een slimme bakker omdat hij zij boekentas volstopt met croissants"))


def compare2(story1, story2):
    words1 = story1.split(" ")
    words2 = story2.split(" ")
    wordset1 = {}
    wordset2 = {}

    wordset1 = set(words1)
    wordset2 = set(words2)
    commonwords = wordset1 & wordset2
    commonwords2 = set()

    for word in commonwords:
        if words1.count(word) == words2.count(word):
            commonwords2.add(word)
    resulttuple = tuple(commonwords2)
    return resulttuple


print(compare2("banaan banaan boom", "banaan boom"))


def compare3stories(story1, story2, story3):
    words1 = set(story1.split(" "))
    words2 = set(story2.split(" "))
    words3 = set(story3.split(" "))
    intersectionwords = words1 & words2
    return intersectionwords.issubset(words3)


print(compare3stories("banaan croissant boa", "croissant boa", "boa croissant stokbrood"))

# this is a dictionary not a set!
# als key kan elk datatype gebruikt worden
exampledictionary = {"naam": "Jasper", "achternaam": "Verbruggen", "leeftijd": 16}
exampledictionary.update({"woonplek": "Mechelen", "favo kleur": "rood"})
print(exampledictionary)


def verjaar(person):
    leeftijd = exampledictionary.get("leeftijd")
    leeftijd += 1
    person.update({"leeftijd": leeftijd})
    return person


print(verjaar(exampledictionary))


def verhuis(person, nieuweplek):
    print(f"oude woonplek: {person['woonplek']}")
    person.update(({"woonplek": nieuweplek}))
    print(person)


verhuis(exampledictionary, "Leuven")

print(exampledictionary.pop("achternaam"))
print(exampledictionary)

print(exampledictionary.keys())
print(exampledictionary.popitem())

print("woonplek" in exampledictionary)
print("Jasper" in exampledictionary)

# key value pair van de voornaam dictionary
personbook = {}

D = {"Achternaam": "Verbruggen", "leeftijd": 16}
personbook.update({"Jasper": D})

print(f"ah yes this is my personal data: {personbook}")
