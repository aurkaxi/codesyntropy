from bill import pay_bill
from cash_out import cash_out
from download import download_bkash_app
from microfinance import microfinance
from my_bkash import my_bkash
from payment import payment
from recharge import mobile_recharge
from reset_pin import reset_pin
from transfer import send_money, send_money_to_non_bkash_user

options = {
    1: send_money,
    2: send_money_to_non_bkash_user,
    3: mobile_recharge,
    4: payment,
    5: cash_out,
    6: pay_bill, # not implemented
    7: microfinance, # not implemented
    8: download_bkash_app, # not implemented
    9: my_bkash, # not implemented
    10: reset_pin, # not implemented
}

db = {"pin": "1234", "balance": "10000"}

while True:
    print(
        "1. Send Money\n2. Send Money to Non-bkash User\n3. Mobile Recharge\n4. Payment\n5. Cash Out\n6. Pay Bill (Not implemented)\n7. Microfinance (Not implemented)\n8. Download bKash App (Not implemented)\n9. My bKash (Not implemented)\n10. Resset PIN (Not implemented)\n0. Exit"
    )
    choice = input("Enter your choice: ")
    if choice.isdigit() is False or int(choice) > 10 or int(choice) < 0:
        print("Invalid choice")
        continue
    choice = int(choice)

    if choice == 0:
        break

    db = options[choice](db)
