i=7
while i>=1:
    print("\n")
    j=i
    while (j>=1):
        print("*",end="")
        j=j-1
    i=i-1

rows=7
for i in range(rows+1,0, -1):
    print("\n")
    for j in range(0, i-1):
        print("*",end=" ")