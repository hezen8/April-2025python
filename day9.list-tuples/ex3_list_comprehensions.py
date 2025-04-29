prices=[100,300,70,678,500]

# newPrices=[]#should have 10% increment of price
# for price in prices:
#     np=price*1.1
#     newPrices.append(np)

#SHORTEST WAY
#generating a lis from older list
newPrices= [price *1.1 for price in prices]

print("oldprices" + str(prices))
print( "Newprices"+ str(newPrices))

numbers= [1,2,3,4,5,6,7,8,9,10]
sqofNumbers=[ number*number for number in numbers]
evennumber=[ number for number in numbers if number % 2 == 0]
oddnumber=[number for number in numbers if number % 2 != 0]
print(evennumber)
print(oddnumber)
print(numbers)
print(sqofNumbers)

