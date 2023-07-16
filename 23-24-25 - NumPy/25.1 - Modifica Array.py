import numpy as np

print('SOTTOMATRICE')
#Sottomatrice -> una parte della matrice
#Matrice da 1 a 28 resa a 7x4
matrice=np.array(range(1,29)).reshape(7,4)
print(matrice) 

print("-> Seconda riga  -> matrice[1]")
print(matrice[1])

print("-> Dalla riga 3 alla 6  -> matrice[3:6]")
print(matrice[3:6])

print("-> Dalla riga 3 alla 6 prendi la seconda riga[1] -> [3:6][1][1]")
print(matrice[3:6][1]) #3:6 è un array di due righe, [1] indica la seconda

print("-> Dalla riga 3 alla 6 prendi la seconda riga[1] e seconda colonna[1] -> [3:6][1]")
print(matrice[3:6][1][1])
#3:6 è un array di due righe, [1] indica la seconda riga e [1] seconda colonna

print('INSERIMENTO')
#INSERIMENTO -> non modificano la struttura attuale ma ne restituiscono una

print('-> Aggiungo elemento alla fine -> np.append') 
array=np.array(range(-10,10))
print(np.append(array,50))#aggiunge un alemento alla fine

print('-> Aggiungo elemento in un indice -> np.insert') 
print(np.insert(array,3,100))#aggiunge un alemento all'indice 3

print('FILTRO')
#FILTRI -> seleziono elementi in base a dei criteri
print('-> Con operatori di confronto')
array_filtrato=array[array<0] #prendo solo i <0
array_booleano=array<0   #alternativa con booleano
print(array_filtrato)

print('--> Con where -> np.where(array_booleano)') #necessita di un array booleano
array_filtrato=np.where(array_booleano) #ritorna tupla
print(array_filtrato)
print('-->  np.where e argomenti -> np.where(array_booleano,ifSi,ifNo)') #necessita di un array booleano
#Ulteriori argomenti a where
    #dove sta true mette il primo
    #se è false mette il secondo
array_filtrato=np.where(array_booleano,'-','+')
print(array_filtrato)

print('-->  np.where ritorna gli indici') #necessita di un array booleano
array_posizioni=np.where(array<0) #ritorna tupla
print(array_posizioni)

print('--> DIMENSIONE ARRAY - len(array[0])') 
#prende la dimensione della riga [0] <- unica riga
print("Ne ho trovati: ",len(array_posizioni[0]))

print('--> SCORRERE ARRAY - for i in range(len(array_posizioni[0]))')
#scorro il rigo [0] per tutta la sua lunghezza
for i in range(len(array_posizioni[0])): 
    print(array_posizioni[0][i]) #stampo il rigo[0] per ogni i

print('FUNZIONI CONDIZIONALI') 
print("->Posizioni diversi da 0")
print(array)   
print(np.nonzero(array))  #ritorna una tupla
print("->Posizioni diversi da 0")

print("-> Tutti gli elementi sono True o diversi da 0?")
print(np.all(array))  #ritorna un booleano
print("-> Almeno un elemento è True o diverso da 0?")
print(np.any(array))  #ritorna un booleano

print('ORDINARE -> sort') 
array=np.random.random(10)*100
print("Prima")   
print(array)   
print("Dopo")   
print(np.sort(array))

