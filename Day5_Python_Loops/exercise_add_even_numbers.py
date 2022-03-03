# print the total of all even numbers between 1 - 100

total = 0

for numbers in range(2, 101, 2):
    total += numbers

print(total)

# another solution
total2 = 0
for numbers in range(1, 101):
    if numbers % 2 == 0:
        total2 += numbers

print(total2)
