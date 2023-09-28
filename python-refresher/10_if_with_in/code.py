# movies_watched =  {"The Matrix", "Green Book", "Her"}
# user_movie = input("Which movie have you recently watched? ")

# if user_movie in movies_watched:
# 	print("Great. I have recently watched it as well!")
# else:
# 	print("Hmm i have not watched that movie yet")
import random
number = random.randint(1,10)

user_guess = input("Guess a number from 1 to 10: ")

if str(number) == user_guess:
	print(f"You are correct. The number drawn was {number}")
else:
	print(f"Your guess is wrong. The number drawn was {number}")