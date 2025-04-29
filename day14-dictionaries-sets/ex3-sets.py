#Set 
# A collection of unique and unorded elements
# Does not allow reputation/duplication
fruits={"oranges","lemons","apples"} #1st way
fruits2=set(["avocados","pineapples","lemons"])#2nd way
fruits3=set([])#creates an empty set
#combine
fruits3=fruits.union(fruits2) 
print(fruits3)
fruits4=set([])
fruits4=fruits.intersection(fruits2)
print(fruits4)
# mySet=set(["abc"])
# print(mySet)
# print(type(fruits))
# print(type(fruits2))