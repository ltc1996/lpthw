print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()                                    #add this line
print("How much do you weigh?", end=' ')            #add  )
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

from sys import argv                                #  add this line
script, filename = argv

txt = open(filename)                                #correct  filename

print("Here's your file {filename}:")
print(txt.read())                                   #txt

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())                             #change  .  to  _


print('Let\'s practice everything.')                #add \
print("""You\'d need to know \'bout escapes
      with \\ that do \n newlines and \t tabs.""")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")                         #add   "
print(poem)
print("--------------")                         #add   "


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")           #add   )

def secret_formula(started):                           #add :
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100                                #add /
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)      #add crates

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)              #add   _
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))



people = 20
cats = 30                               #correct   cats
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")    #add  (   )

if people > cats:                                   #  >
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:                                   #add  :
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:                          #add   :
    print("People are less than or equal to dogs.")


if people == dogs:                           #add ==
    print("People are dogs.")
