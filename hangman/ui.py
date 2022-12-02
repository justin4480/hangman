import os


class UI:
    def get_user_input(self):
        valid_input = False
        while not valid_input:
            user_input = input("enter guess: ").lower()
            valid_input = self.check_valid_input(user_input)
        return user_input

    def check_valid_input(self, user_input):
        return True

    def draw(self, screen):
        os.system("clear")
        print(screen)
