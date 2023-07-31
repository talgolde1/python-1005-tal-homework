
from Games.CurrencyRouletteGame import CurrencyRouletteGame
from Games.GuessGame import GuessGame
from Games.MemoryGame import MemoryGame
from Scores.Score import add_score


def welcome(name):
    return f"Hello {name} and welcome to the World of Games (WoG). Here you can find many cool games to play."


def load_game():
    print('''Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
    2. Guess Game - guess a number and see if you chose like the computer
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS
    ''')

    while True:
        game = input("Enter the game number (1-3): ")
        if game.isdigit() and game in ["1", "2", "3"]:
            break
        print("Please enter a number between 1 and 3.")

    while True:
        difficulty = input("Please choose game difficulty from 1 to 5: ")
        if difficulty.isdigit() and 1 <= int(difficulty) <= 5:
            break
        print("Please enter a number between 1 and 5.")

    if game == "1":
        memory_game = MemoryGame(int(difficulty))
        memory_game.play()
        if memory_game.is_won():
            add_score(int(difficulty))
    elif game == "2":
        guess_game = GuessGame(int(difficulty))
        guess_game.play()
        if guess_game.is_won():
            add_score(int(difficulty))
    elif game == "3":
        currency_game = CurrencyRouletteGame(int(difficulty))
        currency_game.play()
        if currency_game.is_won():
            add_score(int(difficulty))
    while True:
        try:
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() != "yes" or play_again.lower() != "no":
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter 'yes' or 'no'. ")

    if play_again.lower() != "yes":
        print("Hope you had fun! See you next time :)")
        return False
    else:
        print("Let's play again! ")
        load_game()

