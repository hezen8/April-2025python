def rect_area(l,w):
    return l*w

def perimeter(l,w):
    return 2*(l+w)

num1=float(input("Enter the length"))
num2=float(input("Enter the width"))
# print(f"area of the rectangle is {rect-area(length,width)}")
# print(f"perimeter of the rectangle is {rect-perimeter(length,width)}")

result= rect_area(num1,num2)
print(f"area of rectangle is {result}")

result= perimeter(num1,num2)
print(f"perimeter of the rectangle is {result}")