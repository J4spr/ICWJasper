import sys

import bcrypt


class User:
	def __init__(self, username, password, threads=None):
		if threads is None:
			threads = []
		self.__username = username
		self.__password = password
		self.__threads = threads

	def createThread(self):
		text = input("Enter your text:\n")
		newthread = Thread(self.__username, text, [])

	def pinThread(self, thread):
		return self.__threads.append(thread)

	def unpinThread(self):
		return self.__threads.pop()

	def getPinnedThreads(self):
		return self.__threads

	def getusername(self):
		return self.__username


class Thread:
	def __init__(self, owner, text, commentlist):
		self.__owner = owner
		self.__text = text
		self.__commentlist = commentlist

	def showPostWithComments(self):
		pass

	def showContent(self):
		pass

	def getOwner(self):
		return self.__owner

	def gettext(self):
		return self.__text


class Comment:
	def __init__(self, text, owner):
		self.__text = text
		self.__owner = owner

	def showContent(self):
		return f"{self.__text}\n{self.__owner}"


def main():
	user = login("jasper", "admin")
	showwall(user.getPinnedThreads())


def login(username, password):
	password = password.encode('utf-8')
	salt = bcrypt.gensalt()
	hashedpassword = bcrypt.hashpw(password, salt)
	return User(username, hashedpassword, [])


def showwall(threadlist):
	for thread in threadlist:
		print(f"{thread.getOwner()}\n{thread.gettext()}")


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		sys.exit(130)
