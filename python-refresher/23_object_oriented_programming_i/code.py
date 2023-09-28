class Student():
	def __init__(self, name, grades) -> None:
		self.name = name
		self.grades = grades
	
	def average_grade(self):
		return sum(self.grades) / len(self.grades)
	

rolf = Student(name="Rolf", grades=(88, 92, 100))

print("%.2f" % rolf.average_grade())