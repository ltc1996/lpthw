ten_thing = "apple orange crows telephone light suger"

print("wait there are not 10 things in that list")
print("let's fix that")

stuff = ten_thing.split(' ')
more_stuff = ["day", "night", "song", "frisbee", "corn", "banana", "girl", "boy"]

#while len(stuff) < 10:
for i in range(len(stuff), 10):
    next_one = more_stuff.pop()
    print("add: ", next_one)
    stuff.append(next_one)
    print(f"there are {len(stuff)} items now")

print("there we go: ", stuff)

print("let's do some thing with stuff")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(stuff)                #last element deleted
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
