from sys import argv

script, filename = argv

txt = open(filename)

print(f"here is your filename:{filename}")
print(txt.read())
txt.close()             #close file

print("type your filename again:")
file_again = input('> ')

txt_again =open(file_again)
print(txt_again.read())
txt_again.close()       #close file
