#i = 0
numbers = []

def show_number():
    end = int(input('> where do you want to stop: '))
    step = int(input('> enter step: '))

    #i = 0
    #while i < end + 1:
    for i in range(0, end, step):
        print(f"at the top is {i}")
        numbers.append(i)

        i += step

        print(f"at the bottom is {i}")
        print("number now: ", str(numbers).strip('[]'), "\n")          #change list to string and remove   [    ]

show_number()

print("the numbers: ")

for num in numbers:
    print(num)
