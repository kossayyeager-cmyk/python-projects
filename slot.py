import random as r

def spinrow():
    symbols = ['🍋', '🍒', '⭐', '🔔', '🍉']
    result = []

    for symbol in range(3):
        result.append(r.choice(symbols))

    return result


def printrow(result):
    print("*" * 10)
    print("|".join(result))
    print("*" * 10)


def getpayout(result, bet):
    if result[0] == result[1] == result[2]:
        if result[0] == "🍒":
            return bet * 2
        if result[0] == "🍋":
            return bet * 4
        if result[0] == "🍉":
            return bet * 6
        if result[0] == "🔔":
            return bet * 10
        if result[0] == "⭐":
            return bet * 20

    return 0


def main():
    print("*" * 10)
    print("Welcome to the slot machine program:")
    print("The symbols: 🍋🍒⭐🔔🍉")
    print("*" * 10)

    balance = float(input("Enter your balance: "))

    while balance > 0:
        print("Place your bet:")
        bet = input("Enter your bet: ")

        if str(bet)=="q":
                       break
        
        try:
            bet = float(bet)
            if bet <= 0:
                print("Enter a valid bet(q to exit)")
                continue

        except ValueError:
            print("Enter a valid number")
            continue

        if bet > balance:
            print("Insufficient funds")
            continue
        

        balance -= bet

        row = spinrow()
        print("Spinning...\n")
        printrow(row)

        payout = getpayout(row, bet)
        balance += payout

        if payout > 0:
            print(f"You won: {payout}")
        else:
            print("You lost")

        print(f"Current balance: {balance}")


if __name__ == '__main__':
    main()