import unittest

from lessons.testing.SpotIffy.spottify import *


class TestUserClass(unittest.TestCase):
    pass


class TestUserAddSOngToPLaylist(unittest.TestCase):
    def test_add_song_to_playlist(self):
        playlist = Playlist("jasper", [])
        user = User("jasper", "lol", [], [playlist])
        song = Song("name", 0, "artist", "genre")

        user.addsongtoplaylist(song, playlist)
        self.assertTrue(song in playlist.getsongs())


class TestCreatePLaylist(unittest.TestCase):
    def test_create_playlist(self):
        user = User("jasper", "password", [], [])
        playlist = user.createplaylist("name")
        self.assertTrue(playlist in user.getplaylists())

    def test_create_only_one(self):
        user = User("jasper", "password", [], [])
        playlist = user.createplaylist("name")

        self.assertEqual(len(user.getplaylists()), 1)

    def test_addsong_to_playlist(self):
        user = User("jasper", "password", [], [])
        playlist = Playlist("jasper", [])

        self.assertEqual(len(user.getplaylists()), 0)


class TestUserRemovePlaylist(unittest.TestCase):
    def test_remove_pLaylist(self):
        playlist = Playlist("jasper", [])
        user = User("jasper", "password", [], [playlist])

        user.removeplaylist(playlist)
        self.assertTrue(playlist not in user.getplaylists())

    def test_remove_double_owner_playlist(self):
        user1 = User("jasper", "password", [], [])
        user2 = User("jasper2", "password2", [], [])
        playlist = user1.createplaylist("name")

        user2.addtoplaylists(playlist)

        user1.removeplaylist(playlist)
        self.assertTrue(playlist in user2.getplaylists())


class TestUserAddToPlaylists(unittest.TestCase):
    def test_add_to_playlists(self):
        playlist = Playlist("jasper", [])
        user = User("jasper", "jasper", [], [])

        user.addtoplaylists(playlist)
        self.assertTrue(playlist in user.getplaylists())


class TestRemoveSongFromPlaylist(unittest.TestCase):
    def test_remove_song_from_playlist(self):
        song = Song("name", 0, "artist", "genre")
        playlist = Playlist("name", [song])
        user = User("username", "password", [], [])

        self.assertEqual(user.removesongfromplaylist(song, playlist), "no access")


class TestUseraddFriend(unittest.TestCase):
    def test_addfriend(self):
        user1 = User("jasper", "password", [], [])
        user2 = User("username", "password", [], [])

        user1.addfriend(user2)
        self.assertTrue(user2 in user1.getfriends())

    def test_removefriend(self):
        user1 = User("jasper", "password", [], [])
        user2 = User("username", "password", [user1], [])

        user2.removefriend(user1)
        self.assertTrue(user1 not in user2.getfriends())

    def test_removefriendifnotfriends(self):
        user1 = User("jasper", "password", [], [])
        user2 = User("username", "password", [], [])

        self.assertEqual(user2.removefriend(user1), "not friend")
