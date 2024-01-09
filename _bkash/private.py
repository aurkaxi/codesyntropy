def private(password):
    user_password = input("Enter your password: ")
    if user_password == password:
        return True
    else:
        return False
