#Una matrice è simmetrica quando è la trasposta di se stessa
    #se tutti lista[i][j] == lista[j][i]
    
    
#range(N) for j in range(i+1,N) 

N = 5

def inizializza(): #creo matrice vuota
    m = [0]*N
    for i in range(N):
        riga = [0]*N
        m[i] = riga
    return m


def is_simmetrica(m): #verifica se è simmetrica
    for i in range(N): 
        for j in range(i+1,N):
            if m[i][j] != m[j][i]:
                return False
    return True


def visualizza_mat(m):
    for i in range(N):
        print(m[i])


def main():
    m = inizializza()
    print("Matrice:")
    visualizza_mat(m)
    
    print()
    if is_simmetrica(m):
        print("Matrice simmetrica")
    else:
        print("Matrice non simmetrica")
   

main()