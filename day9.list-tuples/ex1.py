#creating a list of values
zeros=[0]*10
print(zeros)

rangeList=list(range(1,11))
print(rangeList)

rangeList2=list(range(100,95,-1))
print(rangeList2)

rangeList1=list(range(10,0,-1))
print(rangeList1)
x=len(rangeList) # length of a list or number of elements or items

# how to copy  a list
#list is an object referrence variable
eastafricaCountries=["Kenya","Uganda","Tanzania","Somalia","Rwanda","Burundi"]
for eastarficaCountry in eastafricaCountries:
    print(eastarficaCountry)
    countries2=eastafricaCountries #does not create a copy of the list, but point to the same list
print(countries2)

copyCountries=eastafricaCountries.copy()
eastafricaCountries.remove("Burundi")
print(eastafricaCountries)
print(copyCountries)

# other way of copying a list
copyCountries2=[]+eastafricaCountries

#3rd way of copying a list
copyCountries3=[]
copyCountries3.extend(eastafricaCountries)

