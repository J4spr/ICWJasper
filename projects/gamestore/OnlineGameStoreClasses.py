# r = redis.Redis(host='localhost', port=6379)


# Define a class for representing game products
class Game:
    def __init__(self, title, price, quantity):
        # Private price attribute
        self.__price = str(price)
        # Private title attribute
        self.__title = title
        # Private quantity attribute
        self.__quantity = str(quantity)

    def gettitle(self):
        return str(self.__title)

    def getprice(self):
        return str(self.__price)

    def getstock(self):
        return str(self.__quantity)

    def getquantity(self):
        return self.__quantity

    def displayinfo(self):
        # Format and return game information
        returnstring = f"{self.gettitle()}: €{self.getprice()} // Quantity in stock: {self.getquantity()}"
        return returnstring

    def setquantity(self, quantity):
        self.__quantity = quantity

    def addstock(self, addedstock):
        self.__quantity += addedstock

    def removestock(self, removedstock):
        self.__quantity -= removedstock


class Competitive(Game):
    def __init__(self, title, price, quantity, minprice, maxprice):
        super().__init__(title, price, quantity)
        self.__min = str(minprice)
        self.__max = str(maxprice)

    def getmin(self):
        return str(self.__min)

    def getmax(self):
        return str(self.__max)


# --------------------------------------------------------------------------------------
class Cooperative(Game):
    def __init__(self, title, price, quantity, difficulty):
        super().__init__(title, price, quantity)
        self.__dificulty = difficulty

    def getdifficulty(self):
        return self.__dificulty


# --------------------------------------------------------------------------------------
# Define a class for representing customers
class Customer:
    def __init__(self, fname, lname, address, purchased):
        # Private first name attribute
        self.__fname = fname
        # Private last name attribute
        self.__lname = lname
        # Private address attribute
        self.__address = address
        # Private number of games purchased attribute
        self.__purchased = purchased

    def displayinfo(self):
        # Format and return customer information
        # {first name} {last name} lives at {address}. Purchased games: {purchased}
        returnstring = f"{self.__fname} {self.__lname} lives at {self.__address}. Purchased games: {self.__purchased}"
        return returnstring

    def getname(self):
        return self.__fname

    def getlastname(self):
        return self.__lname

    def getaddress(self):
        return self.__address

    def getpurchasedgames(self):
        return self.__purchased

    def updatepurchasedgames(self, newdict):
        self.__purchased.update(newdict)


# --------------------------------------------------------------------------------------
# Define an empty Order class (not used in this code)
class Order:
    def __init__(self, customer, gamelist, totalprice):
        self.__customer = customer
        self.__games = gamelist
        self.__totalprice = totalprice

    def getcustomer(self):
        return self.__customer

    def getgames(self):
        return self.__games

    def gettotalprice(self):
        return self.__totalprice
