taskarray = []


def menu():
    global userinput
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")
    print("")
    userinput = input("Enter your choice (1/2/3/4): ")


def main():
    global taskarray

    def addtask(taskarray, value):
        taskarray.append(value)

    def viewtasks(taskarray):
        print("---------------------------------")
        for i in range(len(taskarray)):
            print(taskarray[i])
        print("---------------------------------")

    def removetask(taskarray, value):
        taskarray.remove(value)

    while True:

        menu()
        if userinput == "1":
            value = input("What do you want to add: ")
            addtask(taskarray, value)
            print(f"{value} was added to the list")
        elif userinput == "2":
            viewtasks(taskarray)
        elif userinput == "3":
            value = input("What do you want to remove: ")
            removetask(taskarray, value)
            print(f"{value} was removed from the list")
        elif userinput == "4":
            print("Goodbye!")
            break


if __name__ == '__main__':
    main()
