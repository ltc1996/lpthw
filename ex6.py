types_of_people = 10
x = f"there are {types_of_people} types of people"

binary = "binary"
do_not = "don't"
y = f"those who know {binary} and those who {do_not}"

print(x)
print(y)

print(f"i said: {x}")
print(f"i also said: {y}")

hilarious = 0 > 1
joke_evaluation = "isn't that joke so funny?{}{}"

print(joke_evaluation.format(hilarious,hilarious))
print("{}".format(hilarious))

l = "this is the left side of..."
r = "a string with a right side."

print(l + r)
