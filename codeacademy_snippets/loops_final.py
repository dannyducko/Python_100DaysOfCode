# Your code below:
single_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares = []
cubes = [cube**3 for cube in single_digits] # comprehension lists. cube the number in single_digits

for digit in single_digits:
  squares.append(digit * digit)
  print(digit)

print(squares)
print(cubes)