import numpy as np

print("COPY")
array1=np.array([1,2,3,4,5,6])
print(array1)
array2=array1.copy()
print(array2)

print("MODIFICA DTYPE e SHAPE -> array.astype")
#astype(dtype,casting="unsafe", copy=True)
print("->dtype")
array1=np.ones(5) #da float
print(array1)
array2=array1.astype(np.uint64) #ad uint64. si perde la parte decimale
print(array2)

print("->shape")
array=np.array(range(1,13) ,copy=True)
print("Prima - ",array," - shape=",array.shape)
array.shape=[2,6] #cambiamo dimensione 2 righe 6 colonne
print("Dopo - ",array," - shape=",array.shape)

print("->reshape->3 DIM")
#Matrice a 3 dimensioni 2x3x3=12 -> 12 numero di elementi di partenza
matrice=array.reshape(2,3,2)
print("Reshape - ",matrice," - shape=",matrice.shape)
#se il prodotto delle dimensioni non fa il numero di elementi di partenza
    #-> Eccezione -> ValueError

print("->reshape->2 DIM")
#48 elementi
array=np.arange(1,49)
print("Prima reshape- ",array," - shape=",array.shape)
matrice=array.reshape(6,8) #6x8=48
print("Reshape - ",matrice," - shape=",matrice.shape)

print("->Trasposizione -> array.T")
print("--->Prima")
array=np.array(range(1,9) ,copy=True)
matrice=array.reshape(2,4)
print(matrice)
print("--->Dopo")
matrice_T=matrice.T
print(matrice_T)

#Metodo alternativo -> inverte gli assi
print("->Trasposizione -> matrice.swapaxes()")
print("--->Dopo")
matrice_swappata=matrice.swapaxes(0,1) #assi da 0 a 1
print(matrice_swappata)

#Metodo alternativo -> inverte permuta gli assi
print("->Trasposizione -> matrice.transpose()")
print("--->Prima")
matrice=array.reshape(2,2,2)
print(matrice)
print("--->Dopo")
#il primo asse 0 rimane verticale, gli altri vengono scambiati 2<-1 e 1->2
matrice_transposta=matrice.transpose(0,2,1) 
print(matrice_transposta)










