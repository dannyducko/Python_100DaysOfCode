# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# below is joining the 2 names together and setting them to lower case, so we have the ability to count properly.
name_joined = name1.lower() + name2.lower()
# below counts characters individually against true and love.
count_true = name_joined.count("t") + name_joined.count("r") + name_joined.count("u") + name_joined.count("e")
count_love = name_joined.count("l") + name_joined.count("o") + name_joined.count("v") + name_joined.count("e")
# below concatenates the 2 numbers as a string, to avoid mathematical addition.
count_true_love = str(count_true) + str(count_love)
# or you could wrap the 2 strings in an int
# count_true_love = int(str(count_true) + str(count_love))

if int(count_true_love) < 10 or int(count_true_love) > 90:
    print(f"Your score is {count_true_love}, you go together like coke and mentos.")
elif int(count_true_love) >= 40 and int(count_true_love) <= 50:
    print(f"Your score is {count_true_love}, you are alright together.")
else:
    print(f"Your score is {count_true_love}")
