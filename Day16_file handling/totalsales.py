with open("sales.txt","w") as g:
    total=0
    for counter in range(1,8):
        sales=float(input(f"Enter sales for#{counter}"))
        g.write(str(sales)+"\n")
        total+=int(sales)

print(f"total sales of the week is {total}")
