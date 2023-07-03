import pandas as pd

dati=pd.read_csv('persone.csv',delimiter=';')

print("METODO DESCRIBE -> describe.()")
print(dati)
#Da informazioni sui valori numerici per ogni colonna
print(dati.describe())
    #count -> conteggio valori
    #mean -> media
    #std -> deviazione standard
    #min    -> minimo
    #25%   -> 25° percentile
    #50%   -> 50 percentile
    #75%   -> 75° percentile
    #max    -> massimo
    
#salviamo i dati
statitica=dati.describe()
print("Tipo di dato di describe()")

# <class 'pandas.core.frame.DataFrame'>
print(type(statitica)) # è un DataFrame

print("Describe applicato ad una colonna -> è una Series")
print("->Altezza")
print(statitica['altezza']) # è una series


print("Estrae il solo valore massimo tutte le colonne")
print("->Peso e Altezza MAX")
print(statitica.loc['max']) # è una series
    #lo stesso vale per:
        #count -> conteggio valori
        #mean -> media
        #std -> deviazione standard
        #min    -> minimo
        #25%   -> 25° percentile
        #50%   -> 50 percentile
        #75%   -> 75° percentile
        #max    -> massimo

print("Estrae il solo valore massimo di una colonna")
print("->Peso MAX")
print(statitica.loc['max']['peso']) # è una series

#METODI

print("METODI") #i metodi ritornano i dati richiesti per salvarli altrove
#count() -> conteggio valori
#mean() -> media
#std() -> deviazione standard
#min()    -> minimo
#25%()   -> 25° percentile
#50%()   -> 50 percentile
#75%()   -> 75° percentile
#max()    -> massimo
#cumsum() -> somma comulativa 

#Accedo al peso di dati e sommo tutti i valori
print('Media')
somma_pesi=dati.peso.sum()
conteggio=dati.peso.count()
print("Media peso : ", somma_pesi/conteggio)

print('Somma comulativa')
somma_comulativa=dati.peso.cumsum()
print(somma_comulativa)