def payment(db: dict[str, str]) -> dict[str, str]:
    to = input("Enter Merchant account number: ")
    while to.isdigit() is False or len(to) != 11 or to[0:2] != "01":
        to = input("Invalid Merchant account number. Enter again: ")

    amount = input("Enter amount: ")
    while amount.isdigit() is False or int(amount) > int(db["balance"]):
        amount = input("Invalid amount. Enter again: ")
    amount = int(amount)

    ref = input("Enter reference: ")

    counter_no = input("Enter counter no: ")
    while (
        counter_no.isdigit() is False
        or len(counter_no) != 1
        or counter_no[0] not in ["0", "1"]
    ):
        counter_no = input("Invalid counter no. Enter again: ")

    print(f"To: {to}\nAmount: {amount}\nReference: {ref}\nCounter No: {counter_no}")

    pin = input("Enter Menu PIN to confirm: ")
    while pin != db["pin"]:
        pin = input("Invalid PIN. Enter again: ")

    db["balance"] = str(int(db["balance"]) - amount)
    print(
        f"Payment Tk {amount} to {to} successful. Ref {ref}. Counter {counter_no}. Fee 0.00. Balance {db['balance']}. TrxID: XXXXXX."
    )

    return db
