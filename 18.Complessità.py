#Complessita nella ricerca
#Lineare -> dal primo all'ultimo. non ottime per la ricerca
    #liste
    #tuple
#Sublineare -> migliore per la ricerca
    #Set
    #Dizionari

#RICERCA
print("RICERCA LISTA vs SET")
import time #tempo di sistema
#creo una lista grande in modo sequenziale
lista=list(range(100000000)) #lista di tantissimi elementi
#set grande quanto la lista
insieme=set(lista)
ricerca=2000000000

start_time=time.time() #tempo di sistema attuale

if ricerca in lista:
    print(ricerca," trovato nella lista")
else:
    print(ricerca," non trovato nella lista")
print("La ricerca nella lista ha impiegato",\
    format(time.time() - start_time,'.5f'),"secondi")
#tempi molto lunghi

start_time=time.time()
if ricerca in insieme:
    print(ricerca," trovato nel set")
else:
    print(ricerca," non trovato nella set")
print("La ricerca nel set ha impiegato",\
    format(time.time() - start_time,'.5f'),"secondi")
#tempi molto brevi

