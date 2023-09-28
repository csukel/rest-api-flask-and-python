friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

print(friends == abroad) # True , checks if both have identical elements
print(friends is abroad) # False , checks if they have the same reference in memory

abroad = friends
print(friends is abroad) # True, now those two have the same reference into memory