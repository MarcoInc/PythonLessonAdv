import numpy as np
import matplotlib.pyplot as matplot

#COVARIANZA -> valore numerico che indica 
# quanto due variabili varino insieme
    #valuta la dipendenza
x=np.array([5,10,5,10])
y=np.array([4,9,4,9])
#Covarianza = 1 -> discostano di 1

matplot.plot(x)
matplot.plot(y)
matplot.show()

#Matrice di covariaza -> cov(x,y)
    # una matrice C SIMMETRICA 2x2 in cui 
        #diagonale principale -> covarianza di x con se stessa
        #Valore C(ij) -> covarianza tra x e y -> in basso a destra
print("MATRICE DI COVARIANZA -> cov(x,y)")        
print(np.cov(x,y))
