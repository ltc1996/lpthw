person = "{} {} {}"
print("how old were you in 2000?",end = ' ')
age = int(input())

print("how tall are you?",end = ' ')
height = input()

print("how much are you weigh?",end = ' ')
weight = input()

#print(f"so you are {age} years old, {height} cm tall and {weight} kg heavy")
print("so you are now {} years old, {} cm tall and {} kg heavy".format(18 + age,height,weight))
print(person.format(age,height,weight))
