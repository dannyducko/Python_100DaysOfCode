# Leap year method;
# This is how you work out whether if a particular year is a leap year.
# on every year that is evenly divisible by 4
#   **except** every year that is evenly divisible by 100
#       **unless** the year is also evenly divisible by 400

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

year_divisible_4 = year % 4
year_divisible_100 = year % 100
year_divisible_400 = year % 400

if year_divisible_4 == 0:
    if year_divisible_100 == 0:
        if year_divisible_400 == 0:
            print("Leap Year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")