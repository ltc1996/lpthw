states = {
    'oregon':'OR',
    'flordia':'FL',
    'california':'CA',
    'new york':'NY',
    'michigan':'MI'
}

cities = {
    'CA': 'san francisco',
    'MI': 'detroit',
    'FL': 'jacksonville'
}

#add some cities
cities['NY'] = 'new york'
cities['OR'] = 'portland'

#print these cities
print('-' * 10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

#print some states and it's abbreviation
print('-' * 10)
print("michigan's abbreviation is : " ,states['michigan'])
print("flordia's abbreviation is : ", states['flordia'])

#doing by doing
print('-' * 10)
print("michigan has : ", cities[states['michigan']])
print("flordia has : ",cities[states['flordia']])
print("california has : ",cities[states['california']])

#print all states's abbr
print('-' * 10)
for state, abbrs in list(states.items()):
    print(f"{state} is abbreviated {abbrs}")

#print all cities in states
print('-' * 10)
for abbrs, city in list(cities.items()):
    print(f"{abbrs} has the city {city}")

#do both at the same time
print('-' * 10)
for state, abbrs in list(states.items()):
    print(f"{state} is abbreviated {abbrs}")
    print(f"and has the city {cities[abbrs]}")      #abbrs  ==  states[state]

#get an abbr by state that might not be there
print('-' * 10)
state = states.get('texas')

if not state:
    print("sorry, no taxas")

#get a city with a default value
city = cities.get('TX','does not exist')
print(f"the city for state 'TX' is: {city}")
print(cities)
