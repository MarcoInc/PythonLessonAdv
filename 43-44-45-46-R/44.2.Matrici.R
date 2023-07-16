#Matrice -> vettore organizzato su diverse righe e colonne
#matrix( DATI , ncol=n,nrow=m) -> crea una matrice nxm
#ncol -> numero colonne
#nrow -> numero righe
#se ho le righe è superfluo indicare le colonne*-> verranno calcolate
#byrow -> ordina elementi secondo la riga se TRUE e non per colonna

#creiamo una matrice 2x2 ordinati per righe
matrice=matrix(c(1,2,3,4),
               nrow=2,
               ncol=2, #superfluo
               byrow=TRUE)
matrice

#creiamo una matrice 2x2 ordinati per colonne
matrice=matrix(c(1,2,3,4),
               nrow=2,
               byrow=FALSE)
              #ncol eliminato
matrice

#rinominare righe e colonne
  #creo due vettori con dei nomi
nomi_colonne=c("A","B")
nomi_righe=c("C","D")
#rinomino
colnames(matrice)=nomi_colonne
rownames(matrice)=nomi_righe
matrice

#somma tutti elementi righe
sommeRighe=rowSums(matrice) #ritorna un vettore
sommeRighe
#somma tutti elementi nelle colonne
sommeColonne=colSums(matrice) #ritorna un vettore
sommeColonne

#funzione pipe -> pacchetto dplyr
  #permette di concatenare diverse strighe
  #l'oggetto che precede %>% è il primo argomento della funzione successiva
a%>%f(b) # -> equivale a f(a,b)


#verificare se l'oggetto è una matrice
rowSums(matrice) %>% is.matrix #FALSE -> è un vettore
#equivale ad 
is.matrix(rowSums(matrice)) #FALSE -> è un vettore

rowSums(matrice) %>% is.vector #TRUE 
#equivale ad
is.vector(rowSums(matrice)) #TRUE

#aggiungo una colonna passata come vettore
  #il vettore da aggiungere dovrà avere gli stessi elementi
  # quanti sono le righe della matrice
nuova_matrice=cbind(matrice,E=c(5,6)) #nuova colonna etichettata E
nuova_matrice #da 2x2 a 2x3
#oppure usando un vettore di appoggio
Z=c(10,11)
nuova_matrice=cbind(matrice,Z) #nuova colonna etichettata E
nuova_matrice

#aggiungo una riga passata come vettore
  #il vettore da aggiungere dovrà avere gli stessi elementi
  # quanti sono le colonne della matrice
nuova_matrice=rbind(nuova_matrice,c(99,98,97)) 
nuova_matrice #da 2x3 a 3x3

#unire due matrici verticalmente (una sotto l'altra) con rbind
  #il numero di colonne deve essere lo stesso
altra_matrice=matrix(c(40,41,42,43,44,45),
                     nrow=2,
                     byrow=TRUE)
matrice_full=rbind(nuova_matrice,altra_matrice) #unire due matrici verticalmente
matrice_full #3x3 + 2x3 = 5x3 -> sono aumentate le righe ma non le colonne


