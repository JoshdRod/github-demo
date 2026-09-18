def deposit(balance):
    amount_to_deposit = int(input("How much would you like to deposit? "))
    balance = balance + amount_to_deposit
    return balance

def withdraw(balance):
    amount = int(input("How much would you like to withdraw? "))
    return balance - amount
    
def display(balance):
    print(balance)

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
        print(balance)
    elif choice == 3:
        balance = withdraw(balance)

