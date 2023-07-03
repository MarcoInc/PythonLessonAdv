#SERIES -> Parte di un DataFrame a cui abbiamo estratto dei campi tramite:
    # un campo
    # slicing
#Da altre strutture python quali:
    #liste
    #dizionario
    #array di NumPy
import numpy as np
import pandas as pd

print("LETTURA FILE CSV -> pd.read_csv(...)")
data_file=pd.read_csv('persone.csv',delimiter=';')

print("MOSTRO IL FILE CSV ")
print(type(data_file))
print(data_file)

print("SERIES TRAMITE UN CAMPO")
#Campi estratti da un data frame
data_file_cognome=data_file['cognome']
print(type(data_file_cognome))
print(data_file_cognome)

print("SERIES TRAMITE SLICING -> gli indici sanno gli stessi della dataframe")
#loc e iloc accedono ad una data etichetta/posizione di un dato campo
print("-> iloc")  #indice
print(data_file.iloc[2])
print("-> loc") #etichetta
print(data_file.loc[2])

print("INDICI -> index")
print(data_file.index)
    #start-> da dove parte
    #stop -> dove finisce
    #step=1 -> scorre 1 per 1
print("-->Lista indici a lista ->list()" )
lista_indici=list(data_file.index)
print(lista_indici)


print("SLICING + INDEXING" )
data_file_altezza=data_file['altezza']
print(data_file_altezza)

print("->Posizione 0 -> [0] " )
print(data_file_altezza[0])

print("->Fino alla 2(esclusa) -> [:2] " )
print(data_file_altezza[:2])

print("->Dalla 2(inclusa) -> [2:] " )
print(data_file_altezza[2:])

print("->Dalla 1(inclusa) alla 4(esclusa)-> [1:4] " )
print(data_file_altezza[1:4])
print("->Le 0,2,3 [[0,2,3]]" )
print(data_file_altezza[[0,2,3]]) #doppie [[]] perchè sono più dati

print("DA LISTA A SERIES -> pd.Series(data=[...,...,...])" )
#è possibile ottenere una Series dalle liste
capitali_da_lista=pd.Series(data=['Roma','Parigi','Madrid'])
print(capitali_da_lista)
#i dati avranno le loro etichette/indici

print("DA DIZIONARIO A SERIES -> pd.Series(data=[CHIAVE:VALORE...])" )
#è possibile ottenere una Series dalle liste
capitali_da_dizionario=pd.Series(data=['Italia:Roma','Francia:Parigi','Spagna:Madrid'])
print(capitali_da_dizionario)
#i dati avranno le loro etichette/indici

print("DA ARRAY NUMPY A SERIES -> pd.Series(ARRAY)" )
#è possibile ottenere una Series dalle liste
array_capitali=np.array(['Roma','Parigi','Madrid'])

capitali_da_array=pd.Series(array_capitali)
print(capitali_da_array)
#i dati avranno le loro etichette/indici

