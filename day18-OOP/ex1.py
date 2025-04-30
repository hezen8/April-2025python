#fields/attributes/properties
#class defines how an object is going to look like (always start with a capital letter when naming a class)
#An object is true representation of a class (every object must have an operator)
#method  a special function related to a particular class
# Function an inbult sub-program
# procees of creating an object from a class is called (instanciation)
#How one defines a class
class Account:
    pass

acc1=Account()
acc2=Account()
acc1.name="John"
acc1.bal=4000
acc2.name="heze"
acc2.bal=90000
print(type(acc1))
print(acc1)
print(acc1.bal)
