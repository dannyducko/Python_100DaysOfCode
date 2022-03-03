# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
# do not use the max function with the list. 
highest_score = 0

for score in student_scores:
    if int(score) > highest_score:
        highest_score = int(score)

print(f"The highest score in the class is: {str(highest_score)}")

