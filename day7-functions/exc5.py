def addition(x,y):
    return x+y

loan=float(input("Enter loan payment"))
insurance=float(input("Enter insurance"))
gas=float(input("Enter gas payment"))
oil=float(input("Enter oil payment"))
tires=float(input("Enter tires payment"))
maintenance=float(input("Enter maintenance payment"))
total=loan+insurance+gas+oil+tires+maintenance
monthlycost=total*6
annualcost=monthlycost*12

print(f"The total monthly cost is{monthlycost}")
print(f"The annual cost is {annualcost}")