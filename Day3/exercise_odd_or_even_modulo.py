# exercise to determine if the number input by the user is even or odd. Using modulo. Modulo is a math operation that
# finds the remainder when one integer is divided by another. In writing, it is frequently abbreviated as mod,
# or represented by the symbol %. Anything with the remainder 1, when finding the modulo of number % 2,
# shows the number is an odd number


# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
number_modulo_conversion = number % 2

if number_modulo_conversion == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")