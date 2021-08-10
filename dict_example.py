states = {
"Virginia": "VA",
"Maryland": "MD",
"Pennsylvania": "PA",
"NewYork": "NY"
}

cities = {
"VA": "Fairfax",
"MD": "Silver Spring",
"NY": "Rochester"
}

cities["PA"] = "Monroeville"

#Print some cities
print("-" *10)
print("NY state has: ", cities['NY'])
print("PA state has: ", cities[states["Pennsylvania"]])

#print some states
print("-" *10)
print("Virginia's abbreviation is: ", states["Virginia"])
print("Maryland's abbreviation is: ", states["Maryland"])

#print all states name
print("-" *10)
for state,abb in list(states.items()):
    print(f"State {state} is abbreviated as {abb}")

# print all cities
print("-" *10)
for abb, city in list(cities.items()):
    print(f"{abb} has city {city}")


#print all city and states
print("-" *10)
for state,abb in list(states.items()):
    print(f"State {state} is abbreviated as {abb}", end = " ")
    print(f" and has city {cities[abb]}")

print("-" *10)
state = states.get("Texas")
print(states)
