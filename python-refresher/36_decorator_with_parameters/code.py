import functools

user = {"username": "joe", "access_level": "admin"}


def make_secure(func):
    @functools.wraps(func) # this is used to avoid overriding 
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return "You have no admin rights"

    return secure_function


@make_secure
def get_admin_password(panel=None):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"
    else: 
        return "simple password"

password = get_admin_password()
print(password)
