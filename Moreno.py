import numpy as np
import matplotlib 
matplotlib.use('Agg')

import numpy as np
import matplotlib.pyplot as plt # this is the only line required to make plots with matplotlibt



x=np.linspace(-np.pi*4, np.pi*4, 1000)

plt.plot(x, np.sin(x))
plt.xlabel("x") 
plt.ylabel("sin(x)") 
plt.title("Seno") 


plt.savefig("funcion.png") 