
price=float(input("Enter item price \n"))
total=0
for counter in range(1,11):
    price=float(input(f"Enter item price {counter} \n"))
    while price<0:#using a while loop for input validation
        print("Enter a valid price (>=0)")
        price=float(input(f"Enter item price {counter} \n"))
    total=total+price
print(f"Total price for 10 items is ksh{total:.2f}")