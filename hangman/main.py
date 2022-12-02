from phrases import TVShows, Movies
from game import Game
from ui import UI


def main():
    phrases = Movies()
    game = Game(phrases.get_phrase())
    ui = UI()

    ui.draw(game.__str__())

    while game.state == "playing":
        game.letters_guessed.append(ui.get_user_input())
        game.process_events()
        ui.draw(game.__str__())

    print(game.state)


if __name__ == "__main__":
    main()
