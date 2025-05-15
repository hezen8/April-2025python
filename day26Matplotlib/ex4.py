#creating a histogram
import matplotlib.pyplot as plt
import numpy as np
x=np.array([1,2,3,4,5,6,7,8,9,10])
y=np.array([100,800,200,250,400,340,500,600,700,800])
plt.hist(x, bins=10, color='red', alpha=0.5, edgecolor='magenta')
plt.hist(y,bins=10, color='blue', alpha=0.5, edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')    
plt.grid(axis='y', alpha=0.75)

plt.show()

