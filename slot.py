# This is a text based slot machine
# The user will deposit how ever much money they want then bet on one of three lines of slot machine
# Then a win will be determined
# the user can keep playing until they cash out or lose all their money

MAX_LINES = 7
MAX_BET = 100
MIN_BET = 10

# Collecting user input for money deposit


def deposit():
    while True:
        amount = input("What is your deposit amount? $")
        # checks input to make sure it is a valid number (whole) and nothing else
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print("Balance: ${}".format(amount))
                break
            else:
                print("Your deposit must be more than {}".format(amount))
        else:
            print("Enter your amount")
    return amount

# collecting bet from user


def bet():
    # gets number of line for slot machine
    while True:
        lines = input(
            "Enter number of line to bet on (1 - {})? ".format(str(MAX_LINES)))
        # checks input to make sure it is a valid number and nothing else
        if lines.isdigit():
            lines = int(lines)
            if lines in range(1, MAX_LINES):
                break
            else:
                print("Enter valid number of lines")
        else:
            print("Please enter your number")
    return lines

# main section


def slots():
    balance = deposit()
    lines = bet()
    print(balance, lines)


slots()
