import os
import sys

from OnlineGameStoreClasses import *

os.chdir("./projects/gamestore")
games = []
customerlist = []
customerfile = "customers.txt"
gamesfile = "games.txt"
orderfile = "orders.txt"


def menu():
    print("-------------------------------")
    print("Menu:")
    print("1. Add new game")
    print("2. Add stock")
    print("3. show users")
    print("4. Quit")
    print("-------------------------------")


def readgames():
    with open('games.txt', "r") as file:
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
                newcustomer = Customer(items[0], items[1], items[2], items[3])
                customerlist.append(newcustomer)
            elif len(items) != 4:
                pass
    return customerlist


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


def emptygame():
    with open(gamesfile, "w") as f:
        f.truncate()


def addgame():
    readgames()
    title = input("What is the title that you want to add?\n")
    genre = input("is it a competive or a cooperative game?\n")
    price = input("what price do you want it to be?\n")
    quantity = input(f"How many of {title} did you buy?\n")
    match genre:
        case "competitive":
            minp = input("What is the minimum amount of players required?\n")
            maxp = input("What is the maximum amount of players required?\n")
            newgame = Competitive(title, price, quantity, minp, maxp)
            games.append(newgame)
        case "cooperative":
            difficulty = input("What difficulty would you rate this?\n")
            newgame = Cooperative(title, price, quantity, difficulty)
        case _:
            print("You faggot you made a typing mistake!!!\n")


def main():
    readcustomers()
    readgames()
    menu()
    action = int(input("What do you want to do?"))
    while True:
        match action:
            case 1:
                addgame()
                writegames()
            case 2:
                pass
            case 3:
                # Use a loop to print information about all customers
                for k in range(len(customerlist)):
                    print(f"{k + 1}. {customerlist[k].displayinfo()}")
            case 4:
                break
            case _:
                pass


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted")
        sys.exit(130)
