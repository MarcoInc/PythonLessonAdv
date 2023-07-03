#CSV -> Comma-Sepated Values -> dati separati con un delimitatore
    #usato per memorizzare dati in modo separato tra loro

import numpy as np
print("LETTURA DA FILE CON NUMPY -> np.genfromtxt")
prezzi=np.genfromtxt('25. prezzi.txt')
print(prezzi)
print("-> Record letti -> array.size")
print(prezzi.size)
print("-> Tipo dei record  -> array.dtype")
print(prezzi.dtype)

print("SCRITTURA SU FILE TESTO  -> np.savetxt")
print("--->modifica valori array -> np.around")
    #raddopia e usa 2 cifre decimali
prezzi_raddoppiati=np.around(prezzi*2,2)
print(prezzi_raddoppiati)
#scrive i valori in un file i dati contenuti nell'array 
    #formatta il valori con 2 cifre decimali
np.savetxt('25. prezzi_new.txt',prezzi_raddoppiati, fmt='%0.2f')

print("SCRITTURA SU FILE NPY -> np.save")
#File .NPY -> formato BINARIO per NumPy
np.save('25. prezzi',prezzi)


print("LETTURA FILE NPY -> np.load")
#ATTENZIONE A METTERE L'ESTENSIONE NPY
prezzi=np.load('25. prezzi.npy')
print(prezzi)





