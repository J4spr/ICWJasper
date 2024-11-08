import json
import sys
from getpass import getpass

userfile = "./projects/login/users.json"


def main():
	while True:
		menu()
		# catch the error when the user doesnt input anything
		try:
			useraction = int(input("What do you want to do?\n"))
		except ValueError:
			continue
		match useraction:
			case 1:
				username = askusername()
				password = askpassword()
				writetojson(userfile, username, password)

			case 2:
				username = input("Enter your username\n")
				password = getpass(prompt="Enter your password\n")
				print(login(username, password))

			case 3:
				break

			case _:
				continue


def menu():
	print("1. Create an account")
	print("2. Login")
	print("2. Exit")
	print("----------------------")


def login(username, password):
	with open(userfile, 'r') as file:
		# load the json file into a dictionary
		users = json.load(file)
		# check if user exists and that the password is correct
		if users.get(username) == password:
			return "succesful login"


# a function that keeps asking for a username until it is actually valid
def askusername():
	# make the username an empty string because otherwise I cant give it as a parameter
	# but this isnt a problem because empty = not valid so it keeps asking for a valid input
	continueloop = False
	username = ""
	while not continueloop:
		username = input("Enter a username of 2-24 characters\n")
		continueloop = check_valid_username(username)
	return username


# a function that keeps asking for a password until it is actually valid
def askpassword():
	# make the password an empty string because otherwise I cant give it as a parameter
	# but this isnt a problem because empty = not valid so it keeps asking for a valid input
	continueloop = False
	password = ""
	while not continueloop:
		password = getpass(prompt="Enter a password of 8-24 characters\n")
		continueloop = check_valid_password(password)
	return password


# load the json file into a dictionary
def readfromjson():
	with open(userfile, 'r') as file:
		users = json.load(file)
	return users


# writes to json file if the user creates an account
def writetojson(jsonfile, username, password):
	usersdict = readfromjson()
	usersdict.update({username: password})
	# dont need to do error handling because this creates the file automatically when not exist
	with open(jsonfile, 'w') as file:
		json.dump(usersdict, file)

# check if the user has inputted a valid username
def check_valid_username(username):
	# all valid characters in one string
	valid_characters = "-_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	# return if length is too short
	if len(username) < 2:
		print("Too short")
		return False
	# return if length is too long
	if len(username) > 24:
		print("Too long")
		return False
	# check if the username already exists
	users = readfromjson()
	if users.get(username):
		print("Username already taken")
		return False
	for char in username:
		if char not in valid_characters:
			return False
	return True


def check_valid_password(password):
	# all valid characters in one string
	valid_characters = "-_.?!;+=*,abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
	# return if length is too short
	if len(password) < 8:
		print("Too short")
		return False
	# return if length is too long
	if len(password) > 24:
		print("Too long")
		return False
	for char in password:
		if char not in valid_characters:
			return False
	return True


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit(130)
