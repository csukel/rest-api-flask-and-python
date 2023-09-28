user = {"username": "joe", "access_level": "guest"}

def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else: 
            return "You have no admin rights"
    
    return secure_function

def get_admin_password():
    return "1234"

get_pass = make_secure(get_admin_password)
print(get_pass())