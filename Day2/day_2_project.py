# Tip Calculator
print("Welcome to the tip calculator.")
# below will prompt the user for input on the total bill.
total_bill = float(input("What was the total bill? $"))
# below will capture user input on what percentage tip they would like to give, in integer format.
tip_amount = int(input("What percentage tip would you like to give? 10, 12 or 15?"))
# below will capture input on how many people will split the bill in an integer format.
split_between = int(input("How many people will split the total bill?"))

# convert tip_amount to a workable value (tip_percent) in terms of percent
tip_percent = tip_amount / 100
# calculate percent of bill then add to the total bill and round to 2 places after decimal point.
bill_with_tip = round(tip_percent * total_bill + total_bill, 2)
# could present both lines above as a single line such as;
# bill_with_tip = round(tip_amount / 100 * bill + bill)

# split the new total between the amount of people the user input
amount_per_person = bill_with_tip / split_between

# print the amount owed per person.
print(f"Each person should pay: ${amount_per_person}")


