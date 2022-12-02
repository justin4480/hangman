import unittest
from hangman.phrases import TVShows
from hangman.game import Game


class Tests(unittest.TestCase):
    def test_phrase(self):
        phrase = TVShows()
        self.assertTrue(isinstance(phrase.get_phrase(), str))

    def test_game(self):
        game = Game("heroes")
        self.assertEqual(game.allowed_guesses, 7)

    def test_letters_correctly_guessed(self):
        game = Game("abcde")
        game.letters_guessed = {*"abcxyz"}
        expected = {*"abc"}
        actual = set(game.letters_correctly_guessed())
        self.assertEqual(expected, actual)

    def test_letters_incorrectly_guessed(self):
        game = Game("abcde")
        game.letters_guessed = {*"abcxyz"}
        expected = {*"xyz"}
        actual = set(game.letters_incorrectly_guessed())
        self.assertEqual(expected, actual)

    def test_letters_yet_to_be_guessed(self):
        game = Game("abcde")
        game.letters_guessed = {*"abcxyz"}
        expected = {*"de"}
        actual = set(game.letters_yet_to_be_guessed())
        self.assertEqual(expected, actual)

    def test_check_lose_true(self):
        game = Game("xyz")
        game.allowed_guesses = 10
        game.letters_guessed = {*"abcdefghij"}
        self.assertTrue(game.check_lose())

    def test_check_lose_false(self):
        game = Game("the quick brown fox jumps over the lazy dog")
        game.allowed_guesses = 3
        game.letters_guessed = {*"abcdefghijklmnopqrstuvwxy"}
        self.assertFalse(game.check_lose())

    def test_check_win_true(self):
        game = Game("heroes")
        game.allowed_guesses = 10
        game.letters_guessed = {*"zpheros"}
        self.assertTrue(game.check_win())

    def test_check_win_false(self):
        game = Game("heroes")
        game.allowed_guesses = 10
        game.letters_guessed = {*"zph"}
        self.assertFalse(game.check_win())
