from unittest import TestCase, mock
from lessons.testing.twitter.twitter import *


class TestCreateThread(TestCase):
	@mock.patch("lessons.testing.twitter.twitter.input", create=True)
	def test_createThread(self, mocked_input):
		mocked_input.side_effect = ['Albert', 'second input']
		user = User("username", "password", [])
		thread = Thread(user, "test", [])
		thread = user.createThread()
		self.assertEqual(thread.text, "Albert")

	@mock.patch("lessons.testing.twitter.twitter.input", create=True)
	def test_create_empty_thread(self, mocked_input):
		mocked_input.side_effect = ["", "test"]
		user = User("username", "password", [])
		thread = user.createThread()
		self.assertEqual(thread.gettext(), "test")

	@mock.patch("lessons.testing.twitter.twitter.input", create=True)
	def create_spaces_thread(self, mocked_input):
		mocked_input.side_effect = ["   ", "test"]
		user = User("username", "password", [])
		thread = user.createThread()
		self.assertEqual(thread.gettext(), "test")

	def create_thread_too_many_characters(self, mocked_input):
		user = User("username", "password", [])
		thread = user.createThread()
		# TODO: make long string
		mocked_input.side_effect = ["   ", "test"]
		self.assertTrue(thread in user.getThreads())


class TestPinThread(TestCase):
	def test_pin_thread_2_users(self):
		user = User("username", "password", [])
		user2 = User("username2", "password2", [])
		thread = Thread(user2, "test", [])
		user2.pinThread(thread)
		self.assertTrue(thread in user2.getPinnedThreads())

	def test_pin_own_thread(self):
		user = User("username", "password", [])
		thread = Thread(user, "test", [])
		user.pinThread(thread)
		self.assertTrue(thread in user.getPinnedThreads())

	def test_unpin_thread(self):
		user = User("username", "password", [])
		thread = Thread(user, "test", [])
		user.pinThread()
		user.unpinThread()
		self.assertTrue(thread not in user.getPinnedThreads())

	def test_unpin_thread_not_pinned(self):
		user = User("username", "password", [])
		thread = Thread(user, "test", [])
		user.unpinThread()
		self.assertTrue(thread not in user.getPinnedThreads())


class TestCreateComment(TestCase):
	def test_createComment(self, mocked_input):
		mocked_input.side_effect = ['Albert', 'second input']
		user = User("username", "password", [])
		thread = Thread(user, "test", [])
		thread = user.createComment()
		self.assertEqual(thread.text, "Albert")

	@mock.patch("lessons.testing.twitter.twitter.input", create=True)
	def test_create_empty_comment(self, mocked_input):
		mocked_input.side_effect = ["", "test"]
		user = User("username", "password", [])
		thread = user.createComment()
		self.assertEqual(thread.gettext(), "test")

	@mock.patch("lessons.testing.twitter.twitter.input", create=True)
	def create_spaces_comment(self, mocked_input):
		mocked_input.side_effect = ["   ", "test"]
		user = User("username", "password", [])
		thread = user.createComment()
		self.assertEqual(thread.gettext(), "test")

	def create_comment_too_many_characters(self, mocked_input):
		user = User("username", "password", [])
		thread = user.createComment()
		# TODO: make long string
		mocked_input.side_effect = ["   ", "test"]
		self.assertTrue(thread in user.getThreads())
