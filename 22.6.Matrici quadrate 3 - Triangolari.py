#se vede se il triangolo inferiore o superiore sono tutti uguali a zero

#superiori 
    #range(N) for j in range(i,N) 
#inferiori
    #range(N) for j in range(i+1)
import random
N = 5

def inizializza():
    m = [0]*N
    for i in range(N):
        riga = [0]*N
        m[i] = riga
    return m


def matr_triang_sup(m):
    m2 = m
    for i in range(N):
        for j in range(i,N):
            m[i][j] = random.randint(0,9)
    return m2

def matr_triang_inf(m):
    m2 = m
    for i in range(N):
        for j in range(i+1):
            m[i][j] = random.randint(0,9)
    return m2


def visualizza_mat(m):
    for i in range(N):
        print(m[i])


def main():
    m = inizializza()
    print("Matrice triangolare superiore:")
    visualizza_mat(matr_triang_sup(m))
    
    print()
    m = inizializza()
    print("Matrice triangolare inferiore:")
    visualizza_mat(matr_triang_inf(m))

main()
