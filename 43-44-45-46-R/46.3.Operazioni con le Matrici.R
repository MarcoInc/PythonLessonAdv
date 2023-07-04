#Le operazioni tra matrici seguono la stessa logica delle operazioni tra vettori
# Le regole del CALCOLO MATRICIALE vanno comunque rispettate

#PRODOTTO TRA MATRICI
  # il numero di colonne di una deve essere uguale al numero di righe dell'altra
    #La moltiplicazione NON E' COMMUTTATIVA
matrice_1=matrix(c(1,2,3,4), byrow=FALSE, nrow=2)
matrice_2=matrix(c(1,2,3,4), byrow=TRUE, nrow=2)
matrice_1
matrice_2

    #Ottemiamo una matrice 2x2
matrice_prodotto=matrice_1%*%matrice_2
matrice_prodotto

#SOMMA TRA MATRICI
matrice_somma=matrice_1+matrice_2
matrice_somma



