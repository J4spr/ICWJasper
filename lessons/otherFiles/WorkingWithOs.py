# Import the os module (presumably for working with the operating system).
import os

# Print the current working directory using the os.getcwd() function.
print(os.getcwd())

# Change the current working directory to a specific path.
os.chdir("C:/Users/jasper.verbruggen/OneDrive - VTI Leuven/Documenten/rommel/stuff")

# Print the updated current working directory.
print(os.getcwd())

# List the files and directories in the current directory using os.listdir() and print the results.
print(os.listdir())

# Change the current working directory to a different path.
os.chdir("/")

# Open a file named "cleartext" in read-only mode and print its contents.
file1 = open("cleartext")
print(file1.read())

# Use a context manager (with statement) to open "cleartext" and print its contents.
with open("cleartext") as file1:
    print(file1.read())

# Open "cleartext" in write mode and write some text to it.
with open("cleartext", "w") as writeable:
    writeable.write("Dit is het eerste lijntje in mijn textfile \nen dit het 2de")

# List and print the attributes (functions, objects) of the built-in Python module (__builtins__).
for i in dir(locals()["__builtins__"]):
    print(i)

# Attempt to take user input for a number between 1 and 10.
try:
    number = input("geef een nummer tussen 1 en 10")

    # Check if the input number is outside the specified range and raise an ArithmeticError if so.
    if number < 1 or number > 10:
        raise ArithmeticError

    # Print a message if the number is greater than 5.
    if number > 5:
        print("je zit in de bovenste helft")

except ValueError:
    # Handle an error where the user didn't provide a valid number.
    print("geen correct nummer")

except ArithmeticError:
    # Handle the case where the number is outside the specified range.
    print("geen correct nummer")

except:
    # Handle any other unexpected errors.
    print("geen correct nummer")

else:
    # If no errors were raised, print a success message.
    print("geen errors jonge")

# Attempt to take user input for an even number using the input function.
try:
    number = int(input("geef een even nummer"))

    # Check if the number is not even and raise an AssertionError if so.
    assert number % 2 == 0

except AssertionError:
    # Handle the case where the input number is not even.
    print("ge hebt geen even nummer ingegeven")

else:
    # If the number is even, print a success message.
    print("ge hebt wel een even nummer ingegeven")
