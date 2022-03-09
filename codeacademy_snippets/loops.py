# for <temporary variable> in <list of length 6>:
#   print("Learning Loops!")

###########################
promise = "I will finish the python loops module!"

for p in range(5):
    print(promise)

###########################
# while loops
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

# Your code below:
length = len(python_topics)
index = 0

# while index is less than length;
# while loops check to see if a statement is true. if true, continue.
while index < length:
    print(f"I am learning about {python_topics[index]}")
    index += 1

#######################
# Breaking Loops
dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
    print(dog_breed)
    if dog_breed == dog_breed_I_want:
        print("They have the dog I want!")
        break

######################
# Continue Loops
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
    if age >= 21:
        print(age)
        continue

######################
# Nested Loops
# extract and add the amount of sales of certain ice cream per store.
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
    print(location)
    for item in location:
        scoops_sold += item

print(scoops_sold)

#####################
# Loops - List comprehensions
# Creating elegant code
# We can use normal 'for loops', but we can also make them elegant.
grades = [90, 88, 62, 76, 74, 89, 48, 57]

scaled_grades = [score + 10 for score in grades]
print(scaled_grades)

####################
# Loops - List comprehensions: Conditionals
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [h for h in heights if h > 161]
print(can_ride_coaster)


