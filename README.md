# World of Games Project

Welcome to the World of Games (WoG) project. This repository hosts an interactive suite of text-based games developed in Python, accompanied by a robust Flask-based web application for managing user scores. This endeavor is fortified by an integrated Jenkins pipeline for continuous integration and rigorous testing.

## Getting Started

Ensure you have the following prerequisites in place before commencing:

- Python 3.9
- Docker
- Docker Compose
- Jenkins
- Selenium

## Usage

### Live.py

This module warmly welcomes users to the World of Games and facilitates the launch of various games based on user inputs.

- **`welcome(name)`**: This function extends a personalized welcome to users, using their name.

- **`load_game()`**: This function guides users in selecting a game and difficulty level, subsequently initiating the chosen game with the designated difficulty.

### GuessGame.py

Can you remember a sequence of numbers displayed for a brief moment? In the Memory Game, a sequence of random numbers will appear, and you must recall and input the same sequence afterward. Challenge your memory and observation skills!

### MemoryGame.py

This module embodies the Memory Game, where users strive to recollect a sequence of numbers.

### CurrencyRouletteGame.py

Test your currency exchange knowledge with the Currency Roulette game. You'll be provided with a random amount of USD, and your task is to guess its equivalent value in ILS (Israeli Shekels), using the current exchange rate. The difficulty level will influence the range of acceptable values.

### Utils.py

This utility module provides a range of general-purpose functions.

- **`Screen_cleaner`**: A function designed to clear the screen.

### Score.py

As you play and win games, your accumulated winnings will be recorded. Each game's score is based on the difficulty level and calculated as follows:

```
POINTS_OF_WINNING = (DIFFICULTY X 3) + 5
```

- **`add_score(difficulty)`**: Incorporates the user's score into the score file, based on the game's difficulty.

### MainScores.py

This module utilizes Flask to serve user scores over HTTP in a web page that will display your current score in an easy-to-read format.


### e2e.py

This module contains functions for comprehensive end-to-end testing of the web service.

- **`test_scores_service(app_url)`**: Delivers thorough testing of the web service by verifying the displayed score as a number within the range of 1 to 1000.

- **`main_function(app_url)`**: Executes the testing function, rendering an exit code.

### Dockerfile

The Dockerfile encapsulates the Flask project and establishes the required environment.

### docker-compose.yml

Effectively manage the application through Docker Compose.

### Jenkinsfile

Defines the Jenkins pipeline stages:

1. **Checkout**: Retrieves the repository.
2. **Build**: Constructs the Docker image.
3. **Run**: Executes the application within a Docker container.
4. **Test**: Employs the e2e.py script to rigorously test the application.
5. **Finalize**: Undertakes cleanup and propels the image to DockerHub.

## Running the Application

1. Clone this repository.
2. Navigate to the project root directory.
3. Initiate the application build and launch via Docker Compose:

   ```bash
   docker-compose up --build
   ```

## Jenkins Pipeline

To execute the Jenkins pipeline:

1. Set up Jenkins.
2. Establish a new pipeline job, configuring it to use the Jenkinsfile within the repository.
3. Trigger the pipeline, which encompasses various stages, including comprehensive Selenium-based testing of the web service.
4. Access the Scores.txt live web service at http://localhost:5000.

## Contributions

This repository is currently not accepting direct contributions, as it serves as a showcase for the author's Python coursework. However, if you discover any issues or have suggestions for improvements, please feel free to raise an issue or get in touch via email talgolde1@gmail.com.

We hope you enjoy the "World of Games" and have a fantastic gaming experience! Thank you for visiting my repository.
## License

This project operates under the MIT License. Please refer to the [LICENSE](LICENSE) file for detailed terms.
