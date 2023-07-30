
import os

score_file = "Scores.txt"
return_code = -1


def screen_clean():
    os.system('cls' if os.name == 'nt' else 'clear')
