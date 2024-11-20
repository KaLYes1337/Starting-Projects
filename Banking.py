#Banking Program
def show_balance(balance):
    print("----------------------")
    print(f"Your current balance is {balance:.2f}")
    print("----------------------")


def deposit():
    print("----------------------")
    deposit_amount = float(input("Enter the amount you wish to deposit: "))
    print("----------------------")
    return deposit_amount


def withdraw(balance):
    print("----------------------")
    withdraw_amount = float(input("Enter the amount you wish to withdraw: "))
    print("----------------------")
    if withdraw_amount > balance:
        print("-------------------")
        print("Insufficient funds!")
        print("-------------------")
        return 0
    else:
        return withdraw_amount


def main():
    balance = 0
    is_running = True

    while is_running:
        print("----------------------")
        print("   Banking account!   ")
        print("----------------------")
        print("Choose one of the following:")
        print("1.Show balance!")
        print("2.Deposit!")
        print("3.Withdraw!")
        print("4.Exit!")
        print("----------------------")
        user_input = input("Enter choice (1-4): ")
        if user_input == "1":
            show_balance(balance)
        elif user_input == "2":
            balance += deposit()
        elif user_input == "3":
            balance -= withdraw(balance)
        elif user_input == "4":
            is_running = False
        else:
            print("----------------------")
            print("    Invalid input!    ")
            print("----------------------")

    print("Have a nice day!")


if __name__ == "__main__":
    main()
