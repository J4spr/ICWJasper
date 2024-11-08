class Parrot:
    name = ""
    age = 0


parrot1 = Parrot()
parrot1.name = "Jean"
parrot1.age = 5

parrot2 = Parrot()
parrot2.name = "Json"
parrot2.age = 10

print(f"{parrot2.name} is {parrot2.age} years old\n{parrot1.name} is {parrot2.age} years old")


class Animal:
    @staticmethod
    def eat():
        print("njam, goed gegeten")

    @staticmethod
    def drink():
        print("Nu overleef ik nog 3 dagen")


# Donkeyis een "instance" van Animal. Hij geeft alle attributen
# van Class Animal over (INHERITANCE)
class Donkey(Animal):
    @staticmethod
    def balk():
        print("LUIDE HINNIK")


# Hendrik kakn dus alles wat een Donkey kan, maar ook alles wat een Animal kan. GO HENDRIK
Hendrik = Donkey()
Hendrik.eat()
Hendrik.drink()
Hendrik.balk()

Fredje = Animal()


class Car:
    # init wordt automatisch met de opgeroepen bij creatie van een nieuwe instantie van een class
    def __init__(self):
        self.__price = 9000

    def sell(self):
        print(f"this car sells for {self.__price}")

    def setprice(self, newprice):
        if newprice > 10000:
            self.__price = newprice
        else:
            print("prijs te laag")


PaganiHuayra = Car()
PaganiHuayra.sell()
PaganiHuayra.__price = 1400000
PaganiHuayra.sell()
PaganiHuayra.setprice(54)
PaganiHuayra.sell()


class Veelhoek:
    def __init__(self, no_of_hoeks):
        self.aantalhoeken = no_of_hoeks
        self.sides = [0 for i in range(no_of_hoeks)]

    def setsides(self):
        sides = self.sides
        for i in range(self.aantalhoeken):
            sides[i] = input(f"Geef de {i + 1} zijde")
            sides = [input(f"Geef de {i + 1} zijde") for i in range(self.aantalhoeken)]

    def displaySides(self):
        for i in range(self.aantalhoeken):
            print(f"de {i + 1} zijde is {self.sides[i]} lang")


driehoek = Veelhoek(3)
driehoek.setsides()
driehoek.displaySides()


class Triangle(Veelhoek):
    def __init__(self):
        Veelhoek.__init__(self, 3)

    def isrealtriangle(self):
        s1 = self.sides[0]
        s2 = self.sides[1]
        s3 = self.sides[2]
        if (s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2):
            print("this triangle has realistic dimensions")
        else:
            print("This is a fake traingle")


nieuwediehoek = Triangle()
nieuwediehoek.displaySides()
nieuwediehoek.setsides()
nieuwediehoek
