class Game:
    def __init__(self, title, price, quatity):
        self.__title = title
        self.__price = price
        self.__stock = quatity

    def gettitle(self):
        return str(self.__title)

    def getprice(self):
        return str(self.__price)

    def getstock(self):
        return str(self.__stock)


class Competitve(Game):
    def __init__(self, title, price, quatity, min, max):
        super().__init__(title, price, quatity)
        self.__min = str(min)
        self.__max = str(max)

    def getmin(self):
        return str(self.__min)

    def getmax(self):
        return str(self.__max)


class Cooperative(Game):
    def __init__(self, title, price, quatity, difficulty):
        super().__init__(title, price, quatity)
        self.__dificulty = difficulty

    def getdifficulty(self):
        return self.__dificulty


game1 = Competitve("CallOfDuty", 50, 10, 2, 4)
game2 = Cooperative("BattleBorn", 40, 5, "medium")
games = []


def writegame(game):
    writestring = ""
    writestring += (game.gettitle() + "/")
    writestring += (game.getprice() + "/")
    writestring += (game.getstock() + "/")
    if isinstance(game, Cooperative):
        writestring += game.getdifficulty()
        writestring = ("0/" + writestring)
    #     0 is een coop game
    elif isinstance(game, Competitve):
        writestring += (game.getmin() + "/")
        writestring += (game.getmax())
        writestring = ("1/" + writestring)
    #     1 is een comp game
    writestring += "\n"

    """
    Output van de writestring: 
    Voor game1:
    1/CallOfDuty/50/10/2/4
    Voor game2:
    0/BattleBorn/40/5/medium

    """

    with open("games", "a") as file:
        file.write(writestring)


def readgame(games):
    with open("games", "r") as file:
        readstring = file.read()
        gamelist = readstring.split("\n")
        print(gamelist)
        for game in gamelist:
            items = game.split("/")
            if items[0] == "0":
                newgame = Cooperative(items[1], items[2], items[3], items[4])
            elif items[0] == "1":
                newgame = Competitve(items[1], items[2], items[3], items[4], items[5])
            games.append(newgame)
            return games


writegame(game1)
writegame(game2)
readgame(games)
print(games[0].gettitle())
