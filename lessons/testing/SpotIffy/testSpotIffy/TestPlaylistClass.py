import unittest

from lessons.testing.SpotIffy.spottify import *


class TestPlaylistInit(unittest.TestCase):
    def test_init_songs(self):
        playlist = Playlist("name", [])
        self.assertEqual(playlist.getsongs(), [])

    def test_init_name(self):
        playlist = Playlist("name", [])
        msg = "[Error]"
        self.assertEqual(playlist.getname(), "name", msg)


class TestPlaylistsAddSong(unittest.TestCase):
    def test_playlist_addsong(self):
        playlist = Playlist("jasper", [])
        user = User("jasper", "lol", [], [playlist])
        song = Song("name", 0, "artist", "genre")

        playlist.addsong(song)
        playlist.removesong(song)
        msg = "[Error]"
        self.assertTrue(song not in playlist.getsong(), msg)

    def test_remove_song_multipleplaylists(self):
        song = Song("name", 0, "artist", "genre")
        playlist1 = Playlist("jasper", [song])
        playlist2 = Playlist("jasper2", [song])

        playlist1.removesong(song)
        msg = "[Error]"
        self.assertTrue(song in playlist2.getsong(), msg)

    def test_remove_song_multipletimes_in_playlist(self):
        song = Song("name", 0, "artist", "genre")
        playlist = Playlist("jasper", [song, song])

        playlist.removesong(song)
        msg = "[Error]"
        self.assertTrue(song in playlist.getsong(), msg)

    def test_add_song_multiple_times(self):
        song = Song("name", 0, "artist", "genre")
        playlist = Playlist("jasper", [])

        playlist.addsong(song)
        playlist.addsong(song)
        msg = "[Error]"
        self.assertEqual(2, len(playlist.getsong()), msg)

    def test_remove_song_not_in_playlist(self):
        song = Song("name", 0, "artist", "genre")
        playlist = Playlist("jasper", [])

        playlist.removesong(song)
