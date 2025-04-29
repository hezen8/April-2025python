from random import randint
randomNums=int(input("Enter the number of random numbers"))

try:
    f=open("random numbers.txt","w")
except:
    print("An error occured")


for counter in range(1,randomNums+1):
    num=randint(1,501)
    f.write(str(num)+"\n")
 
