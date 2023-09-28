friend_ages  = {"Rolf": 24, "Adam" : 30, "Anne" : 27}

# print(friend_ages.get("Adam"))
print(friend_ages["Adam"])

friend_ages["Bob"] = 22

print(friend_ages)

friends = [
	{"name" : "Rolf", "age": 24},
	{"name" : "Adam", "age": 30},
	{"name" : "Anne", "age": 27}
]

print(friends)

print(friends[1]["name"])

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student in student_attendance:
	print(f"{student}: {student_attendance[student]}")
# or
for student, grade in student_attendance.items():
	print(f"{student}: {grade}")

attendance_values = student_attendance.values()
print(f"Average score is: {sum(attendance_values)/len(attendance_values)}")