from sys import argv

script, filename = argv

print(f"we're going to erase {filename}")
print("if you don't want that, hit CRTL-c (^C)")
print("if you do want that, hit RETURN")

input('?')

print("opening the file ...")
target = open(filename,'w')

print("truncating the file, goodbye")
target.truncate()

print("now i'm going to ask you for three lines")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("i'm going to write these to the file")

target.write(f"{line1} \n{line2} \n{line3}")   # 1 for 6
target.write(line1 + "\n" + line2 + "\n" +line3)    #another way
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

print("and finally, we close it")
target.close()

txt = open(filename)                         #print this file
print(txt.read())
