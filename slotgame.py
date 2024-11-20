import random


def spin_row():
    symbols = ["🍀", "🔔", "🍉", "⭐", "🍇"]
    return [random.choice(symbols) for s in range(3)]


def print_row(row):
    print(" | ".join(row))


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍀":
            return bet * 50
        elif row[0] == "🔔":
            return bet * 20
        elif row[0] == "⭐":
            return bet * 10
        elif row[0] == "🍉":
            return bet * 5
        elif row[0] == "🍇":
            return bet * 2
    return 0


def main():
    print("Welcome do 40 BURNING HOT")
    print("*** 🍀 🔔 🍉 ⭐ 🍇 ***\n")
    deposit = float(input("Deposit amount: "))

    while deposit > 0:
        bet = input("Place bet amount: ")
        print(f"Balance {deposit}$")
        if not bet.isdigit:
            print("Enter valid number: ")
            continue
        bet = float(bet)
        if bet > deposit:
            print("Insufficient funds!!!")
            continue
        if bet < 1:
            print("Minimum bet ammount is 1$")
            continue

        deposit -= bet

        row = spin_row()
        print(" ")
        print_row(row)

        win = get_payout(row, bet)
        if win > 0:
            print(f"You won ${win}")
        else:
            print("No win")
            print(" ")
        deposit += win


if __name__ == "__main__":
    main()
