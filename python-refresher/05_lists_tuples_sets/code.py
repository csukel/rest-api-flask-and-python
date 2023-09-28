l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")
s = {"Bob", "Rolf", "Anne"}

# print(t)
# t[1] = "Loucas" # Error (tuple does not allow assignment)
# print(t)
print(s)
s.add("Loucas")
s.add(
    "Loucas"
)  # sets does not allow duplicate values hence this statement won't do anything
print(s)
