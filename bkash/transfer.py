def send_money(db: dict[str, str]) -> dict[str, str]:
    to = input("Enter Receiver bKash Account No: ")
    while to.isdigit() is False or len(to) != 11 or to[0:2] != "01":
        to = input("Invalid bKash Account No. Enter again: ")
    to = int(to)

    amount = input("Enter amount: ")
    fee = 0
    while True:
        if amount.isdigit() is False:
            amount = input("Invalid amount. Enter again: ")
            continue

        fee = 0 if int(amount) < 100 else 5 if int(amount) < 25000 else 10
        if int(amount) + fee > int(db["balance"]):
            amount = input("Insufficient balance. Enter again: ")
            continue
        else:
            break
    amount = int(amount)

    ref = input("Enter reference: ")

    print(f"To: {to}\nAmount: {amount}\nReference: {ref}")

    pin = input("Enter Menu PIN to confirm: ")
    while pin != db["pin"]:
        pin = input("Invalid PIN. Enter again: ")

    db["balance"] = str(int(db["balance"]) - amount - fee)

    print(
        f"Send Money Tk {amount} to {to} successful. Ref {ref}. Fee Tk {fee}. Balance Tk {db['balance']}. TrxID: XXXXXX."
    )

    return db


def send_money_to_non_bkash_user(db: dict[str, str]) -> dict[str, str]:
    return send_money(db)
