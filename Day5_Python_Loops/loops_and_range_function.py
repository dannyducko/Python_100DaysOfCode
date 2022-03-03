# for loop with range.

# below will print 1 - 9. Need to set to 11 to actually print 1 through to and including 10.
# for number in range(1, 10):
#     print(number)

for number in range(1, 11):
    print(number)

# we can also 'step' through the range in increments of x - x in this case being 3
for number in range(1, 11, 3):
    print(number)


# sum of every number from 1 > 100
total = 0
for number in range(1, 101):
    total += number

print(total)
