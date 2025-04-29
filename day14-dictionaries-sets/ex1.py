#Dictionaries and Sets
#Dictionaries are used to store information(data values) in a key (collection/data structure that has a key value)
#[] gives you a list
#() gives you a tuple
#{} gives you a dictionary
student = {
"name":"Heze",
"age":21,
#how to have a list within a dictionary
"course":["python","Java","web Design","Discrete Math"],
"nationality":"Austria",
"idNo":"00001",
"telephone":"2547700090"
}

#Another way: Declaring a dictionary using a method constructor
driver=dict(name="Heze",dlClass="BCE",LicenseNo=773)
print(student["name"])
print(student["course"])
# print(driver["LicenseNo"])

#how to access an item in alist within a dictionary
# print(student["course"][1])

# to change the dictionary detail
# before
print(student)
student["name"]="Anita"
print(student)
student["java"]="pichap"
print(student)

# removing a character
del student["nationality"]
print(student)

#returning number of keys in a dictionary
print(len(student))

























































