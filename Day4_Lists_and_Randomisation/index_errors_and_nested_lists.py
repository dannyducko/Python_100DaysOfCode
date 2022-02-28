states_of_america = ["Delaware", "Pennsylvania", "Texas", "Nevada", "Washington"]

# Below will cause an index error: index out of range. Item index does not exist/ out of scope
# print(states_of_america[5])

# Below will print the last member of the list, but will require a -1 as the len counts from 1, not 0.
num_of_states = len(states_of_america)
print(states_of_america[num_of_states - 1])

fruits = ["Apples", "Grapes", "Peaches", "Cherries", "Pears", "Nectarines", "Strawberries"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# nests both lists into a list called dirty_dozen.
dirty_dozen = [fruits, vegetables]
# to call the last item in the last list in the nested list, you will need to do similar to below.
print(dirty_dozen[-1][-1])

