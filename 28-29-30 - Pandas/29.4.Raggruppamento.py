import pandas as pd
import numpy as np


dati=pd.read_csv('persone.csv',delimiter=';')

#GROUP BY di SQL -> raggruppa i dati
print("GROUP BY - GROUPS")

gruppi=dati.groupby('sesso').groups 
    #groupby -> raggruppa -> Ritorna un DIZIONARIO
    #groups -> proprietà che contiene i gruppi
print(gruppi) #stampa un dizionario

print('->Indici di un gruppo specifico -> groupby(\'COL\').groups[\'DATO\']')
#Cerca le F nella colonna sesso e ritorna indici
gruppi_F=dati.groupby('sesso').groups['F']
print(gruppi_F) #stampa gli indici e tipo dei dati

print('->Singoli indici -> groupby(\'COL\').groups[\'DATO\'][INDICE]')
#Dammi il primo [0] tra tutti gli F in sesso
gruppi_F_index=dati.groupby('sesso').groups['F'][0]
print("Indice: ",gruppi_F_index) #stampa gli indici e tipo dei dati
    #ogni singolo elemento è un indice
print("Dato: \n",dati.loc[0]) #stampo il singolo dati all'indice


print('->Scorrere un FOR per INDICE')
gruppi_F=dati.groupby('sesso').groups['F']
for i in gruppi_F: #scorre indice per indice tra tutti gli F in sesso
    print("Indice: ",i) #stampa gli indici
    print("Dato: \n",dati.loc[i]) #stampo il singolo dati all'indice

print('->Scorrere un FOR per CHIAVE')
gruppi_F=dati.groupby('sesso').groups['F']

#Scorre per chiave -> sesso e di ciascuno stampa i risultati per chiave
for chiave,elementi in dati.groupby('sesso'):  #itera per ogni gruppo
    print("Chiave: ",chiave) #stampa la chiave del gruppo
    print(elementi) #stampa i dati che corrispondono alla chiave 
    print()
    
print('->Accesso ad un singolo gruppo tra tanti -> get_group(\'COL\')')
gruppi_F_dati=dati.groupby('sesso').get_group('F') 
#ritorna i dati
    #diverso da gruppi_F=dati.groupby('sesso').groups['F'] -> ritorna gli indci
print(gruppi_F_dati)

print('AGGREGAZIONE -> groupby.FUNZIONE')
#1. Aggreggare per fare operazioni sui singoli gruppi
    #si mette la funzionalità dopo groupby().
    
print('FUNZIONI STANDARD')
#Funzionalità standard
    #media,somma,statistiche, size...
    
#Raggruppa per sesso e si ogni singolo gruppo dammi la dimensione
gruppi_size=dati.groupby('sesso').size()
#size() -> ritorna la dimensione di ogni gruppo
print("Dimensione gruppi -> size()")
print(gruppi_size)

#Raggruppa per sesso e si ogni singolo gruppo fai la media dell'altezza
gruppi_mean=dati.groupby('sesso')['altezza'].mean()
#mean() -> ritorna la media di ogni gruppo selezionato
print("Raggruppa per (sesso) -> groupby() e media->mean()")
print("Media [altezza]: \n",gruppi_mean)

#Raggruppa per sesso e fammi la describe in base all'altezza
gruppi_describe=dati.groupby('sesso')['altezza'].describe()
#describe() -> ritorna la describe
print("Describe di [altezza] dei gruppi (sesso) ->describe()")
print("Describe di [altezza]: \n",gruppi_describe)

print('FUNZIONI NON STANDARD -> agg()')
#Funzionalità non standard
    #prese da NumPy
    #funzionalità custom -> lambda
    
print('Funzioni NumPy-> \\.agg([np...])')
#Raggruppa per (sesso) e dell'[altezza] calcola min e max con NumPy
gruppi_agg=dati.groupby('sesso')['altezza'].agg([np.min,np.max])
print("np.min e np.max dell' [altezza] per ogni (sesso)")

print(gruppi_agg)


print('Funzioni custom Lambda-> \\.agg([np...])')
#Raggruppa per sesso e del peso esegue una funzione lambda
gruppi_custom=dati.groupby('sesso')['peso']\
    .agg([lambda x: np.max(x)-np.min(x)]) #ritorna la differenza tra max e min
print("Differenza tra np.min e np.max dell' [altezza] per ogni (sesso)")
print(gruppi_custom)
