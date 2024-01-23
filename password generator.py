#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

letter_list = []
for x in range(nr_letters):
  n = random.choice(letters)
  letter_list.append(n)

symbol_list = []

for x in range(nr_symbols):
  n = random.choice(symbols)
  symbol_list.append(n)

number_list = []

for x in range(nr_numbers):
  n = random.choice(numbers)
  number_list.append(n)

number_list 

pass1 = "".join(letter_list)
pass2 = "".join(number_list)
pass3 = "".join(symbol_list)

password = pass1 + pass2 + pass3

new_password = []
for char in password:
  new_password.append(char)


final_password = "".join(new_password)
print(final_password)
input("Press Enter to exit.")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

