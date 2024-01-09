ops = {
    1: "Robi",
    2: "Airtel",
    3: "Banglalink",
    4: "Grameenphone",
    5: "Teletalk",
}


def mobile_recharge(db: dict[str, str]) -> dict[str, str]:
    print("1. Robi\n2. Airtel\n3. Banglalink\n4. Grameenphone\n5. Teletalk")
    operator = input("Enter your choice:")

    while operator.isdigit() is False or int(operator) > 5 or int(operator) < 0:
        operator = input("Invalid choice. Try again: ")
    operator = int(operator)

    cat = input("1. Prepaid\n2. Postpaid\nEnter your choice:")
    while cat.isdigit() is False or int(cat) > 2 or int(cat) < 0:
        print("Invalid choice")
        cat = input("1. Prepaid\n2. Postpaid\nEnter your choice:")
    cat = int(cat)

    number = input("Enter mobile number:")
    while number.isdigit() is False or len(number) != 11 or number[0:2] != "01":
        number = input("Invalid mobile number. Enter again:")
    number = int(number)

    amount = input("Enter amount:")
    while (
        amount.isdigit() is False or int(amount) < 0 or int(amount) > int(db["balance"])
    ):
        amount = input("Invalid amount. Enter again:")
    amount = int(amount)

    print(
        f"Operator: {ops[operator]}\nCategory: {'Prepaid' if cat == 1 else 'Postpaid'}\nMobile No: {number}\nAmount: {amount}"
    )

    pin = input("Enter Menu PIN to confirm:")
    while pin != db["pin"]:
        pin = input("Invalid PIN. Enter again:")

    db["balance"] = str(int(db["balance"]) - amount)

    print(
        f"Received Mobile Recharge request of Tk {amount} for {number}. Fee Tk 0.00. Balance Tk {db['balance']}. TrxID: XXXXXX is waiting for confirmation."
    )

    return db
