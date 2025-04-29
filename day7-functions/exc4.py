def amount(x,y=0.8):
    return x*y

rep_cost=float(input("Enter replacement amount"))
result=amount(rep_cost)
print(f"the minimum amount of insurance you should buy for the property is {result}")

