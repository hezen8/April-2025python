class Account:
    def __init__(self,accNo,accName,accBal):
            self.accNo=accNo
            self.accName=accName
            self.accBal=accBal

    def deposit(self,amount):
        if amount<0:
            print("Error amount should be positive")
        else:
            self.accBal=self.accBal+amount
            print(f"Deposit of {amount} successfully")
            
    def withdraw(self,amount):
        if amount>self.accBal:
            print("Insufficient funds in your account")
        else:
            self.accBal=self.accBal-amount
            print(f"Confirmed withdrawal of {amount:.2f} account balance is{self.accBal}")
        
    def getBalance(self):
        return self.accBal
            

            

            