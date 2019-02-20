cars = 100#tatal cars=100
space_in_a_car = 4#each car can carry 4 passangers
drivers = 30#wo got 30 drivers
passangers = 90#we have 90 passangers needed tp transport

cars_not_driven=cars - drivers
car_driven = drivers
carpool_capacity = car_driven * space_in_a_car
average_passangers_per_car = passangers / car_driven

print("there are",cars,"cars available")
print("there are only",drivers,"drivers available")
print("there will be",cars_not_driven,"empty cars today")
print("we can transport",carpool_capacity,"people today")
print("we have",passangers,"to carpool today")
print("we need to put about",average_passangers_per_car,"passangers in each car")
#using format string to rewrite the last sentence
print(f"we need to put about {average_passangers_per_car} passangers in each car")
