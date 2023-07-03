import numpy as np

print("INDICIZZAZIONE - filtro_booleano=dirty<0")
#INDICIZZAZIONE BOOLEANA
    #Array di supporto in cui:
        #come indice un array di bool
        #verranno selezionati gli indici con True
#esempio alcuni valori non validi <0 verranno intesi come DIRTY
dirty=np.array([9,4,1,-0.01,-0.02,-0.0001])

print("Array sporco -> ",dirty)
#Seleziona tutti i valori<0 e mette True, altrimenti false
filtro_booleano=dirty<0
print("Array booleano")
print(filtro_booleano)
#Negli indici dove sta True <0 mette 0 e pulisce l'array
dirty[filtro_booleano]=0
print("Array pulito - ", dirty)

print("->Operatori logici")
#Possiamo usare operatori logici per selezionare divesamente i valori
dirty=np.arange(-1,1.1,0.2)
print("Array sporco -> ",dirty)
#Combiniamo più condizioni
filtro_booleano=(dirty<=0.5) & (dirty>=-0.5)
print("Array booleano")
print(filtro_booleano)
dirty[filtro_booleano]=0
print("Array pulito - ", dirty)
#Ordine operatori logici inportante:
    #NumPy gli operatori relazionali (<,==) hanno precedenza inferiore tra
        #operatori booleani -> motivo per cui usiamo le parentesi
    #Python non da la precedenza a nessun operatore e si basa sulle parentesi

print("SELEZIONE INTELLIGENTE")
#L'indicizazzione intelligente
    #l'indice non è uno scalare ma un array o lista di indici
        # [1,3,4] -> selezioniamo gli indici 1,3 e 4

array=np.array(range(1,9))
print(array)

print("Selezionati gli indici 2,4,7")
selezionati=array[[2,4,7]]
print(selezionati)

print("SLICING - array[[2,4,7]]")
array=np.array(range(1,9))
matrice=array.reshape(2,4)
print(matrice)

print("---->[:,[1] Tutte le righe della sola colonna 1 ->matrice")
selezionati1=matrice[:,[1]]
print(selezionati1)
print("----> [:,1] Tutte le righe della sola colonna 1 ->array")
selezionati2=matrice[:,1]
print(selezionati2)


