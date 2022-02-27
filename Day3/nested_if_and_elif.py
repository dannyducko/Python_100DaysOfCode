print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

# below will check to see if your height is equal to or above 120, and a nested if statement.
if height >= 120:
    print("You are clear to ride the rollercoaster")
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry, you cannot ride today.")

# elifs
# if condition 1:
#   do a
# elif condition 2:
#   do b
# else:
#   do this