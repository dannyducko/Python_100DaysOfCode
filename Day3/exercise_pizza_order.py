# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
small_pizza = 15
medium_pizza = 20
large_pizza = 25

add_pepperoni_small = 2
add_pepperoni_med_large = 3
add_cheese = 1

bill = 0


if size == "S":
    bill += small_pizza
    if add_pepperoni == "Y":
        bill += add_pepperoni_small
    if extra_cheese == "Y":
        bill += add_cheese
    print(f"Your final bill is: ${bill}")
elif size == "M":
    bill += medium_pizza
    if add_pepperoni == "Y":
        bill += add_pepperoni_med_large
    if extra_cheese == "Y":
        bill += add_cheese
    print(f"Your final bill is: ${bill}")
elif size == "L":
    bill += large_pizza
    if add_pepperoni == "Y":
        bill += add_pepperoni_med_large
    if extra_cheese == "Y":
        bill += add_cheese
    print(f"Your final bill is: ${bill}")
else:
    print("Your order failed! Please try again.")

# Better solution below
# bill = 0
#
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25
#
# if add_pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill is: ${bill}.")