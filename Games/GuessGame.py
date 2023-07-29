
import random
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = None

    def is_won(self):
        return self.won

    def generate_number(self):
        self.secret_number = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        while True:
            try:
                guess = int(input(f"Enter a number between 1 and {self.difficulty}: "))
                if guess < 1 or guess > self.difficulty:
                    print(f"Please enter a number between 1 and {self.difficulty}: ")
                    continue
                return guess
            except ValueError: print("Please enter a number, not a string.")

    def compare_results(self, guess):
        if guess == self.secret_number: return "that's it!"
        elif guess < self.secret_number: return "the number is too low"
        else: return "the number is too high"

    def play(self):
        self.generate_number()
        try:
            while True:
                guess = self.get_guess_from_user()
                result = self.compare_results(guess)
                print(result)
                if result == "that's it!": 
                    self.won = True
                    return
                elif result == "the number is too low" or result == "the number is too high": continue
                else: return False
        except KeyboardInterrupt: logging.info("Program interrupted by user. Exiting...")



