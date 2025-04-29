student = {
"name":"Heze",
"age":21,
"course":["python","Java","web Design","Discrete Math"],
"nationality":"Austria",
"idNo":"00001",
"telephone":"2547700090"
}
#obtaining both values en keys
# for x in student():
#     print(x,student[x])

#obtaining  keys
# for x in student.keys():
#     print(x)

#obtaining   values
# for x in student.values():
#     print(x)

for key,value in student.items():
    print(f" {key} \t {value}")