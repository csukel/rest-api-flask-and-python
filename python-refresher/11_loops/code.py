import random

number = random.randint(1, 10)
tries = 3


def get_input(prompt_text, type, **kwargs):
    user_res = input(prompt_text)

    if type(user_res) == type:
        print(f"Your response is incorrect. Please provide a value of type {type}")
        return get_input(prompt_text, type, kwargs)

    user_res = type(user_res)

    lov = kwargs.get("lov")
    if lov is not None and user_res not in lov:
        print(f"Value provided is not within the acceptable values {lov}")
        return get_input(prompt_text, type, kwargs)

    return user_res


while tries > 0:
    user_guess = int(
        get_input("Guess a number from 1 to 10: ", int, lov=[i for i in range(1, 11)])
    )

    if user_guess == number:
        print(f"You guesed it right. The correct number is {number}")
        break
    elif user_guess > number:
        print(f"The number you guessed is qreater than what we are looking for...")
    else:
        print(
            f"The number you guessed is lessser in comparison to what we are looking for .."
        )

    tries -= 1
    print(f"You have another {tries} {'try' if tries == 1 else 'tries'}")
    print("======================")
    print()
