people = 30
cars = 40
trunks = 15

if cars > people:
    print("we should take the cars")
elif cars < people:
    print("we should not take the cars")
else:
    print("we can't decide")

if trunks > cars:
    print("that's too many trunks")
elif trunks > cars:
    print("maybe we could take the trunks")
else:
    print("we still can't decide")

if people > trunks:
    print("allright, let's just take the trunks")
else:
    print("fine, let's stay home then")
