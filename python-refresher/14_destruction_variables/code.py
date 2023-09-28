t = 5, 11

print(t)

x, y = t  # destruct variable
print(f"x: {x}, y: {y}")

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

print(list(student_attendance.items()))

for t in student_attendance.items():
    name, grade = t
    print(f"Name: {name} , Grade: {grade}")

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")

person = ("Bob", 42, "Mechanic")
(
    name,
    _,
    profession,
) = person  # undescore variables should be ignored based on what is agreed by the python community
print(name, profession)

head, *tail = [1, 2, 3, 4, 5]
print(head) # 1
print(tail) # [2, 3, 4, 5]

*head, tail = [1, 2, 3, 4, 5]
print(head) # [1, 2, 3, 4]
print(tail) # 5