#2D list IS a list within a list(consists of rows and columns)
marks=[[70,60,80],[83,74,95],[57,76,87],[62,78,90]]
# total=0
# for mark in marks[0]:
#     total+=mark
# for mark in marks[1]:
#     total+=mark
# for mark in marks[2]:
#     total+=mark+total
# for mark in marks[3]:
#     total+=mark
# Total=total+total+total+total
# average=Total/12
# print(Total)
# print(average)

#SHORTEST WAY
total=0
for row in marks:
    for mark in row:
        total+=mark
print(f"The total marks is {total}")
print(f"The overall average is {total/12:.2f}")

# print(marks)
# print(marks[0])
# print(marks[1][2])
# print(marks[0][0])
# print(marks[3][2])
#Another way
# marks=[[70,60,80], #number of rows
# [83,74,95],
# [57,76,87],
# [62,78,90]] 
# print(marks)
