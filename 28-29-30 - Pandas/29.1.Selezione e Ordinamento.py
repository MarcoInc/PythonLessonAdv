import pandas as pd

data_file=pd.read_csv('29.persone.csv',delimiter=';')

print('SELEZIONE')
#Selezione in base a delle condizioni
print('Tutti gli uomini')
#Seleziona tutte le righe del DataFrame data_file
# in cui il campo sesso è uguale a M
print(data_file[data_file['sesso']=='M'])

print('Chi peza >70')
#Seleziono chi pesa più di 70
print(data_file[data_file['peso']>70])

print('Tutte le donne più alte di 1.7')
#Seleziono tutte le donne alte più di 1.7
data_file2=data_file[(data_file['sesso']=='F') & (data_file['altezza']>1.7)] 
print(data_file2)

#Seleziono uomini che hanno cognome Verdi o Rossi
data_file3=data_file[((data_file['cognome']=='Verdi') | (data_file['cognome']=='Rossi'))
                    & (data_file['sesso']=='M')] 
print(data_file3)

print('ORDINAMENTO')
#Ordinare in base a dei criteri
#sort_index() -> ordina in modo crescente in base agli indici
        #ascending= False -> decrescente
        
print('Per indice -> .sort_index')
ordinati_index=data_file.sort_index
print(ordinati_index)

print('Per indice -> .sort_values(by=\'campo\')')
#sort_values() -> ordina in modo crescente 
# in base ai valori di una o più colonne
    #ascending= False -> decrescente
ordinati_value=data_file.sort_values(by='nome')
print(ordinati_value)