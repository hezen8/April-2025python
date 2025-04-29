item1=float(input("Enter the purchase price"))
item2=float(input("Enter the purchase price"))
item3=float(input("Enter the purchase price"))
item4=float(input("Enter the purchase price"))
item5=float(input("Enter the purchase price"))

subtotal= item1 + item2 +item3 + item4 +item5  
sales_tax=subtotal * 0.07
total=sales_tax + subtotal

print(f"{subtotal}")
print(f"{sales_tax}")
print(f"{total}")
