f=open('employees.txt','w')

for counter in range(1,6):
    name=input("Employees name #{counter}")
    f.write(name+"\n")

f.close()