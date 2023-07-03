#Numpy richiede Anaconda https://www.anaconda.com/products/individual

#Libreria utile per gestire gli array -> diverse dalle liste
    #Liste 
        # i dati possono essere eterogenei -> di tipo diverso
        #stampa una virgola
    #Array 
        # i dati sono omogeni -> dello stesso tipo
        #non stampa virgole

#Importiamo la numpy con un alias facolativo
import numpy as np
print("ARRAY") 
array=np.array([1,2,3,4,5,6])
print(array)  #non ci saranno virgole
print(type(array)) #è un array numpy


#In un array numpy dati non vengono copiati direttamente nell'array 
    #con copy=True facciamo una copia dei valori
array=np.array([1,2,3,4,5,6], copy=True)

print("->Array numeri in sequenza") 
array=np.array(range(1,11), copy=True)
print(array) 

print("->Array di soli 1 -> tutti float") 
numeri=np.ones(5)
print(numeri) 

print("->Array di soli 0 -> tutti float") 
numeri=np.zeros(5)
print(numeri) 

#Un array numpy può ricevere come argomento:    
    #lista
    #array
    #tupla
#Il tipo viene rilevato automaticamente
    #Se vogliamo specificarlo -> dtype
        # bool -> booleani
        # int64 -> interi a 64 bit
        # uint64 -> interi senza segno a 64 bit
        # float64  -> float a 64bit
        # U32      -> interi senza segno a 32
print("->Array di soli 1 -> tutti INT") 
numeri=np.ones(5, dtype=np.uint64)
print(numeri) 

print("MATRICE") 
#MATRICE -> è una lista di liste
matrice=np.array([
    [1,2,3],[4,5,6],[7,8,9]
    ])
print(matrice)
print("->Matrice di tutti 1") 
matrice=np.ones([5,3],dtype=np.uint64) #5 righe 3 colonne
print(matrice)

print("DIMENSIONE") 
print("ndim=",matrice.ndim)  #quante dimensioni ho
print("shape=",matrice.shape)  #dimenzione matrice
print("dtype=",matrice.dtype) #tipo di dato

print("EYE -> np.eye(N,M=None, k=0,dtype=np.float)") 
#Crea una matrice NxM di tutti 1 nella diagonale k-esima,
# gli altri stanno 0
    #M=None -> M=N
#eye(N,M=None, k=0,dtype=np.float)
print("->Dalla prima diagonale") 
matrice_eye=np.eye(3)
print(matrice_eye)

print("-> Dalla seconda diagonale") 
matrice_eye=np.eye(3, k=1)
print(matrice_eye)

print("-> Dalla seconda e dim custom") 
matrice_eye=np.eye(3,M=5, k=1)
print(matrice_eye)

print("ARANGE") 
#arange(INIZIO(incluso), STOP(escluso), STEP)
numeri=np.arange(2,5,0.25)
print(numeri)

print("->arange decrescente") 
numeri=np.arange(5,2,-0.25)
print(numeri)








