from art import logo
import random
print(logo)
print("Welcome to the Number Guessing Game!")
print("Im thinking of a number between 1 and 100.")
random_number = random.randint(1, 100)

def easy_mode():
  number_of_turns = 10
  guess = ""
  while number_of_turns != 0 and guess != random_number:
    print(f"you have {number_of_turns} attempts remaining to guess the number")
    guess = int(input("make a guess: "))
    if guess > random_number:
      print("Too high")
    elif guess < random_number:
      print("Too low")
    elif guess == random_number:
      print(f"You got it! The answer was {random_number}")
    number_of_turns -= 1

def hard_mode():
  number_of_turns = 5
  guess = ""
  while number_of_turns != 0 and guess != random_number:
    print(f"you have {number_of_turns} attempts remaining to guess the number")
    guess = int(input("make a guess: "))
    if guess > random_number:
      print("Too high")
    elif guess < random_number:
      print("Too low")
    elif guess == random_number:
      print(f"You got it! The answer was {random_number}")
    number_of_turns -= 1

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
  easy_mode()
else:
  hard_mode()

