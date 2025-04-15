number=float(input("Enter a positive number to add and a negative number to quit")) #priming read
total=0
while(number>=0):
    total=total+number
    number=float(input("Enter a positive number to add and a negative number to quit")) 
print(f"The sum of numbers entered is {total}")