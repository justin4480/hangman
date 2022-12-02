from abc import ABC
import random


class Phrase(ABC):
    def __init__(self, phrases):
        self.phrases = phrases
        self.shuffle_phrases()

    def shuffle_phrases(self):
        random.shuffle(self.phrases)

    def get_phrase(self):
        if len(self.phrases) == 0:
            raise IndexError("phrases list is empty")
        return self.phrases.pop()


class Movies(Phrase):
    def __init__(self):
        super().__init__([
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
        ])


class TVShows(Phrase):
    def __init__(self):
        super().__init__(["Wednesday", "Heroes", "Dark"])
