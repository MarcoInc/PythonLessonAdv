#Sequenza -> oggeto che contiene più element

#LISTA -> tipo array ma diverso
    #Array sono omogeni stesso tipo
    #Liste mostrano le virgole, gli array no
print("LISTA")  
lista_num=[1,2,3,4,5] #omogeneo -> tutti dello stesso tipo
lista_mista=["Ciao","Mondo",5,"Sole",3.14] #non omogeneo -> tipo diverso
#stampa le liste
print(lista_num)
print(lista_mista)

print("RIPETIZIONI")  
#RIPETIZIONI di elementi 
lista_0=[0]*5 #ripete 0 per 5 volte
lista_bin=[0,1]*5 #ripete la sequenza 0 1 per 5 volte
print(lista_0)
print(lista_bin)

print("FOR")  
#FOR - La lista è un oggetto iterabile
lista_num=[1,2,3,4,5,6,7,8,9,10] #omogeneo -> tutti dello stesso tipo
for x in lista_num:
    print(x)
    
print("INDEXING")  
#INDEXING -> uso di indici
print(lista_num[5]) #elemento all'indice 5
#print(lista_num[50]) #eccezione IndexError -> siamo fuori dalla lista
print("Cambio valore")  
lista_num[5]="8"  #cambio il valora ad un indice
print(lista_num[5])

print("LUNGHEZZA")
#LUNGHEZZA
dim=len(lista_num)
print(dim)
print("Ultimo elemento")
print(lista_num[dim-1]) #ultimo elemento

print("Funzione conta")
conta=[0]*10   #array da 10 tutti a 0
for i in range(10):  #scorro
    conta[i]=i+1 #metto valori dentro la lista
print(conta)

print("Unire liste")
#UNIRE LISTE
lista_tot=lista_num+lista_mista
print(lista_tot)

print("SOTTOLISTA")
#SOTTOLISTA / SLICE -> Sottostringa
sottolista=lista_tot[2:10] #dal 2 incluso al 10 escluso
print(sottolista)

print("OPERATORE IN")
#OPERATORE IN

print("CERCARA NELLA LISTA")
#CERCARE NELLA LISTA
lista_nomi=["Pippo","Paolo","Francesco","Franco"]
nome="Franco"
if nome in lista_nomi:
    print('Trovato')
else:
    print('Non trovato')
    
print("\nMETODI DELLE LISTE")
#METODI DELLE LISTE
lista_num=[1,2,3,4,5,6,7,8,9,10]
#Aggiunge un elemento in coda
print("Aggiungo 99 in coda")
lista_num.append(99)
print(lista_num)

#Ritorna un elemento all'indice indicato
print("Elemento all'indice 5")
print(lista_num.index(5)) #elemento all'indice 5

print("Inserisco numero all'indice 3")
#Inserisce al indice->primo argomento il valore->secondo argomento
lista_num.insert(3,15975)  
print(lista_num)

print("Lista ordinata")
#Ordina gli elementi della lista
lista_num.sort()    
print(lista_num)    

print("Lista invertita")
#Inverte i valori della lista
lista_num.reverse()     
print(lista_num)

#Ritorna il massimo della lista
print("Massimo")  
print(max(lista_num))
 #Ritorna il minimo della lista
print("Minimo")    
print(min(lista_num))

print("Rimuovo il primo 10 che trova")
#Rimuove elemento all'indice creato
lista_num.remove(10) 
print(lista_num)
#Rimuovo la prima occorenza che trova
print("Rimuovo l'elemento all'indice 5")
del lista_num[5] 
print(lista_num)

a=[1,2,3,4]
c=0
for e in a:
    c=c+e
    print(c)




