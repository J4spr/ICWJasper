import random
import time

# set answer to yes on the question to play again
answer = "yes"
# ask the necessary stuff to start the program good
name = input("Whats your name: ")
time.sleep(1)

# use while loop to continue on and on until player doesn't want to play again
while True:
    # ask minimum to the player
    min = int(input("What do you want to be the minimum:"))
    time.sleep(1)
    # ask maximum to player
    max = int(input("What do you want to ben the maximum:"))
    time.sleep(1)

    # put random value in variable so we can compare in if statement
    number = random.randint(min, max)

    maxAttempts = 5

    # make for loop to continue til number is guessed right
    for i in range(maxAttempts):
        guess = int(input("What's your guess"))
        # compare the random number with the player guess
        if number == guess:
            print("You guessed right")
            break
        elif number < guess:
            print("Too high")
        elif number > guess:
            print("Too low")

    answer = input(f'Do you want to play again? (Yes/No), {name}')

    if answer == "no":
        # if player says no break out of while loop and exit program
        break
    elif answer == "yes":
        # if player says yes start while loop from beginning
        continue
