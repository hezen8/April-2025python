import pandas as pd
#creating a DataFrame from a dictionary
grades_dict={"Hexe":[89,90,71],"Gandalf":[99,100,95],"glades":[78,85,88],"Fred":[95,92,90]}
grades_df=pd.DataFrame(grades_dict,index=["exam1","exam2","exam3"])
#Or
# grades_df.index=["exam1","exam2","exam3"]
# print(grades_df)

#creating a DataFrame from a list of lists
gradesDf=pd.DataFrame([[89,90,71],[99,100,95],[78,85,88],[95,92,90]],columns=["exam1","exam2","exam3"],index=["hexe","Gandalf","glades","Fred"])
# print(gradesDf)
#creating a DataFrame from a list of dictionaries

#how to transpose a DataFrame
gradesDF3=pd.DataFrame(gradesDf.T)
print(gradesDF3)

#ACCESSING VALUES IN A DATAFRAME
#accessing a single value



