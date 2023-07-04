matrice=matrix(c(1,2,3,4,5,6,7,8,9),
               nrow=3,
               ncol=3,
               byrow=TRUE)
nomi_colonne=c("A","B","C")
nomi_righe=c("D","E","F")
colnames(matrice)=nomi_colonne
rownames(matrice)=nomi_righe
matrice

#indexing matrici[ ] -> ritorna una matrice
  #selezioni elemento alla prima riga e prima colonna
matrice[1,1] #è una matrice

  #seleziona la seconda e terza riga e la prima e seconda colonna
  # [c(RIGHE),c(COLONNE)]
matrice[c(2,3),c(1,2)]

matrice%>%class() #"matrix" "array" 

#slicing matrice
  #seleziono tutta la seconda colonna
colonna_B=matrice[,2] #ritorna vettore
colonna_B
  #seleziono tutta la prima riga
riga_c=matrice[1,] #ritorna un vettore
riga_c

#Matrice booleanca con condizione

matrice_condizione=matrice>5
matrice_condizione
class(matrice_condizione) #"matrix" "array" 

  #posso usare la matrice booleana per selezionare elementi 
  #della matrice iniziale
matrice[matrice_condizione] #stampa i valori >5

#Eliminare riga
matrice_senza_riga=matrice[-1,]
matrice_senza_riga
  #eliminare più righe
matrice_senza_righe=matrice[-(2:3),] # eliminate seconda e terza riga 
matrice_senza_righe #è rimasta una riga -> vettore

#Eliminare colonna
matrice_senza_colonna=matrice[,-1]
matrice_senza_colonna
  #eliminare più colonne
matrice_senza_colonne=matrice[,-(2:3)] # eliminate seconda e terza colonna 
matrice_senza_colonne #è rimasta una colonna -> vettore


