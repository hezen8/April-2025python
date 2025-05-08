#ACCESSING VALUES IN A DATAFRAME
#accessing a single value
import pandas as pd
grades_dict={"Hexe":[89,90,71],"Gandalf":[99,100,95],"glades":[78,85,88],"Fred":[95,92,90]}
grades_df=pd.DataFrame(grades_dict,index=["exam1","exam2","exam3"])
# print(grades_df["Hexe"])

#FOR MULTIPLE VALUES
#accessing multiple values
# print(grades_df[["Hexe","Gandalf"]])

# #SLICING DATAFRAMES
# print(grades_df.loc["exam2":"exam3"])
# print(grades_df.iloc[0:2])

# #accessing a particular value in a dataframe
# print(grades_df.at["exam1","Hexe"])
# print(grades_df.iat[0,0])
# #or
# print(grades_df.iloc[0,0])

# print(grades_df.loc["exam1":"exam3","Hexe":"glades"])
# print(grades_df.iloc[0:3,0:2])

#explaining greater than and less than
# print(grades_df[grades_df>90])#get grades greater than 90
# print(grades_df[grades_df<90])#get grades less than 90
# print(grades_df[(grades_df<90) & (grades_df>80)])#btn 80 or above but less than 90
# print(grades_df.mean())
# for specifing a column
# print(grades_df["Hexe"].mean())#mean of hexe
# print(grades_df.describe())#mean, std, min, max, 25%, 50%, 75% of all columns
# #including all columns
# print(grades_df.describe(include="all"))#mean, std, min, max, 25%, 50%, 75% of all columns including all columns
# #including all columns and all data types
# print(grades_df.describe(include="all",datetime_is_numeric=True))#mean, std, min, max, 25%, 50%, 75% of all columns including all columns and all data types
# print(grades_df.mean(axis=1))#mean of all columns for each row
# print(grades_df.mean(axis=0))#mean of all rows for each column

#sorting values in a dataframe according to the index
print(grades_df.sort_index(ascending=True))#sort index in ascending order
print(grades_df.sort_index(ascending=False))#sort index in descending order







