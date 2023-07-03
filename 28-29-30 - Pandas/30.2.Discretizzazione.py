import pandas as pd
import numpy as np

#DISCRETIZZAZIONE
    #Una variabile continua in una discreta
        #Utile per creare istogrammi

# cut(x,y)
    # suddivide il primo parametri (array o serie) in più categorie/bins semi aperte (ESCLUSO....INCLUSO]
    # secondo parametro il numero di categorie/bins equamente spaziate
        #oppure una lista di valori estremi alle categorie/bins

#Crea una distribuzione uniforme di 20 numeri random da 0 a 100
numeri=np.random.uniform(0,100,20)
serie=pd.Series(numeri)

print("CUT")
#Divido la serie in 4 categorie in termini di ampiezza
    #head(7) -> seleziona le prime 7 categorie
categorie=pd.cut(serie,4).head(7)
print(categorie)

print("CUT + LABELS=(....)")
#Divido la serie in 3 categorie
    #labels= -> specifico delle categorie
categorie=pd.cut(serie,3,labels=('Basso','Medio','Alto')).head(7)
print(categorie)
#mostra le cagorie invece degli intervalli

print("CUT + LABELS=False")
#Divido la serie in 3 categorie
    #labels=False -> mette dei numeri in labels
categorie=pd.cut(serie,3,labels=False).head(7)
print(categorie)
#mostra le dei numeri invece degli intervalli

print("QCUT")
#Divido la serie in 3 categorie in termini di quantili 
# e non di ampiezza delle categorie
categorie_quantili=pd.qcut(serie,3,labels=('Basso','Medio','Alto')).head(7)
print(categorie_quantili)