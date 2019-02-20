formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(True,False,False,True))
print(formatter.format(formatter,formatter,formatter,formatter))
print("he will knock {} times".format(2 + 2))
print(formatter.format(
    "try your",
    "own text here",
    "maybe a poem",
    "or a song about it"
))
