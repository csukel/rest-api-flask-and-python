def multiply(*args):
	total = 1 
	for arg in args:
		total *= arg
	return total


print(multiply(2, 3, 5))

def add(x, y):
	return x + y

nums = [3, 5]
print(add(*nums))

nums = {"x": 15, "y": 25}
print(add(**nums))