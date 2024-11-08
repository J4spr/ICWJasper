import random
import time

answer = "yes"
# ask the necessary stuff to start the program good
name = input("Whats your name: ")
time.sleep(1)

min = "a"
time.sleep(1)

max = "z"
time.sleep(1)

# make array so you can use the ints better with it
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x",
            "y", "z"]
# use while loop so we can ask user to play again
while True:
    # declare the max attempts
    maxAttempts = 5
    # get random index out array
    randomIndex = random.choice(range(len(alphabet)))
    # retrieve it
    letter = alphabet[randomIndex]

    # make for loop to continue til number is guessed right
    for i in range(maxAttempts):
        guess = input("What's your guess")
        if letter == guess:
            print("You guessed right")
            break
        elif letter < guess:
            print("Too far in the alphabet")
        elif letter > guess:
            print("Too closer in the alphabet")
    # ask user to play again
    answer = input(f'Do you want to play again? (Yes/No), {name}')

    if answer == "no":
        # break out of while loop if player says no
        break
    elif answer == "yes":
        # go on with the loop if player says yes
        continue
