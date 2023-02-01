import random


# This is a text based slot machine
# The user will deposit how ever much money they want then bet on one of three lines of slot machine
# Then a win will be determined
# the user can keep playing until they cash out or lose all their money

MAX_LINES = 7
MAX_BET = 100
MIN_BET = 10

# Collecting user input for money deposit *********************************************************


def deposit():
    while True:
        amount = input("What is your deposit amount? $")
        # checks input to make sure it is a valid number (whole) and nothing else
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Your deposit must be more than {}".format(amount))
        else:
            print("Enter your amount")
    return amount

# collecting bet from user ***********************************************************************


def lines():
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

# getting the bet from user **********************************************************************


def get_bet():
    while True:
        bet = input("What is your bet? $")
        # checks input to make sure it is a valid number (whole) and nothing else
        if bet.isdigit():
            bet = int(bet)
            if bet in range(MIN_BET, MAX_BET):
                break
            else:
                print(
                    "Your bet must be between ${0} - ${1}".format(MIN_BET, MAX_BET))
        else:
            print("Enter your bet please")
    return bet

# main section ***********************************************************************************


def slots():
    balance = deposit()
    line = lines()
    while True:
        bet = get_bet()
        total_bet = bet * line

        if total_bet not in range(balance):
            print("Insufficient funds can\'t cover bet.\n-- Current Balance: ${0} --\n-- Your bet: ${1} --".format(
                balance, total_bet))
        else:
            break
    print("You bet ${0} on {1} lines, making total bet ${2}".format(
        bet, line, total_bet))


slots()
