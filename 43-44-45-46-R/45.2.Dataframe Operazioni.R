anni=c(30,27,24)
sposato=c(TRUE,FALSE,FALSE)
regione=c("Piemonte","Lazio","LIguria")
risultato=c("Ottimo","Insufficente","Sufficente")

#Creiamo il dataframe basato sui dati del vettore
test=data.frame(anni,sposato,regione,risultato)
test

#Cambiare il nome delle righe -> da indici a Nomi 
rownames(test)=c("Anna","Paolo","Luca")
test

#Creare una nuova colonna -> nuova variabile (a destra)
test$id=c(1,2,3) #SCRIVE NEL DATAFRAME
  #oppure usando la libreria dplyr -> mutate
#NON SCRIVE SUL DATAFRAME 
mutate(test,id_2=c(10,20,30)) # lo mostra solamente con una colonna in più
test
  #per vedere i risulati con mutate
test=mutate(test,id_2=c(10,20,30)) 
test

#Mostrare le PRIME osservazioni/righe
head(test, n=2) #prime 2

#Mostrare le ULTIME osservazioni/righe
tail(test, n=1) #ultima

#Dimensioni del dataframe -> # righe e colonne
dim(test) #3 righe e 6 colonne

#Numero di righe [1]
dim(test)[1]
  #oppure
nrow(test)

#Numero di colonne [2]
dim(test)[2]
  #oppure
length(test)


#INDEXING nei dataframe
  #SELEZIONE COLONNA
    #Metodo con NUMERO DI COLONNA
test[,3] #seleziona la sola colonna 3
    #Metodo con NOME DELLA COLONNA
test[,"regione"] #seleziona la sola colonna "regione"
    #Metodo con $ già visto
test$regione

  #SELEZIONE RIGHE
    #Metodo con NUMERO DI RIGA
test[2,] #seleziona la sola riga 2
    #Metodo con NOME DELLA RIGA
test["Paolo",] #seleziona la sola riga "Paolo"
  
  #INDEXING BOOLEANO
sposato
test[sposato,] #seleziona solo dove sposato sta a TRUE

#Sottoinsiemi di osservazioni su una determinata variabile
subset(test,risultato!='Insufficente') #solo chi non è "Insufficente"
#in alternativa solo chi è Ottimo o Sufficente
subset(test,risultato %in% c("Ottimo","Sufficente")) # -> %in% -> uguaglianza


#Ordinare un dataframe
arrange(test,anni) #ordinatest per anni

#Modificare il valore di un particolare livello di una variabile
  #1. trasformiamo risultato in characters
test$risulato=as.character(test$risultato) 
  #2. Indexing booleano cercando dove sta Ottimo
index_ottimo=which(test$risulato == "Ottimo")
index_ottimo #indice degli Ottimo
  #Scriviamo negli gli indici dove sta ottimo, e nella 4 colonna
  # il valore di Buono
test[index_ottimo,4]="Buono"
test

#Eliminare una colonna
test$regione=NULL #elimina la colonna regione
#oppure
test=test[,-2] #eliminata la seconda colonna -> sposato
test



