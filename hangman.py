# hangman.py
import random
import os


class Hangman(object):

    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    def __init__(self, secret_word: str, guesses: int = 7):
        self.secret_word = secret_word
        self.avalible_guess = list("abcdefghijklmnopqrstuvwxyz")
        self.totalguesses = guesses
        self.remainingguesses = guesses

    def get_secret_grid(self) -> str:
        return " ".join(
            [
                letter if letter.lower() not in self.avalible_guess else "_"
                for letter in self.secret_word
            ]
        )

    def get_remaining_letters(self) -> str:
        return " ".join(
            [
                letter if letter in self.avalible_guess else "_"
                for letter in self.alphabet
            ]
        )

    def get_remaining_guesses(self) -> str:
        return f"{self.remainingguesses} of {self.totalguesses} guesses remaining"

    def display_board(self) -> None:
        os.system("clear")
        print(self.get_secret_grid(), "\n")
        print(self.get_remaining_letters(), "\n")
        print(self.get_remaining_guesses(), "\n")

    def get_player_guess(self):
        while True:
            letter = input("Guess a letter: ")
            if letter.lower() not in self.avalible_guess:
                print("Not an appropriate choice.")
                continue
            if letter.lower() not in self.secret_word.lower():
                self.remainingguesses -= 1
            self.avalible_guess.remove(letter.lower())
            break

    def check_for_win(self) -> bool:
        return (
            len(set(self.avalible_guess).intersection(set(self.secret_word.lower())))
            == 0
        )

    def check_for_loose(self) -> bool:
        return self.remainingguesses == 0 and not self.check_for_win()

    def run_game(self):
        self.display_board()
        while True:
            self.get_player_guess()
            self.display_board()
            if self.check_for_win():
                print("You win!", "\n")
                break
            if self.check_for_loose():
                print("You lose!", "\n")
                break


def main():
    while True:
        movies = [
            "Alice in Wonderland",
            "Toy Story 3",
            "Cars 2",
            "Winnie the Pooh",
            "The Muppets",
            "Wreck-It Ralph",
            "Monsters University",
            "Frozen",
            "Big Hero 6",
            "Inside Out",
            "The Good Dinosaur",
            "Moana",
            "Beauty and the Beast",
            "Coco",
            "Incredibles 2",
            "Aladdin",
            "The Lion King",
        ]
        hangman = Hangman(random.choice(movies))
        hangman.run_game()
        if input("Press enter to play again: ") != "":
            break


if __name__ == "__main__":
    main()
