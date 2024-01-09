def cash_out(db: dict[str, str]) -> dict[str, str]:
    to = input("Enter Agent bKash Account Number: ")
    while to.isdigit() is False or len(to) != 11 or to[0:2] != "01":
        to = input("Invalid Agent Account Number. Enter again: ")

    amount = input("Enter amount: ")
    fee = 0
    while True:
        if amount.isdigit() is False:
            amount = input("Invalid amount. Enter again: ")
            continue

        fee = int(amount) * 0.0185
        if int(amount) + fee > int(db["balance"]):
            amount = input("Insufficient balance. Enter again: ")
            continue
        else:
            break
    amount = int(amount)

    print(f"To: {to}\nAmount: {amount}")

    pin = input("Enter Menu PIN to confirm: ")
    while pin != db["pin"]:
        pin = input("Invalid PIN. Enter again: ")

    db["balance"] = str(int(db["balance"]) - amount - fee)

    print(
        f"Cash Out Tk {amount} to {to} successful. Fee Tk {fee}. Balance Tk {db['balance']}. TrxID: XXXXXX."
    )

    return db
