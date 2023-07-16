#Stesso numero di righe e colonne
#diagonale principale
    #lista[i][i] = 1
#diagonale secondaria
    #lista[i][N-1-i] = 1

N = 5

def inizializza(): #crea una matrice quadrata
    m = [0]*N
    for i in range(N):
        riga = [0]*N
        m[i] = riga
    return m


def diag_princip(m): #mette 1 nella diagonale principale
    for i in range(N):
        m[i][i] = 1
    return m

def diag_second(m): #mette 1 nella diagoanle secondaria
    for i in range(N):
        m[i][N-1-i] = 1
    return m


def visualizza_mat(m): #mostra la matrice
    for i in range(N):
        print(m[i])


def main():
    m = inizializza()
    print("Matrice vuota:")
    visualizza_mat(m)
    
    matrice_principale = diag_princip(m)

    print()
    print("Matrice con diagonale principale a 1:")
    visualizza_mat(matrice_principale)
    
    m = inizializza()
    matrice_secondaria = diag_second(m)
    print()
    print("Matrice con diagonale secondaria a 1:")
    visualizza_mat(matrice_secondaria)
main()
