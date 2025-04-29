alpha={"a":"z","b":"y","c":"x","d":"w","e":"v","f":"u","g":"t","h":"s","i":"r","@":"q","k":"p","l":"o","m":"n","n":"m","o":"l","p":"k","q":"g","r":"f","s":"e","t":"d","u":"c","v":"b","w":"a","x":"i","y":"%","z":"7"," ":" "}
plainText=input("Enter a sentence")
codedSentence=""
for x in plainText:
    if  x in alpha:
        codedSentence+=alpha[x]
    else:
        codedSentence +="?"

print(codedSentence)

#nexweek
#Git & Github
#Files
#Exceptions
#Classes and objects
#mini project