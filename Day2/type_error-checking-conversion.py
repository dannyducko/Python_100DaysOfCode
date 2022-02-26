# len(4837) - would output an error advising its a TypeError, as its a type of 'int'.

num_char = len(input("What is your name?"))
# print("Your name has " + num_char + "characters.")   - This will error as a type error, due to num_char outputting
# as an int. You can tell its an int by running the below; Typecheck function.
# print(type(num_char))

# We can also do type conversion, or type casting.
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

# below will print 175.5
print(70 + float("100.5"))

# below will print 70100
print(str(70) + str(100))


