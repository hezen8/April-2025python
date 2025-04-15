marks=int(input("Enter percentage marks scored "))
if marks>100 or marks<0:
    print("Error !!! Enter valid mark 0-100%")
elif marks>=70:
    print("Grade is A")
elif marks>=60:
    print("Grade is B")
elif marks>=50:
    print("Grade is C")
elif marks>=40:
    print("Grade is D")
elif marks>=30:
    print("Grade is E")
else:
    print("Grade is F")
