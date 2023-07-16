#Liste a 2 dimensioni 
    #indice riga
    #indice colonna
#Trasposta, inverto il numero di righe con il numero di colonne e viceversa
    # Matrice:
#       [4, 6]
#       [1, 8]
#       [6, 3]

# Matrice trasposta:
#       [4, 1, 6]
#       [6, 8, 3]

import random

RIGHE = 3
COLONNE = 2

def inizializza(): #riempie la matrice con elementi random
    m = [0]*RIGHE
    for i in range(RIGHE):
        riga = [0]*COLONNE
        m[i] = riga

    for i in range(RIGHE):
        for j in range(COLONNE):
            m[i][j] = random.randint(1,9)

    return m

def trasposta(m):
    #creo una matrice inzialmente vuota con 0
    mt = [0]*COLONNE
    for i in range(COLONNE):
        riga = [0]*RIGHE
        mt[i] = riga
    #inserisco i valori in modo trasposto
    for i in range(RIGHE): 
        for j in range(COLONNE):
            mt[j][i] = m[i][j]

    return mt


def main():

    m = inizializza()

    print("Matrice:")
    for i in range(RIGHE):
        print(m[i])

    m2 = trasposta(m)

    print()
    print("Matrice trasposta:")
    for i in range(COLONNE):
        print(m2[i])

main()
