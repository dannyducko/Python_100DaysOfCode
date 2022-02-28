states_of_america = ["Delaware", "Pennsylvania", "Texas", "Nevada", "Washington"]

# positive index (indices) 0, 1, 2, 3 etc
print(states_of_america[0])
print(states_of_america[1])

# negative index -1, -2, -3, -4 (-1 will print Washington. -2 will print Nevada, etc)
print(states_of_america[-1])

# edit a list member
states_of_america[1] = "Pencilvania"
print(states_of_america[1])

# Append to the list. and print the last index in the list, which will now be new york due to the append.
states_of_america.append("New York")
print(states_of_america[-1])

# extend the list by appending multiple indices/ values.
states_of_america.extend(["Dakota", "Florida"])
print(states_of_america[-1] + " " + states_of_america[-2])


