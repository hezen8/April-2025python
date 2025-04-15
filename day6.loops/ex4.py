for i in range(1,5):
    print(f"Enter marks for student #{i}")
    total=0
    for j in range(1,4):
        marks=int(input("Enter marks for test #{j}"))
        total=total+marks
    average=total/3
    print(f"Average marks for student {i} is {average:.2f}")