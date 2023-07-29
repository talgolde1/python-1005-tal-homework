# World of Games

Welcome to the "World of Games" repository! This project offers an engaging collection of Python games that will challenge your skills and provide hours of entertainment. Each game comes with different difficulty levels to cater to players of all experience levels.

## Getting Started

To get started with the games, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/talgolde1/python-1005-tal-homework.git
   cd python-1005-tal-homework
   ```

2. Run the MainGame.py script:

   ```
   python MainGame.py
   ```

   The program will prompt you to choose a game and set the desired difficulty level. Simply follow the on-screen instructions to start playing.

## Games Overview

### Guess Game

In this game, you need to guess a randomly chosen number between 1 and the selected difficulty level. Put your intuition to the test and see if you can guess correctly!

### Memory Game

Can you remember a sequence of numbers displayed for a brief moment? In the Memory Game, a sequence of random numbers will appear, and you must recall and input the same sequence afterward. Challenge your memory and observation skills!

### Currency Roulette

Test your currency exchange knowledge with the Currency Roulette game. You'll be provided with a random amount of USD, and your task is to guess its equivalent value in ILS (Israeli Shekels), using the current exchange rate. The difficulty level will influence the range of acceptable values.

## Scores Management

As you play and win games, your accumulated winnings will be recorded. Each game's score is based on the difficulty level and calculated as follows:

```
POINTS_OF_WINNING = (DIFFICULTY X 3) + 5
```

The scores are saved in the "Scores.txt" file. You can check your current score by accessing the web page served by `MainScores.py`:

```
python MainScores.py
```

The web page will display your current score in an easy-to-read format.

## Contribution

This repository is currently not accepting direct contributions, as it serves as a showcase for the author's Python coursework. However, if you discover any issues or have suggestions for improvements, please feel free to raise an issue or get in touch via email talgolde1@gmail.com.

We hope you enjoy the "World of Games" and have a fantastic gaming experience! Thanks you for visiting my repository.
