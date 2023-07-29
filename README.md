# World of Games

Welcome to the "World of Games" repository! This project consists of a collection of fun and interactive Python games that you can play. Each game challenges your skills and offers different levels of difficulty for an exciting experience. This repository also includes utilities to manage scores and display your current score on a web page.

## Files and Functions Overview

### Live.py

This file contains functions to welcome users and prompt them to choose and play a game.

#### `welcome(name)`

- This function takes a person's name as input and returns a welcome message.
- It will display: "Hello \<name\> and welcome to the World of Games (WoG). Here you can find many cool games to play."

#### `load_game()`

- This function displays the available games and their corresponding numbers.
- The user can choose a game by entering the game number (1, 2, or 3) and the desired difficulty level (1 to 5).
- The chosen game will then be started with the selected difficulty level.

### MainGame.py

This file acts as the entry point for the games and calls functions from Live.py.

### GuessGame.py

This game is all about guessing a random number chosen by the computer.

#### Properties:

- `Difficulty`: The level of difficulty for the game.

#### Methods:

1. `generate_number`: Generates a random number between 1 to the difficulty.
2. `get_guess_from_user`: Prompts the user for a number between 1 to the difficulty and returns the user's input.
3. `compare_results`: Compares the secret generated number with the user's guess and returns True if they match, False otherwise.
4. `play`: Calls the above functions to play the game and returns True if the user wins, False if they lose.

### MemoryGame.py

In this game, the user must remember a sequence of numbers displayed briefly and input the same sequence afterward.

#### Properties:

- `Difficulty`: The level of difficulty for the game.

#### Methods:

1. `generate_sequence`: Generates a list of random numbers between 1 to 101 with a length equal to the difficulty.
2. `get_list_from_user`: Prompts the user to enter a list of numbers with a length equal to the difficulty and returns the user's input.
3. `is_list_equal`: Compares two lists and returns True if they are equal, False otherwise.
4. `play`: Calls the above functions to play the game and returns True if the user wins, False if they lose.

### CurrencyRouletteGame.py

This game challenges the user to guess the value of a random amount of USD in ILS, using the current exchange rate.

#### Properties:

- `Difficulty`: The level of difficulty for the game.

#### Methods:

1. `get_money_interval`: Gets the current currency rate from USD to ILS and generates an interval around the value, based on the difficulty.
2. `get_guess_from_user`: Prompts the user to enter their guess of the USD value converted to ILS for a given amount of USD.
3. `play`: Calls the above functions to play the game and returns True if the user wins, False if they lose.

### Utils.py

This file contains general information and utility functions used across the games.

- `SCORES_FILE_NAME`: A string representing the filename for storing scores. By default, it is set to "Scores.txt".
- `BAD_RETURN_CODE`: A number representing a bad return code for a function.
- `Screen_cleaner`: A function to clear the screen (useful before starting a new game).

### Score.py

This package manages the scores file. The scores file keeps track of the user's accumulated winnings.

- `POINTS_OF_WINNING`: The number of points awarded for winning a game, calculated based on the difficulty.
- `add_score(difficulty)`: A function to update the current score in the scores file when the user wins a game.

### MainScores.py

This file serves the user's current score in the "Scores.txt" file over HTTP with HTML using Flask.

- `score_server()`: This function reads the score from the scores file and returns an HTML page displaying the current score. In case of an error, it displays an error message in red.

## Getting Started

To run the games, simply execute `MainGame.py` using Python. The program will prompt you to choose a game and difficulty level. Follow the on-screen instructions to play and have fun!

Feel free to explore the code in each game file to understand how the games work. Additionally, you can check the scores by accessing the web page served by `MainScores.py`.

Have fun and enjoy the "World of Games"!
