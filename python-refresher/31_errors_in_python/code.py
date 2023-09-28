def divide(dividend, divisor):
	if divisor == 0:
		raise ZeroDivisionError("Divisor cannot be 0.")
	
	return dividend/divisor

# divide(15, 0)

# grades = [78, 99 , 85, 100]

# print("Welcome to the average grade program.")
# average = divide(sum(grades), len(grades))

# print(f"The average grade is {average}")

students = [
	{"name": "Bob", "grades": [75, 90]},
	{"name": "Rolf", "grades": []},
	{"name": "Jen", "grades": [100, 90]}
]

# try:
# 	for student in students:
# 		name = student['name']
# 		grades = student['grades']
# 		average = divide(sum(grades), len(grades))
# 		print(f"{name} averaged {average}.")
# except ZeroDivisionError:
# 	print(f"ERROR: {name} has no grades!")
# else:
# 	print("-- All stduent grades averages calculated --")
# finally:
# 	print("-- End of student average calculation --")

calculated_for_all = True
for student in students:
	name = student['name']
	grades = student['grades']
	try:
		average = divide(sum(grades), len(grades))
	except ZeroDivisionError:
		print(f"ERROR: {name} has no grades!")
		calculated_for_all = False
	else:
		print(f"{name} averaged {average}.")

if calculated_for_all:
	print("-- All stduent grades averages calculated --")
else:
	print("-- End of student average calculation --")	