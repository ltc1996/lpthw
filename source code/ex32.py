the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'orange', 'pear', 'apricot']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print(f"this is count {number}")

for fruit in fruits:
    print(f"a fruit of type: {fruit}")


for i in change:
    print("i got {}".format(i))

#start with a empty list
element = []

for i in range(0, 6, 2):                #step = 2
    print(f"add {i} to the list")
    element.append(i)


for i in element:
    print(f"element was: {i}")
