# lambda arguments:expression

def tripler(n):#ordinary named function
    return n*3
print(tripler(20))

tripler2=lambda x:x*3
print(tripler2(20))

print((lambda x:x*3)(25))
print((lambda y:y**3)(3))
print((lambda x:x+5)(10))
print((lambda x:x*x)(10))

