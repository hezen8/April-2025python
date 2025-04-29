length1=float(input("Enter the length"))
width1=float(input("Enter the width"))
areaofrec1= length1 * width1

length2=float(input("Enter the length"))
width2=float(input("Enter the width"))
areaofrec2= length2 * width2

if areaofrec1>areaofrec2:
    print("area of rectangle one is greater")
elif areaofrec2>areaofrec1:
    print("area of rectangle two is greater")
elif areaofrec2==areaofrec1:
    print("area ot the rectangles are the same")