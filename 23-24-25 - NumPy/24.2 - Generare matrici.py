import numpy as np
print("MATRICE RANDOM")
matrice_random=np.random.random((3,3)) #matrice 3x3
print(matrice_random)

print("-> valori tra 0 e 100 ")
matrice_random=np.random.random((3,3))*100 #matrice 3x3
print(matrice_random)

print("MATRICE STESSI VALORE")
print("->da ones a 7")
#matrice  4x5 con tutti 1 e poi moltiplica tutti i valori per 7
matrice_ripetuti=np.ones((4,5),dtype=np.uint64)*7
print(matrice_ripetuti)
print("->direttamente a 7 -> np.full()")
#ne creo una direttamente 4x5 tutti a 7
matrice_ripetuti=np.full((4,5),7)
print(matrice_ripetuti)

print("MATRICE UNIFORNEMENTE DISTRIBUTI -> np.linspace()")
#np.linspace(INIZIALE (INCLUSO), FINALE(INCLUSO), #ELEMENTI)
array1=np.linspace(1,100, 10)
print("np.linspace(1,100, 10)")
print(array1)

print("np.linspace(1,100, 7)")
array2=np.linspace(1,100, 7)

print(array2)
array3=np.linspace(1,100, 7)
print("np.linspace(1,100, 7)")

print(array3)
