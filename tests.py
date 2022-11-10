import unittest
from hangman import Hangman

def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

class TestHangman(unittest.TestCase):

    def setUp(self):
        self.hangman = Hangman('The Matrix')
        
    def tearDown(self):
        None

    def test_get_secret_grid_guessed_none(self):
        self.assertEqual(self.hangman.get_secret_grid(), '_ _ _   _ _ _ _ _ _')

    def test_get_secret_grid_guess_some(self):
        self.hangman.avalible_guess = list('abcdefghijklnopqrstuvwyz')
        self.assertEqual(self.hangman.get_secret_grid(), '_ _ _   M _ _ _ _ x')

    def test_get_secret_grid_guessed_all(self):
        self.hangman.avalible_guess = list('wyz')
        self.assertEqual(self.hangman.get_secret_grid(), 'T h e   M a t r i x')

run_tests(TestHangman)