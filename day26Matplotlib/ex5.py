import matplotlib.pyplot as plt
import numpy as np
w=np.array([10,25,35,45,15])
fruits=['apple','banana','orange','grape','kiwi']
plt.pie(w, labels=['jane','Brian','Caleb','Denis','Esther'],startangle=90,shadow=False)
plt.legend(fruits)
plt.show()