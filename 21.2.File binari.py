#Nei file binari non ci sono caratteri codificati come testo

#Per scrivere in un file binario i dati vanno prima SERIALIZZATI
#Per leggere da un file binario si deve DESERIALIZZARE i dati
#modulo pickle -> permette di serializzare i file binario

import pickle
#la scrittura avviene con dump()
#la lettura avviene con load()

dizionario = {'X': 1, 'Y': 2, 'Z': 3}

print("Scrittura dizionario nel file binario....")
#w->modalità scrittura
#b-> modalità binario
outputfile = open('21.dizionario.dat','wb')

#scrivo nel file i dati -> serializzazione
pickle.dump(dizionario,outputfile)
outputfile.close()

print("Lettura del file binario scritto")
#r -> modalità lettura
#b -> modalità binaria
inputfile = open('21.dizionario.dat','rb')

#leggo nel file i dati e lo salvo in file_dizionario-> deserializzazione
file_dizionario=pickle.load(inputfile)
outputfile.close()
#stampo il contenuto del file
print(file_dizionario)




