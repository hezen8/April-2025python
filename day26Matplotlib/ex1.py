# a low level plot library
import matplotlib.pyplot as plt
import numpy as np

xpoint=np.array([0,2,4,6,8])
ypoint=np.array([3,7,0,12,14])

xpoint1=np.array([0,1,6,7,10])
ypoint1=np.array([6,10,3,15,17])
plt.plot(xpoint,ypoint,marker="o")
# plt.plot(xpoint,ypoint,'ro') # red 
plt.plot(xpoint1,ypoint1,":",marker="x")#dotted line
# plt.plot(xpoint,ypoint,"g--")#green dashed 

#


plt.show()