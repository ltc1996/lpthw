def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2 : {arg2}")

def print_two_agian(arg1, arg2):
    print(f"arg1: {arg1}, arg2 : {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("i've got nothing")

print_two("lee", "tiancheng")
print_two_agian("lee", "tiancheng")
print_one("so cool")
print_none()
