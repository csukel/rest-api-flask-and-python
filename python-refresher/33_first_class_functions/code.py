from functools import reduce

def add(*args):
    return sum(args)

def multiply(*args):
    return reduce((lambda x, y: x * y), args) 

def calculate(*args, operator):
    return operator(*args)

nums = (1 , 2, 3, 4)
print(f"Sum of {nums} is {calculate(*nums, operator=add)}")
print(f"Product of {nums} is {calculate(*nums, operator=multiply)}")
print(f"The min value of {nums} is {min(nums)}")
print(f"The max value of {nums} is {max(nums)}")