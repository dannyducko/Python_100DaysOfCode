print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

the_start = input("You're at a crossroad. Where do you want to go? Type left or right \n").lower()

if the_start == "left":
    lake_input = input(
        "You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type "
        "'swim'' to swim across. \n").lower()
    if lake_input == "wait":
        pick_door = input("Your wait paid off. A boat arrived and takes you across the lake. You arrive at the "
                          "island unharmed. There is a house with 3 doors. One red, one yellow and one blue. "
                          "Which colour do you choose?\n").lower()
        if pick_door == "yellow":
            print("You found the treasure! You Win!")
        elif pick_door == "red":
            print("It's a room full of fire. Game Over.")
        elif pick_door == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")

    elif lake_input == "swim":
        print("You begin your way across the lake, you have plenty of energy and actually starting to enjoy the swim! "
              "But you notice a shark (in a lake?) and it's aware of your presence. You're in the middle of the lake, "
              "you can't really do much really. You die... \nGame Over!")

elif the_start == "right":
    print("You cautiously make your way through the woods, where you come across a raging bear. You do your best to "
          "run back the way you came from but the bear outpaces you, and you eventually meet your doom. \nGame Over!")
else:
    print("Game Over.")
