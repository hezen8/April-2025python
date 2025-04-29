prices=[]
total=0
for price in range(1,8):
    sale=float(input(f"Enter store sales for day{price}"))
    prices.append(sale)
    total=sale+total
print(f"Total sales of the week is kshs: {total:.2f}")
