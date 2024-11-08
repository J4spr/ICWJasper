import os
import sys

from OnlineGameStoreClasses import *

# --------------------------------------------------------------------------------------
print(os.getcwd())
os.chdir("./projects/gamestore")
print(os.getcwd())
cart = dict()
games = []
customerlist = []
orders = []
customerfile = "customers.txt"
gamesfile = "games.txt"
orderfile = "orders.txt"


# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

def menu():
    print("-------------------------------")
    print("Menu:")
    print("1. Browse games")
    print("2. Purchase games")
    print("3. show users")
    print("4. Quit")
    print("-------------------------------")


# --------------------------------------------------------------------------------------
# Define a function to create a menu of game options
def addtoinput(gamelist):
    inputstring = "("
    for game in range(len(gamelist)):
        inputstring += str(game + 1)
        if game + 1 != len(gamelist):
            inputstring += "/"
    inputstring += ")"
    return inputstring


# --------------------------------------------------------------------------------------
def addtocart():
    cartsummary = {}
    for item in cart:
        cartsummary.update({item: cart[item]})
    return cartsummary


# --------------------------------------------------------------------------------------
def readgames():
    with open(gamesfile, "r") as file:
        readstring = file.read()
        gamelist = readstring.split("\n")
        # print(games)
        for game in gamelist:
            items = game.split("/")
            if items[0] == "0":
                newgame = Cooperative(items[1], items[2], items[3], items[4])
                games.append(newgame)
            elif items[0] == "1":
                newgame = Competitive(items[1], items[2], items[3], items[4], items[5])
                games.append(newgame)
    return games


def readcustomers():
    with open(customerfile, "r") as file:
        readstring = file.read()
        customerdata = readstring.split("\n")
        for customer in customerdata:
            items = customer.split("/")
            if len(items) == 4:
                if items[3] == "":
                    dictionary = {}
                else:
                    dictionary = {}
                    items[3].split(":")
                    # TODO: fix this
                newcustomer = Customer(items[0], items[1], items[2], dictionary)
                customerlist.append(newcustomer)
            elif len(items) != 4:
                print(f"skipped a line due to insufficient data: {customer}")
    return customerlist


def readorders():
    with open(orderfile, "r") as file:
        readstring = file.read()
        orderdata = readstring.split("\n")
        for order in orderdata:
            items = order.split("/")


# --------------------------------------------------------------------------------------

def writegames():
    emptygame()
    for game in games:
        writestring = ""
        writestring += (game.gettitle() + "/")
        writestring += (game.getprice() + "/")
        writestring += (str(game.getquantity()) + "/")
        if isinstance(game, Cooperative):
            writestring += game.getdifficulty()
            writestring = ("0/" + writestring)
            writestring += "\n"
        #     0 is een coop game
        elif isinstance(game, Competitive):
            writestring += (game.getmin() + "/")
            writestring += (game.getmax())
            writestring = ("1/" + writestring)
            writestring += "\n"
        #     1 is een comp game

        """
        Output van de writestring: 
        Voor game1:
        1/CallOfDuty/50/10/2/4
        Voor game2:
        0/BattleBorn/40/5/medium
    
        """
        with open(gamesfile, "a") as file:
            file.write(writestring)


def writecustomers():
    emptycustomers()
    for customer in customerlist:
        writestring = ""
        writestring += (customer.getname() + "/")
        writestring += (customer.getlastname() + "/")
        writestring += (customer.getaddress() + "/")
        writestring += str(customer.getpurchasedgames())
        writestring += "\n"

        """
        Output van de writestring: 
        Voor game1:
        1/CallOfDuty/50/10/2/4
        Voor game2:
        0/BattleBorn/40/5/medium
    
        """
        with open(customerfile, "a") as file:
            file.write(writestring)


def writeorders():
    emptyorders()
    with open(orderfile, 'a') as file:
        with open(orderfile, 'a') as file:
            for order in orders:
                try:
                    writestring = ""
                    writestring += f"{order.getcustomer()}/"

                    cartstring = ""
                    for game in order.getgames():
                        cartstring += f"{game}:{order.getgames()[game]},"

                    writestring += f"{cartstring}/"
                    writestring += f"{str(order.gettotalprice())}\n"

                    file.write(writestring)

                except Exception as e:
                    print(f"Error processing order: {e}")


# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
def emptygame():
    with open(gamesfile, "w") as f:
        f.truncate()


def emptycustomers():
    with open(customerfile, "w") as f:
        f.truncate()


def emptyorders():
    with open(orderfile, "w") as f:
        f.truncate()


# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------
def browsegames():
    game = None
    # Use a loop to print information about all games
    for j in range(len(games)):
        if int(games[j].getquantity()) <= 0:
            # game has no items left
            print(f"{games[j].gettitle()} has no items left")
        else:
            print(f"{j + 1}. {games[j].displayinfo()}")
    # Call addtoinut
    inputstring = addtoinput(games)
    # Prompt the user to choose a game
    while True:
        gameint = int(input(f"Choose 1 of the games {inputstring}"))
        if gameint > len(games):
            print("You cant choose that game it doesnt exist")
            continue
        else:
            game = games[gameint - 1]
            break
    while True:
        gamequantity = int(input(f"How many of  do you want to buy"))
        if gamequantity > int(game.getquantity()):
            print("We dont have so many stock")
        else:
            game.setquantity(int(game.getquantity()) - int(gamequantity))
            break

    cart.update({game: gamequantity})


def calculatetotalprice():
    totalprice = 0
    for game in cart:
        totalprice += int(game.getprice()) * int(game.getquantity())
    return totalprice


def purchasegames(customerarray):
    # currentcustomer = ''
    name = input("Enter your first name")
    name = name.title()
    for customer in customerarray:
        if customer.getname() == name:
            currentcustomer = customer
            print(f"Hello {name} your games are purchased")
            break
    else:
        lastname = input("Give your last name too: ")
        adress = input("And your adress")
        currentcustomer = Customer(name, lastname, adress, dict())
        customerarray.append(currentcustomer)

    newpurchasedgames = dict()
    for game in cart:
        newpurchasedgames.update({game.gettitle(): cart[game]})
    currentcustomer.updatepurchasedgames(newpurchasedgames)

    neworder = Order(currentcustomer.getname(), newpurchasedgames, calculatetotalprice())
    orders.append(neworder)

    cart.clear()
    return customerarray


# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

# Define the main function
def main():
    readgames()
    readcustomers()
    readorders()
    while True:
        menu()
        action = input("What do you want to do?\n")
        if len(action) > 0:
            action = int(action)
        else:
            print("You didn't enter anything")
            continue
        match action:
            case 1:
                browsegames()
            case 2:
                purchasegames(customerlist)
                writegames()
                writecustomers()
                writeorders()
            case 3:
                for k in range(len(customerlist)):
                    print(f"{k + 1}. {customerlist[k].displayinfo()}")
            case 4:
                break
            case _:
                menu()


# --------------------------------------------------------------------------------------
# Check if this script is the main program entry point
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted")
        sys.exit(130)
