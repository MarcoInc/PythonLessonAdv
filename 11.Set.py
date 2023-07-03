#SET -> memorizza dati come se fosse un insieme matematico
    #nessun duplicato
        #causerà un'eccezione
#Cosa può contenere:
    #Lista ->
    #Stringa 
    #Tupla
#Set vuoto
insieme=set() 

insieme=set("abbaabccddddddd")
print(insieme) #stamperà i singoli elementi senza ripetizioni

#Riempio set a partire da una lista
print('Da lista [...]')
lettere=["alfa","beta","gamma","delta"]
print(lettere)

print("""A set {'..'}""")
insieme=set(lettere)
print(insieme)

print('Dimensione set')
#Dimensione set
dimensione=len(insieme)
print(dimensione)

print('Aggiungo elemento')
#Aggiunta di un elemento
insieme.add('zeta')
print(insieme)

print('Aggiungo più elementi')
#Aggiungo più elemento
lista=["kappa","W","Pippo","Pluto"]
insieme.update(lista)
print(insieme)

print('Rimuovo elementi')
#Rimuovere elemento
insieme.remove('alfa')  #causa eccezione KeyError
insieme.discard('gamma') #non causa eccezione
print(insieme)

print('Elimino tutto il set')
#elimino tutto il set
insieme.clear()
print(insieme)

#OPERAZIONI INSIEMISTICA
print('OPERAZIONI INSIEMISTICA')
print('Unione |')
insieme1=set(["alfa","beta","gamma","delta","epsilon","kappa"])
insieme2=set(["alfa","beta","delta","eta","zeta"])

#Unione -> tutti gli elementi del primo e del secondo
unione1=insieme1|insieme2 
#uguali
unione2=insieme1.union(insieme2)
print(unione1)
print(unione2)

print('Intersezione &')
#Unione -> tutti gli elementi che sono in comune tra il primo e il secondo
intersezione1=insieme1&insieme2
#uguali
intersezione2=insieme1.intersection(insieme2)
print(intersezione1)
print(intersezione2)

print('Differenza -')
#Differenza -> tutti gli elementi del primo che non appartengono al secondo
differenza1=insieme1-insieme2
#uguali
differenza2=insieme1.difference(insieme2)
print(differenza1)
print(differenza2)

print('Differenza simmetrica ^')
#Differenza simmetrica -> tutti gli elementi non condivisi tra il primo e il secondo
differenza_simmetrica1=insieme1^insieme2
#uguali
differenza_simmetrica2=insieme1.symmetric_difference(insieme2)
print(differenza_simmetrica1)
print(differenza_simmetrica2)

print('VERIFICA SET')
#Metodi per verificare i set
print('Sottoinsieme <=')
print(insieme1.issubset(insieme2))
#uguali
print(insieme1<=insieme2)

print('Superinsieme >=')
print(insieme1.issuperset(insieme2))
#uguali
print(insieme1>=insieme2)










