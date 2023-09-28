numbers = [1, 3, 5]

doubled = [num*2 for num in numbers]
print(doubled)


friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
# start_s = [name for name in friends if name[0].lower() == "s"]
start_s = [friend for friend in friends if friend.startswith("S")]
print(start_s)

print("friends: ", id(friends), "\nstarts_s: ", id(start_s))