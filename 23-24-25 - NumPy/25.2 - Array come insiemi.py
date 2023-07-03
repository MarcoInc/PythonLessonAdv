#Gli array posson essere trattati come insiemi matematici
import numpy as np
print("INSIEME CON VALORI UNICI -> npunique")
array_duplicati=np.array([0,1,5,6,0,3,5,2,8,4,0])
print(array_duplicati)
print("-> dopo -> npunique")
print(np.unique(array_duplicati))

print("ELEMENTI ARRAY STANNO IN UN ALTRO ARRAY? -> np.in1d")
array=np.array(range(10))
print(array)
array2=np.array([0,2,10,3,12,3,7,9,15,20,1])
print(array2)
#controlla quali elementi di array2 sta in array
print(np.in1d(array2,array)) #ritorna un array di booleani

print("UNIONE ARRAY -> np.union1d")
pari=np.array(range(0,10,2)) #pari fino a 10 ESCLUSO
dispari=np.array(range(1,10,2)) #dipari fino a 10 ESCLUSO
print(pari)
print(dispari)
print("unendo....")
array_unito=np.union1d(pari,dispari)
print(array_unito)

print("INTERSEZIONE ARRAY -> np.union1d")
array_intersezione=np.intersect1d(pari,array_unito)
print("....tra pari e unito -> np.union1d")
print(array_intersezione)
