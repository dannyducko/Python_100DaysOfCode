print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
bill = 0

# below will check to see if your height is equal to or above 120, and a nested if statement.
if height >= 120:
    print("You are clear to ride the rollercoaster")
    age = int(input("What is your age?"))
    if age < 12:
        bill += 5
        print("Child tickets are $5")
    elif age <= 18:
        bill += 7
        print("Youth tickets are $7")
    else:
        bill += 12
        print("Adult tickets are $12")

    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3

    print(f"Your total is ${bill}.")

else:
    print("Sorry, you cannot ride today.")