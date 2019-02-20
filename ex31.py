print("""you enter a dark room with two doors
do you go through door #1 ot door #2?""")

prompt = '> '

door = input(prompt)

if door == '1':
    print("there's a giant bear here eating a cheese cake")
    print("what do you do?")
    print("1.\ttake his cake")
    print("2.\tscream at the bear")

    bear = input(prompt)

    if bear == '1':
        print("the bear eats your face off\ngood job")
    elif bear == '2':
        print("the bear eats your legs off\ngood job")
    else:
        print(f"{bear} is an excellent choice")
        print("bear runs away")

elif door == '2':
    print("you stare into the endless abyss at Cthulhu's retina")
    print("1.\tblueberries")
    print("2.\tyellow jacket clothespins")
    print("3.\tunderstanding revolvers yelling melodies")

    insanity = input(prompt)

    if insanity == '1' or insanity == '2':
        print("your body survives powered by a mind of jello")
        print("good job")
    else:
        print("the insanity rots your eyes into a pool of muck")
        print("good job")

else:
        print("you stumble around and fail on a knife and die\ngood job")
