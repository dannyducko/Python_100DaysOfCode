# Functions with more than 1 input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"I see you're going to {location} today, let me help with that.")


# positional arguments
greet_with("Dan", "France")

# keyword arguments - specifying, in any location, what the input/ variable will be.
greet_with(location="France", name="Dan")
