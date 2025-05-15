#creating a bargraph
import matplotlib.pyplot as plt
import numpy as np
x=np.array(["Jan","Feb","Mar","Apr","May"])
y=np.array([100,800,200,700,500])
plt.bar(x,y)
plt.show()