welcome = input("Whats your name?")


def greet(name): # the data entered here is called a "parameter"
    print(f"Hi {name}")
    print(f"Goodbye {name}")
    print(f"Didn't I say goodbye already {name}?")


greet(welcome) # the data entered here is called an argument.
