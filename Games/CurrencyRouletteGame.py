
import random
import time
import yfinance as yf
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


class CurrencyRouletteGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.interval = self.get_money_interval()

    def is_won(self):
        return self.won

    def get_money_interval(self):
        logging.debug("Retrieving exchange rate from Yahoo Finance...")
        ticker = yf.Ticker("USDILS=X")
        history = ticker.history(period="1m")
        current_rate = history["Close"].iloc[-1]
        logging.debug(f"Exchange rate retrieved: {current_rate}")
        total_value = random.randint(1, 100)
        return total_value - (5 - self.difficulty), total_value + (5 - self.difficulty), current_rate

    def get_guess_from_user(self):
        time.sleep(2)
        return float(input(f"Enter your guess for the value of {self.interval[0]} USD in ILS: "))

    def play(self):
        try:
            while True:
                try:
                    user_guess = self.get_guess_from_user()
                    if self.interval[0] <= user_guess <= self.interval[1]:
                        print("Congrats, You won the game.")
                        self.won = True
                        return
                    else:
                        print("Sorry, you lost the game.")
                        return False
                except ValueError: print("Please enter a number, not a string.")
        except KeyboardInterrupt: logging.info("Program interrupted by user. Exiting...")


