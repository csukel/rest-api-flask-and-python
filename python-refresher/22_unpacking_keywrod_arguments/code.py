# def named(**kwargs): #pack args to dictionary
# 	print(kwargs)

# named(name="Bob", age=25)

# def named(name, age):
# 	print(name, age)


# person = {"name": "Bob", "age": 25}
# named(**person) #unpack dictionary args

# def named(**kwargs):
# 	print(kwargs)

# def print_nicely(**kwargs):
# 	named(**kwargs)
# 	for arg, value in kwargs.items():
# 		print(f"{arg}: {value}")

# print_nicely(name="Bob", age=25, profession="Engineer")

def both(*args, **kwargs):
	print(args)
	print(kwargs)

both(1, 2, 3, 5, name="Bob", age=25)