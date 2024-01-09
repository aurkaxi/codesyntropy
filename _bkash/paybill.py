from print_line import print_line


def pay_bill(db: dict):
    try:
        user_pay_taka = float(input("Enter amount: "))
        get_available_balance = db.get("balance", 0)

        if get_available_balance >= user_pay_taka:
            db.update({"balance": get_available_balance - user_pay_taka})
            print_line("Successfully payment.")
        else:
            print_line("Insufficient balance")
    except:  # noqa: E722
        print_line("\nInvalid amount\n")
        return pay_bill(db)
