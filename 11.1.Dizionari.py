#DIZIONARIO -> Memorizza coppie chiave-valore
#CHIAVI NON DUPLICABILI
#gli elementi non sono in ordine 
    #gli elementi non sono ordinabili
    
#CREO DIZIONARIO
dizionario={"Marco":123456789,"Giuseppe":35718,"Pippo":8451231}
print(dizionario)
#Dizionario vuoto
dizionario_vuoto=dict()
print('Dizionario vuoto')
print(dizionario_vuoto)

#Grandezza del dizionario
print('Dimensione dizionario')
print(len(dizionario))

print('Ricerca chiave')
#RICERCA CHIAVE
#la ricerca avviene per nome->chiave e restituisce il valore
chiave="Marco"
if chiave in dizionario: #senza controllo delle eccezioni
    print(dizionario[chiave])

#se manca la chiave ci sarà eccezione KeyError
chiave="Pluto"
try:
    print((dizionario[chiave]))
except KeyError:
    print('chiave non trovata')

print('Cambio valora a partire della chiave')
#le chiavi dei dizionari possono mutare il valore
    #le chiavi sono immutabili
dizionario['Marco']=123456789
print(dizionario['Marco'])

#Cancellare coppia chiave valore
if 'Pippo' in dizionario: #senza controllo delle eccezioni
    del dizionario['Pippo'] #per chiave
print(dizionario) 

#Iterare dizionario
for chiave in dizionario:
    print(chiave)
    print(chiave, dizionario[chiave])
    
#Azzerra un dizionario
dizionario.clear()

#METODI
print("METODI DIZIONARI") 
dizionario={"Marco":123456789,"Giuseppe":35718,"Pippo":8451231}
print("Recupero valore da chiave") 

default='ciao'
#Recupera il valore associato altrimenti ritorna un valore di default
print(dizionario.get('Pippo',default))

print("Recupero valore da chiave")
#Restituisce le chiavi e relativi valori
t=dizionario.items()
print(t) 
#ogni elemento estratto sarà una tupla
print("Ogni singola tupla estratta con items()")
for tupla in t:
    print(tupla)

print("Tutte le chiavi")
#Tutte le chiavi
k=dizionario.keys()
for key in k:
    print(k)
    
print("Tutti i valori")
#Tutti i valori
valori=dizionario.values()
print(valori)

print("Estraggo ed elimino una chiave")
#Estrae il valore associato, lo ritorna e poi lo elimina
valore=dizionario.pop('Pippo','Non valido') #Chiave, return di default
print("Valore estratto")
print(valore)
print("Dizionario modificato")
print(dizionario)

print("Estraggo il valore di una chiave a caso e lo elimino")
#Estrae a caso
estratto=dizionario.popitem()
print(estratto)
print("Dizionario modificato")
print(dizionario)