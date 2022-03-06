# for <temporary variable> in <list of length 6>:
#   print("Learning Loops!")

###########################
promise = "I will finish the python loops module!"

for p in range(5):
  print(promise)

###########################
# while loops
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 
length = len(python_topics)
index = 0

# while index is less than length;
while index < length:
  print(f"I am learning about {python_topics[index]}")
  index += 1