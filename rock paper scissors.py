rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


x = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")
import random
list = [rock,paper,scissors]
if x == "0":
  print(rock)
  y = random.choice(list)
  if y == scissors:
    print("Computer chose" + y)
    print("You win")
  elif y == paper:
    print("Computer chose" + y)
    print("Computer wins")
  elif y == rock:
    print("Computer chose" + y)
    print("its a draw")
elif x == "1":
  print(paper)
  y = random.choice(list)
  if y == rock:
    print("Computer chose" + y)
    print("you win")
  elif y == scissors:
    print("Computer chose" + y)
    print("computer wins")
  elif y == paper:
    print("Computer chose" + y)
    print("its a draw")
elif x == "2":
  print(scissors)
  y = random.choice(list)
  if y == rock:
    print("Computer chose" + y)
    print("computer wins")
  elif y == paper:
    print("Computer chose" + y)
    print("you win")
  elif y == scissors:
    print("Computer chose" + y)
    print("its a draw")
input("press enter to exit")
