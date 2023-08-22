#plot random x,y coordinates
import matplotlib.pyplot as plt
import random
import numpy as np
x = np.linspace(0, 10, 1000)
y = np.sin(x)
plt.plot(x,y)
plt.show()
