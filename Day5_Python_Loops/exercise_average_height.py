# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
# do not use len or sum. meant to use loops.
print("Here are the entries you submitted " + str(student_heights))

total_height = 0
height_count = 0

# each time it runs through a new entry in the student_heights list, + to the total of total height var
# and + 1 each time to the height_count.
for height in student_heights:
    total_height += height
    height_count += 1

average_height = round(total_height / height_count)
# print(average_height)

print(f"The average height between all entries is; {average_height}")

