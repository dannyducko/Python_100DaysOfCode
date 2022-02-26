# print(8 / 3) will give us 2.666666
# print(int(8 / 3)) will give us 2, but its not rounded up to the correct number.

# the below will round the number.
print(round(8 / 3))

# the below will round to 2 points of precision/ 2 points after the decimal point.
print(round(8 / 3, 2))

# Floor division - two // will turn the number into a int/ whole number.
print(8 // 3)

# We can continue carrying out calculations on variables;
result = 4 / 2
result /= 2
print(result)

# example manipulating a variable by adding to it each time. example; a score
score = 0
# user scores a point
score += 1
print(score)

height = 1.8
isWinning = True

# f strings
# if we wanted to convert a int inline like below, we'd declare the variable as a str/ int to convert.
print("Your score is " + str(score))
# This can be a pain if we have multiple data types to print etc. A more convenient way is below;
print(f"Your score is {score}, the tallest member of the team is {height} and you are winning is {isWinning}.")
