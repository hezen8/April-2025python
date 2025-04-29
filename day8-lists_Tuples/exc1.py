marks=[]
total=0
for j in range(1,6):
    mark=float(input(f"Enter marks"))
    marks.append(mark)
   
    total=mark+total
average=total/5
print(max(marks))
print(min(marks))
print(f"the average mark is{average}")