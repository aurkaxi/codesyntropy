def user_choice():
    try:
        choice = int(input("Enter your choice: "))
        return choice
    except:  # noqa: E722
        return user_choice()
