ore_lavoro=c(8,8,8,4,8)
settimana=c("Lun","Mar","Mer","Giov","Ven")
names(ore_lavoro)=settimana

#ADDIZIONE DI UNA COSTANTE ad un vettore
  #a ciascun elemento somma 10
c(1,2,3,4,5)+10 

#MOLTIPLICAZIONE DI UNA COSTANTE ad un vettore
  #a ciascun elemento moltiplico 10
c(1,2,3,4,5)*10

#SOTTRAZIONE TRA VETTORI
  #sottraggo ogni elemento corrispondente
c(1,2,3) -c(4,5,6) #i  vettori devono avere la stessa lunghezza

#PRODOTTO INTERNO -> moltoplicazione tra due vettori
  #moltiplico ogni elemento corrispondente
c(1,2,3)*c(4,5,6) #i vettori devono avere la stessa lunghezza

#ELEVAZIONE A POTENZA
  #1°Metodo 
2^3
  #2°Metodo
2**3 
    #Elevamento a potenza di un vettore con un altro vettore
    # Elevo ogni elemento corrispondente
c(2,3)**c(4,3) #i vettori devono avere la stessa lunghezza
  
#QUOZIENTE
  #Con parte decimale
22/3
  #Intera senza resto
22%/%3

#MODULO -> resto
22%%3

#SEQUENZA NUMERI
  #da 0 a 10 con passo 1
1:10 
  #Con passo custom
seq(from=0, to=10,by=2) #da 0 a 10 con passo 2 a 2
  #Senza specificiare from e to
seq(0,10,2)

#RIPETERE UN OGGETTO 
  #vettore
rep(12,times=3) #12 per 3 volte
  #oggetto
rep(ore_lavoro,times=3) #oggetto per 3 volte
#Ripetere anche gli elementi dentro un vettore
rep(c(1,2,3),each=2,times=3) #ripeti i singoli per 2 e poi per 3

#LUNGHEZZA VETTORE -> quanti elementi ci sono?
length(c(1,2,3,4,5))
#Nei dataframe length -> colonne

#COMPORRE UN NUOVO VETTORE USANDO VETTORI GIA' PREESISTENTI
numeri=c(1,2,3,4,5)
#inserisce il 6 nel mezzo tra sottovettore[1:3] e [4:5]
nuovi_numeri=c(numeri[1:3],6, numeri[4:5])#[1:3] 6 [4:5]
nuovi_numeri

#INCOLLARE GLI ELEMENTI DI UN VETTORE IN UNA STRINGA
  #specifichiamo un separatore tra un elemento e l'altro
paste(nuovi_numeri,collapse = "//") #ritorna una stringa

#INVERTIRE I VALORI LOGICI
valori=c(TRUE,FALSE,TRUE) #Da TRUE -> FALSE e da FALSE -> TRUE
!valori
valori

#SOMMARE TUTTI GLI ELEMENTI DI UN VETTORE BOOLEANO
valori %>% sum() #numeric -> 1+0+1 

#TRASFORMARE UN VETTORE LOGICAL ad/da UN VETTORE NUMERICO
as.numeric(valori)  #TRUE -> 1 , FALSE -> 0
  #viceversa
as.logical(c(0,1,1,1,0)) # 1 -> TRUE , 0 -> FALSE

  
  

