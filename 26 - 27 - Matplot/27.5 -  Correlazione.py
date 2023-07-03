import numpy as np
import matplotlib.pyplot as matplot

x=np.array([5,10,5,10])
y=np.array([4,9,4,9])
#CORRELAZIONE
    # relazione tra due variabili affinchè un valore 
    # della prima corrisponda ad un valore della seconda
    #tiene conto delle SCOSTAMENTI DALLA MEDIA 
#INDICE DI CORRELAZIONE -> grado di correlazione tra due variabili
    #valore tra -1 e 1 in cui
        # -1 -> Correlazione INDIRETTA o INVERSA
            #Se aumenta uno diminuisce l'altra
        # 1 -> Correlazione DIRETTA o POSITIVA
            #Se aumenta uno aumenta pure l'altra
        # 0 -> Non vi è correlazione
        # valore nullo -> non implica indipendeza

#Matrice di correlazione -> corrcoef(x,y)
    # una matrice SIMMETRICA R 2x2 in cui 
        #diagonale principale -> correlazione di x con se stessa
        #Valore R(ij) -> correlazione tra x e y -> in basso a destra
print("MATRICE DI CORRELAZIONE -> corrcoef(x,y)")        
print(np.corrcoef(x,y))
    
