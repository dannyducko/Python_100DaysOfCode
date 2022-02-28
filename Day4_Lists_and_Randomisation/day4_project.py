import random

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

#Write your code below this line 👇

# create game options in list format, attached to the variables above.
game_options = [rock, paper, scissors]
# create a random number between 0 and 2, used to select the image and list index later.
computer_choice = random.randint(0, 2)
# image to be pulled on computer choice and printed.
computer_choice_image = game_options[computer_choice]

# Request user input as to their choice.
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors.\n"))

# combine both choices into a str format to use for win conditions
both_choices_combined = str(user_input) + str(computer_choice)
# win conditions would be; 02, 10, 21
# draw conditions would be; 00, 11, 22

# print your choice and computers choice.
print(f"\n You chose: \n {game_options[user_input]}")
print(f"Computer chose: \n {computer_choice_image}")

# if statement. if the win conditions are met, which are 02, 10 or 21, print you win.
# draw conditions drawn up in elif and loss statement doesn't matter as caught in else statement.
if both_choices_combined == "02" or both_choices_combined == "10" or both_choices_combined == "21":
    print("You Win!!")
elif both_choices_combined == "00" or both_choices_combined == "11" or both_choices_combined == "22":
    print("You Draw!!")
else:
    print("You Lose!!")


# course solution
# game_images = [rock, paper, scissors]
#
# user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# print(game_images[user_choice])
#
# computer_choice = random.randint(0, 2)
# print("Computer chose:")
# print(game_images[computer_choice])
#
# if user_choice >= 3 or user_choice < 0:
#   print("You typed an invalid number, you lose!")
# elif user_choice == 0 and computer_choice == 2:
#   print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#   print("You lose")
# elif computer_choice > user_choice:
#   print("You lose")
# elif user_choice > computer_choice:
#   print("You win!")
# elif computer_choice == user_choice:
#   print("It's a draw")

