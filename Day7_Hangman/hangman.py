import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = []
word_length = len(chosen_word)

print(chosen_word)

for _ in range(word_length):
    display += "_"

#guess = input("Guess a letter!\n > ").lower()

while display.count("_") > 0:
    #print(display.count("_"))
    guess = input("Guess a letter!\n > ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(*display)

print("You won")





