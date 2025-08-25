#Bank System V1, this system is just for 3 operations
# 1. Statement
# 2. Deposit
# 3. Withdraw
# with a withdraw limit of 3 by day can't be exceeding 500
# just positive amounts are allowed and just one user is allowed
# can't be withdrawn negative amounts

LIMIT_WITHDRAW_BY_DAY = 3
LIMIT_WITHDRAW_AMOUNT = 500

depositAmount = 0
withdrawAmount = 0

bankAmounts = {
    "statement": 0.00,
    "operations": 0,
    "deposits": 0,
    "withdrawals": 0
}

menu = """

Welcome to your bank account


    [s] Statement
    [d] Deposit
    [w] Withdraw
    [e] Exit

    
software v1 
"""


while True:

    option = input(menu)

    if option == "s":
        print("Statement of your account")
        print(f"Your balance is: R$ {bankAmounts['statement']:.2f}")
        print(f"Total operations: {bankAmounts['operations']}")
        print(f"Total deposits: {bankAmounts['deposits']}")
        print(f"Total withdrawals: {bankAmounts['withdrawals']}")

    elif option == "d":
        print(f"Deposit, your balance is: R$ {bankAmounts['statement']:.2f}")

        while True:
            depositAmount = float(input("Enter the deposit amount: R$ "))

            if depositAmount <= 0:
                print("Deposit amount must be positive, try again: R$ ")
            else:
                bankAmounts['statement'] += depositAmount
                bankAmounts['operations'] += 1
                bankAmounts['deposits'] += 1
                break
        
        
    elif option == "w":
        print(f"Withdraw your balance is: R$ {bankAmounts['statement']:.2f}")

        if bankAmounts["withdrawals"] < LIMIT_WITHDRAW_BY_DAY:
            while True:
                withdrawAmount = float(input("Enter the withdrawal amount: R$ "))
                if withdrawAmount <= 0:
                    print("Nothing withdrawn, back to menu")
                    break
                elif withdrawAmount > bankAmounts['statement']:
                    print("You don't have enough balance, try again: R$ ")
                elif withdrawAmount > LIMIT_WITHDRAW_AMOUNT:
                    print("You exceeded the withdrawal limit of R$ 500, try again: R$ ")
                else:
                    bankAmounts['statement'] -= withdrawAmount
                    bankAmounts['operations'] += 1
                    bankAmounts['withdrawals'] += 1
                    break
        else:
            print("Sorry you exceeded your withdrawal limit by day")

    elif option == "e":
        print("Exit, thank you for using our service!")
        break
    else:
        print("Invalid option, try another one again")