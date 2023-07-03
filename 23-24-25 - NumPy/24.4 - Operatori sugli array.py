import numpy as np
#Vengono associati elementi con lo stesso indice

#SOMMA TRA ARRAY
print("SOMMA TRA ARRAY")
array1=np.random.random(10)
array2=np.random.random(10)

print(array1+array2) #somma tra loro gli elementi
print("SOTTRAZIONE TRA ARRAY")
print(array1-array2)    #sottrae tra loro gli elementi

print("CONFRONTO TRA ARRAY")
print(array1>array2) #confronta tra loro gli elementi

print("PRODOTTO SCALARE")
print(array1*0.8) #moltiplica ognuno per 0.8

print("RADDOPPIATI")
array1*=2
print(array1) #moltiplica ognuno per 0.8

print("UFUNCTION -> ufunc")
print("-> Confronto righe matrice")
array=np.random.random(20)*100
matrice=array.reshape(10,2).T
#confronto la riga 0 con la riga 1
variazioni=np.greater(matrice[0],matrice[1])
print(variazioni)

#NUMERI STRANI
print("NUMERI PARTICOLARI")
array=np.random.random(20)*100
array[5]=np.nan #->Not A Number
print("-> NaN")
print(array)
print("-> Ci sono NaN?")
print(np.isnan(array)) #C'è un nan nell'array?
array[np.isnan(array)]=0
print(array)



