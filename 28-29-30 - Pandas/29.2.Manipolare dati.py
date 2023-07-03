import pandas as pd

# data_file=pd.read_csv('persone.csv',delimiter=';')

print('DATA FRAME DI PARTENZA')
#Creiamo un DataFrame usando una lista
    #data=[...] -> campi singoli
    #culumns=[...] -> nome colonne
    #index = [...] -> etichette personalizzate al posto di numeri
dati=pd.DataFrame(data=[['Luca',28,'Milano'],
                ['Alessia',22,'Venezia'],
                ['Filippo',21,'Bari'],
                ['Silvia',30,'Messina']],
                columns=['nome','eta','citta'])
print(dati)

print('MODIFICA RIGA')
#MODIFICA
print('->Riga 1 -> loc[1] <- ETICHETTA')
dati.loc[1]=['Paola',25,'Genova']
print(dati)
print('->Ultima riga -> iloc[-1] <- INDICE/POSIZIONE')
dati.iloc[-1]=['Pippo',27,'Catania']
print(dati)

print('-> Aggiunta riga se l\'etichetta non fosse presente -> loc[...]')
#Se usato loc su una etichetta non presente, la riga viene aggiunta
# con l'etichetta usata
dati.loc[10]=['Caterina',51,'Pisa']
print(dati)

print('INFO INDICI')
indice_max=dati.index.max()
print("->Indice del valore massimo : ",indice_max)

dati.loc[5]=['Marta',33,'Firenze']
print("->Inserito dato all'etichetta 5")
print(dati)
indice_ultimo_inserito=dati.index[-1]
print("->Ultimo indice inserito : ",indice_ultimo_inserito)

print('ELIMINAZIONE -> drop(axis=1 o 0)')
# drop() elimina un dato e ritorna un nuovo DataFrame
    #se axis=0 -> elimina una RIGA
    #se axis=1 -> elimina una COLONNA
print('-> Per ETICHETTA')
print('-->Eliminata RIGA etichettata 10')
dati_etichetta_eliminata=dati.drop(10, axis=0)
print(dati_etichetta_eliminata)

print('-->Eliminata COLONNA etichettata \'citta\'')
dati_colonna_eliminata=dati.drop('citta', axis=1)
print(dati_colonna_eliminata)

print('-> Per INDICE')
print('-->Eliminata ultima riga -> Posizione [-1]')
dati_lastRiga_eliminata=dati.drop(dati.index[-1])
print(dati_lastRiga_eliminata)

print('CONCATENARE DUE DATAFRAME -> concat([df1,df2])')
# concat()
    # RESET DEGLI INDICI
        # drop=True impedisce indici doppi
print('DataFrame 1')
dati1=pd.DataFrame(data=[['Luca',28,'Milano'],
                ['Alessia',22,'Venezia'],
                ['Filippo',21,'Bari'],
                ['Silvia',30,'Messina']],
                columns=['nome','eta','citta'])
print(dati1)

print('DataFrame 2')
dati2=pd.DataFrame(data=[['Matteo',15,'Torino'],
                ['Piero',20,'Palermo'],
                ['Martina',25,'Vicenza'],
                ['Alessandro',33,'Trapani']],
                columns=['nome','eta','citta'])
print(dati2)
print('DataFrame 1 + DataFrame 2')
dati_concatenati=pd.concat([dati1,dati2]).reset_index(drop=True)
    # drop=True -> reset indici
print(dati_concatenati)

print('ESPLORARE DATAFRAME -> .iteritem() e .iterrow()')
#Si può iterare per:
    #indice -> iloc
    #etichetta -> loc
print("Per indice di colonna -> .iteritems()") #iteritems DEPRECATO ->items NUOVO
#Scorre una sola colonna
for i,v in dati.iteritems():
    #i -> indice nome campo ->colonna
    #v -> valore del campo
    if i=='nome':  #Scorre la colonna nome
            print(v)   #Stampa i soli nomi 

print("Per indice di riga -> .iterrows()")
for i,v in dati.iterrows():
    print("All'indice ",i," -> Nome : ",v.nome," ->Città : ",v.citta)
