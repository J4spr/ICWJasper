import os
import sys
from datetime import datetime

global action


def checkdate():
    now = datetime.now()
    currenttime = now.strftime("%d/%m/%Y")
    print(currenttime)


def texttodict(filedict):
    with open("Diary", "r") as file:
        for line in file:
            print(line)
            parts = line.strip().split(":")
            print(parts)
            filedict.update({parts[0]: parts[1]})
            print(f"{filedict}\n{parts}")
    return filedict


def menu():
    print("-------------------------------")
    print("Menu:")
    print("1. Write")
    print("2. Read a specific date")
    print("3. Quit")
    print("-------------------------------")
    action = int(input("What do you want to do? (1/2/3)\n"))
    return action


def read():
    # get the date from the user
    date = input("What date do you want to read your thoughts from?\n")

    # create an empty dictionary
    diarydict = {}

    # open the file and read its content
    with open("Diary", "r") as f:
        # loop through each line in the file
        for line in f:
            # split the line
            parts = line.strip().split(":")
            # if the date matches the user's input, add the text to the dictionary
            if parts[0] == date:
                diarydict[date] = parts[1]

    if date not in diarydict:
        print(f"No thoughts found for {date}")
    # print the text for the given date
    else:
        print(f"{date}:{diarydict[date]}")


def write(filedict, text, date):
    # add the story to the dictionary
    filedict[date] = text

    # open the file for appending
    with open("Diary", "a") as f:
        # write the date and text to the file
        f.write(f"{date}:{text}\n")


def main():
    checkdate()
    filedict = {}
    filedict = texttodict(filedict)
    while True:
        action = menu()
        try:
            actionasint = int(action)
        except ValueError:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue
        match actionasint:
            case 1:
                # get the date and story from the user
                date = input("Enter the date (YYYY-MM-DD): ")
                story = input("Enter your story: ")
                # add the story to the dictionary
                write(filedict, story, date)
                print("Story added to diary.")
            case 2:
                # read the diary entry for the given date
                read()
            case 3:
                print("Goodbye!")
                break
            case _:
                print("Invalid action. Please try again.")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted")
        sys.exit(130)
