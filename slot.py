# This is a text based slot machine
# The user will deposit how ever much money they want then bet on one of three lines of slot machine
# Then a win will be determined
# the user can keep playing until they cash out or lose all their money


# Collecting user input for money deposit and bet
def deposit():
    while True:
        amount = input("What is your deposit amount? $")
        # checks input to make sure it is a valid number and nothing else
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


deposit()
