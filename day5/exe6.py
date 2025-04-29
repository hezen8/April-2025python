month=float(input("Enter month (in numeric form)"))
day=float(input("Enter a day"))
year=float(input("Enter a two digit year"))

if month*day==year:
    print("The date is magic")
elif month*day!=year:
    print("The date is not magic")