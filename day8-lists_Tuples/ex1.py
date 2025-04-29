#Data structures in python
#1 lists
#2 Tuples
#3 Sets
#4 Dictionaries

#1 lists can be created in two ways
#types of lists
#1 append  - add a value/character
#2 insert
#3 Delete
#4 Pop
#5 sum
#6 clear
#first way
friends=["Ann","hexe","shelly","maggy","felix","junior","Martha"]
#second way
fruits=list(("mango","oranges","bananas","grapes","guavas"))
prices=[349.0,900.0,568.9,3000.00]

# print(friends[3])
# print(fruits[2])
# print(prices[3])

for friend in friends:
    print(friend)
for fruit in fruits:
    print(fruit)

total=0 
for price in prices:
    total = total+price
    average=total/4
#first way
print(f"Total price: kshs{total:.2f}")
print(f"average price: kshs{average:.2f}")
#shortest way
print(f"Total price: kshs {sum(prices):.2f}")

#1sequence/collective/iterables(enables you to store many things at one space)
#list
#arrays
#tuples