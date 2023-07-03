import matplotlib.pyplot as matplot
import numpy as np
import random as rnd #rnd è un alias

print('Subplots -> subplots')

#genera dei valori per le ascisse da 0 a 2 con step 0.01
    #0.0, 0.01,0.02......2.0
x=np.arange(0.0,2.0,0.01)

#il nostro riquadro sarà 2x3
fig, grafico=matplot.subplots(2,2)
#TUTTI I GRAFICI ALLE COORDINATE
    #grafico lineare
        #set_title-> etichetta 
grafico[0,0].plot(x,x)
grafico[0,0].set_title('Axis [0,0]')

    #parabola x^2
grafico[0,1].plot(x,x**2)
grafico[0,1].set_title('Axis [0,1]')

    #parabola x^3
grafico[1,0].plot(x,x**3)
grafico[1,0].set_title('Axis [1,0]')

    #parabola x^4
grafico[1,1].plot(x,x**4)
grafico[1,1].set_title('Axis [1,1]')

#mostra le etichette in ogni grafico
    #in questo caso solo nel primo rigo
for ax in grafico.flat:
    ax.set(xlabel='x-label',ylabel='y-label')
    
#Risolve il problema delle etichette sovrapposte ai grafici sottostanti
for ax in grafico.flat:
    ax.label_outer()
matplot.show()
