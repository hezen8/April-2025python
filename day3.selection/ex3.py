age=int(input("Please enter your age"))
if age<0:
    print("Error !!! Enter valid mark 0-100%")
elif age<=1:
    print("you are an infant")
elif age>1 and age<13:
    print("you are a child")
elif age>=13 and age<20:
    print("you are a teenager")
elif age>=20:
    print("you are an adult")
