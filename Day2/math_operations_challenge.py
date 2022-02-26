# BMI Calculator. The calculation for BMI is BMI = weight(kg) / height to the power of 2.
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# float and weight to be changed into floats as it will otherwise error. Instead of power, could just height*height
bmi = float(weight) / float(height) ** 2
# when printing the bmi value, convert it into an integer otherwise you'll end up with a decimal number.
print(int(bmi))