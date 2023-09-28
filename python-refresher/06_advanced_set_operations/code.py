friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends - abroad # difference operator
local_friends = friends.difference(abroad)
print(local_friends)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science) 
both = art & science # intersection operator
print(both)