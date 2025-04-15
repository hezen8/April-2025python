proceed=True
totalExpenses=0
budgetAmount=float(input("Enter the amount budgeted for a month"))
while proceed:
    expenses=float(input("Enter the current expense"))
    totalExpenses=totalExpenses+expenses
    print("Do you wish to continue Enter y(yes) or any other key (No)")
    response=input()
    if response.lower() !='y':
        proceed=False

print(f"Budgetamount minus totalexpenses is ksh {budgetAmount-totalExpenses:.2f}")
