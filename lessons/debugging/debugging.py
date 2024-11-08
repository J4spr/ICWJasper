class Car:
    def __init__(self):
        self.__speed = 0
        self.__distance = 0
        self.__timespent = 0

    def accelerate(self):
        self.timestep()
        self.__speed += 5

    def brake(self):
        self.timestep()
        self.__speed -= 5

    # every action is one timestep
    def timestep(self):
        self.__timespent += 1

    # print the average speed
    def avgspeed(self):
        self.timestep()
        avgspeed = self.__distance / self.__timespent
        print(avgspeed)

    # print the distance you have driven
    def showdistance(self):
        self.timestep()
        print(self.__distance)


newcar = Car()
while True:
    action = input("Would you like to [A]ccelerate, [B] brake, show average [S]peed or show the [D]istance\n")
    action = action.upper()
    match action:
        case "A":
            newcar.accelerate()
        case "B":
            newcar.brake()
        case "S":
            newcar.avgspeed()
        case "D":
            newcar.showdistance()
        case _:
            continue
