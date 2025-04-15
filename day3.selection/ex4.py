year=int(input("Enter the year"))
if year % 100==0 and year % 400==0 or year % 100 !=0 and year % 4==0:
    print("Leap year 29 days in February")
else:
    print("not a leap year 28 days in Februry")