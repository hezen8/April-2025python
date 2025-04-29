try:
    num1=int(input("Enter a number"))
    num2=int(input("Enter a second number"))
    print(f"The quotient is {num1/num2}")
except ZeroDivisionError:
    print("division by zero is not possible")
except ValueError:
    print("Enter integer values")
except Exception:
    print("An error occured")

print("End of program")