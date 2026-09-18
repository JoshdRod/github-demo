def deposit(balance):
    amount_to_deposit = int(input("How much would you like to deposit? "))
    balance = balance - amount_to_deposit
    return balance

def withdraw(balance):
    pass # TODO: This function should ask the user how much they want to withdraw, and subtract that from their balance. Don't worry about invalid inputs - assume the atm user is a smart guy. Return the balance.

def display(balance):
    pass # TODO

balance = 67
while True:
    print("Welcome to the Python ATM! What would you like to do?")
    print("1. View Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    choice = int(input())
    if choice == 1:
        display(balance)
    elif choice == 2:
        balance = deposit(balance)
    elif choice == 3:
        balance = withdraw(balance)

