# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
ez_pass = ""
letter_count = 0
symbol_count = 0
number_count = 0

for random_letter in letters:
    if letter_count != nr_letters:
        letter_count += 1
        ez_pass = str(ez_pass) + letters[random.randint(0, len(letters) - 1)]

for random_symbol in symbols:
    if symbol_count != nr_symbols:
        symbol_count += 1
        ez_pass = str(ez_pass) + symbols[random.randint(0, len(symbols) - 1)]

for random_number in numbers:
    if number_count != nr_numbers:
        number_count += 1
        ez_pass = str(ez_pass) + numbers[random.randint(0, len(numbers) - 1)]

print(ez_pass)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

for random_letter in letters:
    if letter_count != nr_letters:
        letter_count += 1
        ez_pass = str(ez_pass) + letters[random.randint(0, len(letters) - 1)]
    if symbol_count != nr_symbols:
        symbol_count += 1
        ez_pass = str(ez_pass) + symbols[random.randint(0, len(symbols) - 1)]
    if number_count != nr_numbers:
        number_count += 1
        ez_pass = str(ez_pass) + numbers[random.randint(0, len(numbers) - 1)]

print(ez_pass)

## solution from course
#easy
password = ""
for char in range(nr_letters):
    password += random.choice(letters)

for char in range(nr_symbols):
    password += random.choice(symbols)

for char in range(nr_numbers):
    password += random.choice(numbers)

print(password)


# hard
password_list = []
for char in range(nr_letters):
    password_list += random.choice(letters)
    # or use .append instead of += password_list.append(random.choice(letters))

for char in range(nr_symbols):
    password_list += random.choice(symbols)

for char in range(nr_numbers):
    password_list += random.choice(numbers)

pw = ""

random.shuffle(password_list)
for char in password_list:
    pw += char

print(pw)
