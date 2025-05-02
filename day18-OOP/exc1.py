import account

# Global variable to track account balance
balance = 0

def get_menu():
    print()
    print("My Account")
    print("1-Deposit amount")
    print("2-Check balance")
    print("3-Withdraw cash")
    print("4-Quit program")

    choice = int(input("Enter a choice: "))

    while choice < 1 or choice > 4:
        choice = int(input("Enter a valid choice (1-4): "))
         
    return choice

def Deposit():
    global balance
    amount = int(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print(f"Deposit of {amount} was successful. Current balance is {balance}.")
    else:
        print("Invalid deposit amount.")

def withdraw():
    global balance
    amount = int(input("Enter amount to withdraw: "))
    if amount > balance:
        print("Insufficient funds in your account.")
    elif amount > 0:
        balance -= amount
        print(f"Confirmed withdrawal of {amount}. Current balance is {balance}.")
    else:
        print("Invalid withdrawal amount.")

def balance_check():
    global balance
    print(f"Your current balance is {balance}.")

def main():
    choice = 0
    while choice != 4:
        choice = get_menu()
        if choice == 1:
            Deposit()
        elif choice == 2:
            balance_check()
        elif choice == 3:
            withdraw()
    print("Thank you for using My Account. Goodbye!")

main()