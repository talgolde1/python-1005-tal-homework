
import os


winnig_points = lambda difficulty: (difficulty * 3) + 5


def add_score(difficulty):
    try:
        with open(os.path.join("Scores", "Scores.txt"), "r") as file:
            current_score = int(file.read())
            new_score = current_score + winnig_points(difficulty)
            file.seek(0)
            file.write(int(new_score))
    except IOError:
        with open(os.path.join("Scores", "Scores.txt"), "w") as file:
            new_score = winnig_points(difficulty)
            file.write(int(new_score))
