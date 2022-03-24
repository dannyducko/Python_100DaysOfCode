# insert item into an index point
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

# Your code below:
front_display_list.insert(0, "Pineapple")
print(front_display_list)


#############
# .pop - removing an item and can be re-used in another variable
data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# Your code below:
# below will remove last entry, and under that will remove the item at the 3rd index.
data_science_topics.pop()
data_science_topics.pop(3)

print(data_science_topics)

#############
# instead of creating a list with 0, 1, 2, etc. we can use the range function.
# Your code below:

number_list = range(0, 9)
print(list(number_list))

zero_to_seven = range(0, 8)
print(list(zero_to_seven))

# slicing lists
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:2] # will print shirt shirt

# Your code below:
print(beginning)

middle = suitcase[2:4]

# more slicing
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Your code below:
last_two_elements = suitcase[-2:]
print(last_two_elements)

slice_off_last_three = suitcase[:-3]
# could also be [3:]
print(slice_off_last_three)

######### Counting in a list
votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Your code below:
jake_votes = votes.count("Jake")
print(jake_votes)

######### Sorting lists
# .sort() does not generate a new list, so cant be used in variables.
# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
addresses.sort()
print(addresses)

# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()


# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
cities.sort(reverse=True)
print(cities)

######### Sorting lists 2
# sorted() does create a new list and called by sorted(name_of_list)
games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

# Your code below:
games_sorted = sorted(games)
print(games)
print(games_sorted)