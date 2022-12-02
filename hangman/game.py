class Game:
    ALPHABET = list("abcdefghijklmnopqrstuvwxyz")

    def __init__(self, secret_phrase):
        self._secret_phrase = secret_phrase
        self.letters_guessed = []
        self.allowed_guesses = 7
        self.state = "playing"

    @property
    def secret_phrase(self):
        return self._secret_phrase.lower()

    def secret_phrase_case_sensitive(self):
        return self._secret_phrase

    def process_events(self):
        if self.check_win():
            self.state = "win"
        if self.check_lose():
            self.state = "Lose"

    def letters_correctly_guessed(self):
        return set(self.letters_guessed).intersection(set(self.secret_phrase))

    def letters_incorrectly_guessed(self):
        return set(self.letters_guessed).difference(set(self.secret_phrase))

    def letters_yet_to_be_guessed(self):
        return (
            set(self.secret_phrase)
            .difference(set(self.letters_guessed))
            .intersection(set(Game.ALPHABET))
        )

    def check_win(self):
        return len(self.letters_yet_to_be_guessed()) == 0

    def check_lose(self):
        return len(self.letters_incorrectly_guessed()) >= self.allowed_guesses

    def get_lives(self):
        return (
            f"{self.allowed_guesses - len(self.letters_incorrectly_guessed())} "
            f"guesses remaining"
        )

    def get_guesses(self):
        return " ".join(["_" if i in self.letters_guessed else i for i in Game.ALPHABET])

    def get_board(self):
        return " ".join(
            [
                "_" if i.lower() in self.letters_yet_to_be_guessed() else i
                for i in self._secret_phrase
            ]
        )

    def __str__(self):
        return f"{self.get_lives()}\n\n{self.get_guesses()}\n\n{self.get_board()}\n"
