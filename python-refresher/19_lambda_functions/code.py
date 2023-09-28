# def add(x, y):
# 	return x + y

# print(add(5, 7))

# add = lambda x, y: x + y

# print(add(5, 7))

# print((lambda x, y: x + y)(5,7))

def double(x):
	return x * 2

sequence = [1, 2, 3, 4, 5]
# doubled = [double(x) for x in sequence]
# doubled = [ (lambda x: x * 2)(x) for x in sequence]
# doubled = map(double, sequence)
doubled = list(map(lambda x: x * 2, sequence))

print(sequence)
print(doubled)