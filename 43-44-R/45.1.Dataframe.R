#Dataframe sono come le tabelle utilizzate per raccogliere informazioni
# in merito a determinate variabili osservate su n osservazioni:
  #variabili disposte in colonna
  #osservazioni disposte in riga -> ogni singolo individuo

#Partiamo dai seguenti vettori
anni=c(30,27,24)
sposato=c(TRUE,FALSE,FALSE)
regione=c("Piemonte","Lazio","LIguria")
risultato=c("Ottimo","Insufficente","Sufficente")

#Creiamo il dataframe basato sui dati del vettore
test=data.frame(anni,sposato,regione,risultato)
test

#Per vedere i dati nell'AREA DEGLI SCRIPT -> equivalenti
  #* Doppio click nel dataframe nel WORKSPACE
  #* Usando la seguente funzione
View(test)

#Visionare le principali statistiche in base al tipo di variabile
summary(test)
  #variabile numerica -> statistiche descrittive(max,min,mediana,media,quartili)
  #variabile logica -> frequenze assolute di ciascuna

#Analizzare la struttura del dataframe -> simili
  #*Click nella freccia blu nel dataframe -> output nella finestra
  #* Usando la seguente funzione -> output area Console
str(test)
  #quante variabili
  #tipo di variabile
  #valore variabile

#Selezionare una singola colonna
  #In test seleziona la colonna anni
test$anni
test$anni%>%class() #"numeric"
 

#Rendiamo una colonna un VETTORE FATTORIALE
test$regione=factor(test$regione)
  #tutta la colonna adesso è un VETTORE FATTORILE
test$regione %>% class() #factor
#Il tipo dei dati all'interno
regione %>% class() #"character"

