#DATA FRAME -> struttura bidimensionale -> tabella
    #accesso per righe e colonne
#SERIES -> Parte di DataFrame

#Utilizzeremo un file CSV
import pandas as pd

print("LETTURA FILE CSV -> pd.read_csv(...)")
#read_csv() -> Lettura di un file csv con delimitatore tra un dato e l'altro
data_file=pd.read_csv('persone.csv',delimiter=';')
print("MOSTRO IL FILE CSV ")
#TIPO -> <class 'pandas.core.frame.DataFrame'>
print(type(data_file))
print(data_file)
#ogni elemento è conteggiato da 0 in modo progressivo -> non è un indice!

print("TIPO DELLE COLONNE -> data_file.dtype")
#dtypes() -> è un ATTRIBUTO che contiene i tipi delle colonne
    #Ogni colonna avrà probabilmente tipi differenti
print(data_file.dtypes)
# il tipo object -> stringa

print("CASTING FORMATO DATA -> pd.to_datetime(...)")
#La data non è stata riconosciuta
    #Effettuiamo un casting
data_file['nascita']=pd.to_datetime(data_file['nascita'])
print(data_file.dtypes)

print("AGGIUNTA COLONNA")
#Modifichiamo le colonne con le funzioni lambda
data_file['sesso_esteso']=\
data_file['sesso'].apply(lambda x:'MASCHIO' if x=='M' else 'FEMMINA')
print(data_file)

print('ESTRARRE DATI DA UN DATAFRAME ESISTENTE -> È UNA SERIES <-SPOILER 28.2')
#creiamo un nuovo dataframe con i soli campi nome e cognome
data_file_nome_cognome=data_file[['nome','cognome']] #doppia parentesi se sono più campi
#è ancora un dataframe
print(type(data_file_nome_cognome))
print(data_file_nome_cognome)


print("ACCESSO AI DATI")
#Si usano le etichette per accedere alle singole righe e/colonne


print("Ritorna nome riga/etichetta->loc[2]")
# loc[.] ->  si può accedere all’elemento mediante la sua etichetta -> 0, 1, 2 .....
    #Se abbiamo eliminato un etichetta ci sarà l'ECCEZIONE -> KeyError perchè non la trova
print(data_file.loc[2])

print("Ritorna indice/posizione->iloc[2]")
# iloc[.] -> lavora sul conteggio della posizione/indice e non sull'etichetta -> come gli array
    #Se abbiamo eliminato un indice non ci saranno eccezzioni
        #I valori sono scalati di una posizione avendone eliminato uno
            #In posizione 2 ritorna l'elemento con Name:1
print(data_file.iloc[2])
#Name: ETICHETTA/POSIZIONE
#a parità di indice, loc e iloc ritorna lo stesso dato

print("->Ritorna il nome della riga/etichetta->index[2]")
#index -> nome etichetta del dato -> legato ad iloc
print(data_file.index[2])

print("-->Indici -> index")
#info sulla DataFrame/Series
print(data_file.index)
    #start-> da dove parte
    #stop -> dove finisce
    #step=1 -> scorre 1 per 1
print("--->Lista indici a lista -> list()" )
lista_indici=list(data_file.index)
print(lista_indici)


print("SLICING -> [.. : ..] -> È UNA SERIES <-SPOILER 28.2")
#Con lo slicing estraiamo dei sottodati tramite le loro etichette   

print("->Tramite loc -> loc[x:y] -> ESTREMI x e y INCLUSI")
#ESTREMI INCLUSI
print(data_file.loc[1:3])
        #prende dalla 1 alla 3

print("->Tramite iloc -> iloc[x:y] -> estremi x INCLUSO e y ESCLUSO <- TIPO ARRAY")
#ESTREMO x incluso ed y escluso tipo gli array
print(data_file.iloc[1:3])
    #prende dalla 1 alla 2

print("->Restringere lo slicing ad alcuni dati -> loc/iloc[x:y][['campo1','campo2']]")
print(data_file.loc[1:3][['nome','cognome']])

print("PRIME x RIGHE INZIALI -> head(x)")
print(data_file.head(2))
    #se x non è specificato stampa tutto
print("ULTIME x RIGHE FINALI -> tail(x)")
print(data_file.tail(2))
    #se x non è specificato stampa tutto


