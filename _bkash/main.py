from command import command
from helpline import helpline
from my_account import my_account
from paybill import pay_bill
from user_choice import user_choice
from send_money import send_money


def main():
    isQuit = False
    [account_details, db] = my_account()
    while not isQuit:
        command()
        choice = user_choice()
        if choice == 1:
            send_money()
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pay_bill(db())
        elif choice == 5:
            account_details()
        elif choice == 6:
            helpline()
        elif choice == 7:
            isQuit = True


main()
