import random


# This is a text based slot machine
# The user will deposit how ever much money they want then bet on one of three lines of slot machine
# Then a win will be determined by getting the amount of lines choosen in a row
# the user can keep playing until they cash out or lose all their money

MAX_LINES = 3
MAX_BET = 2000
MIN_BET = 10

ROWS = 3
COLUMNS = 3

# Symbols for the slot machine ********************************************************************
symbol_count = {
    'A': 7,
    'B': 7,
    'C': 7,
    'D': 7
}
symbol_values = {
    'A': 7,
    'B': 7,
    'C': 7,
    'D': 7
}

# determines what qualify as a winner
def check_winner(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

# Slot machine spin will randomly pick values
def slot_maschine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


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
            "Enter number of lines to bet on (1 - {})? ".format(str(MAX_LINES)))
        # checks input to make sure it is a valid number and nothing else
        if lines.isdigit():
            lines = int(lines)
            if lines > 0 and lines <= MAX_LINES:
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
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(
                    "Your bet must be between ${0} - ${1}".format(MIN_BET, MAX_BET))
        else:
            print("Enter your bet please")
    return bet

# main section ***********************************************************************************
def slots(balance):
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
    slot = slot_maschine_spin(ROWS, COLUMNS, symbol_count)
    print_slot_machine(slot)
    winnings, winning_lines = check_winner(slot, line, bet, symbol_values)
    if winnings == 0:
        print("You won ${}".format(winnings))
    else:
        print("You won ${}".format(winnings))
        print("You won on", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print("Current balance is ${}".format(balance))
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += slots(balance)

    print(f"You left with ${balance}")


main()
