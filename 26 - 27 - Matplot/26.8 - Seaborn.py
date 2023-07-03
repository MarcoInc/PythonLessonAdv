import matplotlib.pyplot as matplot
import numpy as np
import random as rnd #rnd è un alias
#Seaborn permette di rendere di migliorare la grafica
import seaborn as sb

sb.set()
x=np.random.rand(100)
#dispolot -> instogramma
#kde -> funzione di disploit per calcolare....densità kernel..
sb.displot(data=x, kde=True)

matplot.show()
