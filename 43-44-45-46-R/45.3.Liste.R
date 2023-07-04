#Lista -> aggregazione di oggetti di R di diversa natura (vettori,matrici,dataframe..)
# Contenitore di oggetti diversi

#VETTORE
ore_lavoro=c(8,8,8,4,8)
settimana=c("Lun","Mar","Mer","Giov","Ven")
names(ore_lavoro)=settimana
ore_lavoro

#MATRICE
matrice=matrix(c(1,2,3,4),
               nrow=2,
               ncol=2, #superfluo
               byrow=TRUE)
matrice

#DATAFRAME
anni=c(30,27,24)
sposato=c(TRUE,FALSE,FALSE)
regione=c("Piemonte","Lazio","LIguria")
risultato=c("Ottimo","Insufficente","Sufficente")
#Creiamo il dataframe basato sui dati del vettore
test=data.frame(anni,sposato,regione,risultato)
#Cambiare il nome delle righe -> da indici a Nomi 
rownames(test)=c("Anna","Paolo","Luca")
test=mutate(test,id=c(1,2,3)) 
test=mutate(test,id_2=c(10,20,30)) 
test

#LISTA -> ogni elemento avrà un indice numerico
mia_lista=list(ore_lavoro,matrice,test)
mia_lista

#Rinominare oggetti della lista
    #ogni elemento avrà il suo nome e non un numero indice
mia_lista=list(primo_elemento=ore_lavoro,
                secondo_elemento=matrice,
                terzo_elemento=test)
mia_lista

#STRUTTURA LISTA
str(mia_lista)
  #quanti elementi ho
  #nomi degli elementi
  #struttura interna degli elementi

#ESTRAZIONE ELEMENTI
  # Metodo usando il nome dell'elemento $
mia_lista$primo_elemento
  # Metodo usando l'indice dell'elemento [ [ ] ]
mia_lista[[1]] #doppia [[]] -> elemento della lista
               #singola [ ] -> sottolista -> elemento di una lista

mia_lista[[1]] %>% class() #"numeric" <- il primo elemento è un vettore numeric

mia_lista[1] #singole [] -> seleziono una parte della lista
mia_lista[1] %>% class() # "list"

#Selezionare elemento di un sottoelemento
#della lista primo_elemento seleziono il secondo elemento
mia_lista[['primo_elemento']][2] #singola -> [ ]

#Eseguire operazioni tipiche sull'vettore estratto
mia_lista[[1]] %>% sum() 

#DARA' ERRORE -> error in sum -> è una lista! non è un vettore
mia_lista[1] %>% sum()#singole [ ]

#AGGIUNGERE ELEMENTO
speed=c("lento","superveloce","veloce","veloce","normale","normale")

#Il quarto elemento conterrà il vettore speed -> characters
mia_lista[[4]]=speed # doppie [ [ ] ]
#Rinominiamo il l'etichetta del quarto elemento
names(mia_lista)[4]="quarto_elemento"
mia_lista

#in alternativa con $
ore_full=ore_lavoro>4 #vettore booleano
#il quinto_elemento conterrà il vettore booleano
mia_lista$quinto_elemento=ore_full
mia_lista

#ELIMINARE OGGETTO
mia_lista[[5]]=NULL #elimino il quinto elemento
mia_lista

#CREARE VETTORE CONTENENTE TUTTI GLI OGGETTI NELLA LISTA
vettore=unlist(mia_lista)
vettore
class(vettore) #"character"





