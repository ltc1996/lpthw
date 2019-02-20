def add(a, b):
    print(f"adding {a} and {b}")
    return a + b

def subtract(a, b):
    print(f"sub {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"multiply {a} * {b}")
    return a * b

def divide(a, b):
    print(f"divide {a} / {b}")
    return a / b

print("let's do some math with these functions")

age = add(30, 5)
height = subtract(78, 9)
weight = multiply(4, 20)
iq = divide(6, 0.2)

print(f"age: {age},height: {height},weight: {weight}, iq: {iq}")

print("here's a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("that becomes", what, "\ncan you do it by your hand?")
