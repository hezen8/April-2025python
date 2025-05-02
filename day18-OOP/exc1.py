import account

# acc1=account.Account(1111,"alex",500)
# acc1.getBalance()
# print(acc1.getBalance())

def get_menu():
    print()
    print("My Account")
    print("1-Deposit amount")
    print("2-check balance")
    print("3-withdraw cash")
    print("4-Qiut program")

    choice=int(input("Enter a choice"))

    while choice<1 or choice>4:
         choice=int(input("Enter a valid choice(1-4)"))
         
    return choice



def Deposit(amount):
    bal=0
    amount=int(input("Enter amount to deposit"))
    bal+=amount
    print(f"deposit of {amount} was successful and balance is {bal}")

     
def withdraw(amount):
    if amount>balance:
          print("Insufficient funds in your account")
    else:
        balance=balance-amount
        print(f"Confirmed withdrawal of {amount:.2f} account balance is{balance}")
        
    

def main():
        amount={}
        choice=0
        while choice !=4:
            choice = get_menu()
            if choice==1:
                Deposit(amount)
            elif choice==2:
                balance(amount)
            elif choice==3:
                withdraw(amount)
main()
            
    
