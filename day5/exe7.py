seconds=0
hours=0
days=0
seconds=float(input("Enter number of seconds"))
if seconds>=86400:
    days=seconds//86400
    seconds=seconds%86400
if seconds>=3600:
    hours=seconds//3600
    seconds = seconds%3600
if seconds>=60:
    min=seconds//60
    seconds=seconds%60


print(f"{days},{hours},{min},{seconds}")
