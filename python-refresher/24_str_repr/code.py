class Person():
	def __init__(self, name, age) -> None:
		self.name = name
		self.age = age

	def __str__(self) -> str:
		return f"Name: {self.name}, age: {self.age}"

	def __repr__(self) -> str:
		return f"<Person('{self.name}', {self.age})"
	
peter = Person(name="Peter", age=30)
print(peter)
print(peter)