
winnig_points = lambda difficulty: (difficulty * 3) + 5


def add_score(difficulty):
    try:
        with open("Scores.txt", "r+") as file:
            current_score = int(file.read())
            new_score = current_score + winnig_points(difficulty)
            file.seek(0)
            file.write(str(new_score))
    except IOError:
        with open("Scores.txt", "w") as file:
            new_score = winnig_points(difficulty)
            file.write(str(new_score))
