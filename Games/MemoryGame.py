
import random
import logging
import time

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def generate_sequence(self):
        return [random.randint(1, 101) for _ in range(self.difficulty)]

    def is_won(self):
        return self.won

    def get_list_from_user(self):
        user_list = []
        for number in range(self.difficulty):
            while True:
                try:
                    numbers = int(input(f"Enter number {number + 1}: "))
                    user_list.append(numbers)
                    break
                except ValueError: print("Please enter numbers, not letters.")
        return user_list

    def is_list_equal(self, list1, list2):
        return list1 == list2

    def play(self):
        try:
            start = self.generate_sequence()
            print(f"Memorize the following numbers: {start}")
            time.sleep(0.7)
            user_list = self.get_list_from_user()
            if self.is_list_equal(start, user_list):
                print("You won.")
                self.won = True
                return
            else:
                print("you lost.")
                return False
        except KeyboardInterrupt: logging.info("Program interrupted by user. Exiting...")




