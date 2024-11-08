import sys

import bcrypt


class Song:
    def __init__(self, name, duration, artist, genre):
        self.__name = name
        self.__duration = duration
        self.__artist = artist
        self.__genre = genre

    def getname(self):
        return self.__name

    def getduration(self):
        return self.__duration

    def getarttist(self):
        return self.__artist

    def getgenre(self):
        return self.__genre

    def play(self):
        pass

    def pause(self):
        pass

    def skip(self):
        pass


class User:
    def __init__(self, user, password, friends=None, playlists=None):
        if friends is None:
            friends = []
        if playlists is None:
            playlists = []
        self.__user = user
        self.__password = password
        self.__friends = friends
        self.__playlists = playlists

    def addsongtoplaylist(self, song, playlist):
        if playlist in self.__playlists:
            return playlist.addsong(song)
        return None

    def getplaylists(self):
        return self.__playlists

    def createplaylist(self, name):
        playlist = Playlist(name, [])
        self.__playlists.append(playlist)
        return playlist

    def removeplaylist(self, playlist):
        return self.__playlists.remove(playlist)

    def addtoplaylists(self, playlist):
        return self.__playlists.append(playlist)

    def addfriend(self, user):
        self.__friends.append(user)

    def removefriend(self, user):
        if user in self.__friends:
            return self.__friends.remove(user)
        return "not friend"

    def getuser(self):
        return self.__user

    def setuser(self, username):
        self.__user = username

    def getpassword(self):
        return self.__password

    def setpassword(self, password):
        self.__password = password

    def getfriends(self):
        return self.__friends

    def setfriends(self, friends):
        self.__friends = friends

    def removesongfromplaylist(self, song, playlist):
        if playlist in self.__playlists:
            playlist.removesong(song)
        else:
            return "no access"


class Playlist:
    def __init__(self, name, songs):
        self.__name = name
        self.__songs = list(songs)

    def getsongs(self):
        return self.__songs

    def removesong(self, song):
        if song in self.__songs:
            self.__songs.remove(song)
        else:
            return "no access"

    def addsong(self, song):
        return self.getsongs().append(song)

    def getsong(self):
        return self.__songs

    def getname(self):
        return self.__name

    def setname(self, name):
        self.__name = name


def main():
    username = input("name?\n")
    password = input('What is your password\n')
    password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashedpassword = bcrypt.hashpw(password, salt)
    friends = []
    playlists = []
    user = User(username.title(), hashedpassword, friends, playlists)
    printstring = (f"name: {user.getuser()}\n"
                   f"password: {password}\n"
                   f"hashed password: {user.getpassword()}\n"
                   f"friends: {user.getfriends()}\n "
                   f"playlists: {user.getplaylist()}")
    print(printstring)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
