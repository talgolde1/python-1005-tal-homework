
import os
from Live import load_game, welcome
name = os.getenv(input("Enter your name: "))
print(welcome(name))
load_game()