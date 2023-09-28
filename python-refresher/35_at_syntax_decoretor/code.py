import functools

user = {"username": "joe", "access_level": "guest"}


def make_secure(func):
    @functools.wraps(func) # this is used to avoid overriding 
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return "You have no admin rights"

    return secure_function


@make_secure
def get_admin_password():
    """
    Gets the password of admin
    """
    return "1234"


print(get_admin_password.__name__)
print(get_admin_password.__doc__)
password = get_admin_password()
print(password)
