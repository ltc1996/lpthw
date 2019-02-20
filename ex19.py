def cheese_and_crackers(cheese_count, boxes_of_crakers):
    print(f"you have {cheese_count} cheesees")
    print(f"you have {boxes_of_crakers} boxes of crackers")
    print("that's enough for party")
    print("get a blacket\n")

print("we can just give the function numbers directly:")        #give numbers directly
cheese_and_crackers(20,30)

print("or, we can use variables from our script:")              #give numbers via variables
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("we can get numbers by typing yourself")                  #give numbers by typing
amount_of_cheese = int(input("the amount of cheese:"))          #transform string to number
amount_of_crackers = int(input("the amount of crack ers:"))
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("we can even do math inside too:")                        #calculate with numbers
cheese_and_crackers(10 + 20, 5 + 6)

print("and we can combine the two, variables and math:")        #calculate with variables
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
