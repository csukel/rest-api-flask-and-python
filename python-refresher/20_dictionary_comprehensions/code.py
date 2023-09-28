users = [
	(0, "Bob", "password"),
	(1, "Rolf", "bob123"),
	(2, "Jose", "longp4assword"),
	(3, "username", "1234")
]

username_mapping = {user[1]: user for user in users}
print(username_mapping)

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

user = username_mapping.get(username_input)

if user is not None:
	_, username, password = user
	if username is not None and password_input == password:
		print("Successfully authenticated")
	else:
		print("Erroneous login details")
else:
	print("Erroneous login details")
