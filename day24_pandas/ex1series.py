#series is a one-dimensional array-like object that can hold any data type
#it is similar to a list or a dictionary
#it is a labeled array, meaning that each element in the series has an index
#it is similar to a dictionary in that it can hold different data types
#it is similar to a list in that it is a one-dimensional array-like object
#it is similar to a numpy array in that it is a one-dimensional array-like object
#it is similar to a dataframe in that it is a one-dimensional array-like object
#and is labeled with an index
import numpy as np
import pandas as pd

#creating and storing values in a series
grades = pd.Series([90, 80, 70, 60, 50])
# print(grades[0])
# print(grades.count())
# print(grades.mean())
# print(grades.max())
# print(grades.min())
# print(grades.sum())
# print(grades.std()) #standard deviation
# print(grades.median()) #median
# print(grades.mode()) #mode
# print(grades.var()) #variance
# print(grades.describe()) #summary statistics

#creating a series with custom index
grades2 = pd.Series([96, 78, 87, 69, 10])
#assigning labels to the list in a series
grades2 = pd.Series([96, 78, 87, 69, 10],index=["hexe","Martha","maggy","jumior","zippy"])
print(grades2)
#using a dictionary to create a series
#creating a series from a dictionary
dictGrades={"hexe":96,"Martha":78,"maggy":87,"jumior":69,"zippy":10}
grades3=pd.Series(dictGrades)
print(grades3)

#dataFrame D And F are capitalized
# # print(type(grades) #<class 'pandas.core.series.Series'>
# print(grades)


 # creating a series from a range of values
# hundreds=pd.Series(100,range(10))
# print(hundreds)
