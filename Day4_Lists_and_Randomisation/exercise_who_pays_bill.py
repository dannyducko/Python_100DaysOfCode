import random
# Split string method - below name variable takes everything from the list, and splits where there is a comma space.
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# len displays the total of items in the list,
name_list_length = len(names)
# below grabs the names list, pulls a random index from 0 -> name_list_length -1.-1 required as len counts from 1 not 0.
print(names[random.randint(0, name_list_length - 1)] + " will pay for the bill")


# solution from course
#Get the total number of items in list.
num_items = len(names)
#Generate random numbers between 0 and the last index.
random_choice = random.randint(0, num_items - 1)
#Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")