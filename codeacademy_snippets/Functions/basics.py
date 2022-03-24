# Your code below:
def directions_to_timesSq():
    print("Walk 4 mins to 34th St Herald Square train station")
    print("Take the Northbound N, Q, R, or W train 1 stop")
    print("Get off the Times Square 42nd Street stop")


directions_to_timesSq()


##### Parameters and arguments
# setting the parameter to location, where the location can be used when calling the func.
def generate_trip_instructions(location):
    print("Looks like you are planning a trip to visit " + location)
    print("You can use the public subway system to get to " + location)


generate_trip_instructions("Grand Central Station")


###### Multiple parameters
# multiple para called, in order, and the values defined at the bottom when calling func.
# Below is a "positional argument". plane is in the first position, etc.
def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
    car_rental_total = car_rental_rate * trip_time
    hotel_total = hotel_rate * trip_time - 10
    print("Your total is: " + (car_rental_total + hotel_total + plane_ticket_price))


calculate_expenses(200, 100, 100, 5)

#######################################
###### default parameters
## below will set discount to a "default parameter"
# def calculate_taxi_price(miles_to_travel, rate, discount = 10):
#   print(miles_to_travel * rate - discount )

##### Keyword arguments
## explicitly refer to what each argument is assigned to in the functions call.
# calculate_taxi_price(rate=0.5, discount=10, miles_to_travel=100)
#######################################


###### Types of arguments
def trip_planner(first_destination, second_destination, final_destination = "Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)

#positional arguments. set to the order defined in the function argument.
trip_planner("Denmark", "France", "Germany")

#keyword arguments, can be any order, but called in order define by original statement.
trip_planner(first_destination = "Iceland", final_destination = "Germany", second_destination = "India")

#Default arguments. will print our entries, and then the default.
trip_planner(first_destination = "Brooklyn", second_destination = "Queens")
