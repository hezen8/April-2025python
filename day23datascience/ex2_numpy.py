import numpy as np
#having a multi_dimensional array
marks=np.array([[15,56,78,65,90],[45,41,54,63,77],[78,89,90,91,92]])
# print(marks.dtype)
# for i in marks:
#     for j in i:
#         print(j,end=" ")
# print()
# print(marks.ndim)
# print(marks.sum())
# print(marks.sum(axis=0))
# print(marks.sum(axis=1))
# #square root of each element
# print(np.sqrt(marks))
# #getting range of numbers from arrays
# numbers=np.arange(1,11)
# numbers2=np.arange(11,21)
# numbers3=np.add(numbers,numbers2)
# print(numbers)
# print(numbers2)
# print(numbers3)

# #multiplying numbers in array by a number
# print(numbers*2)

# #indexing and slicing
# print(numbers[0])   #first element
# print(numbers[0:5]) #first 5 elements
# print(numbers[0:5:2]) #first 5 elements with step of 2

#exercise
# numbers=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
# evennumbers=[number for number in range(len(numbers)) if number%2==0]
# print(evennumbers)

# numbers=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
# oddnumbers=[number for number in range(len(numbers)) if number%2!=0]
# print(oddnumbers)

#slicing
# print(marks[[0,2],3])
# print(marks[0:2,0:3])


