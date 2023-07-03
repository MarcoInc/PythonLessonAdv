#Codifica Unicode 16
# Tipo -> str
#'Stessa riga' o "Stessa riga"
#"""" Righe
#    diverse """

print("Singoli caratteri")
#Accesso singoli caratteri
stringa="sole"
for carattere in stringa:
    print(carattere)

print("Singoli caratteri indice")
#singoli caratteri
print(stringa[0],stringa[2]) #primo e terzo

print("Singoli caratteri indice a ritroso")
#A Ritroso
print(stringa[-1],stringa[-2]) #ultimo e penultimo

#Eccezione IndexError se vado oltre tramite indice
print("Test eccezioni")
index=10
if index<len(stringa):
    print(stringa[index])
else:
    print("Indice non valido")
#OPPURE
try:
    print(stringa[index])
except:
    print("Indice non valido")

#esempio contatore
contatore=0
for carattere in stringa:
    if carattere=='s' or carattere=='l':
        contatore+=1
print("Ho contato s e l :", contatore)

#Concatenazione
stringa1=stringa+stringa

print("Sotto stringhe")
#Sotto stringhe
stringa2="Che caldo che fa"

print("[8:len(stringa2)]")
sub1=stringa2[8:len(stringa2)] #dal 8 incluso alla fine
print(sub1)

print("[8:]")
sub2=stringa2[8:] #dal 8 in poi
print(sub2)

print("[:7]")
sub3=stringa2[:7] #fino 7 escluso
print(sub3)

print("[0:len(stringa2):2]")
sub4=stringa2[0:len(stringa2):2] #dal 0 alla fine a 2 a 2
print(sub4)

print("Ricerca")
#Ricerca
nomi="Marco Giorgio Samuele Luigi Andrea Salvo Cristiano"
print(nomi)
if "Marco" in nomi:
    print("Nome trovato")
else:
    print("Nome non trovato trovato")

print("METODI STRINGHE")
#METODI STRIGHE -> sono degli oggetti
print("\tTest sulle stringhe")
    #Test sulle stringhe
stringa="CIAO123"
print(stringa+" Ha solo caratteri alfa numerici ed >=1?")
print(stringa.isalnum())

stringa="ciao"
print(stringa+" Ha solo caratteri solo caratteri alfabetici ed >=1?")
print(stringa.isalpha())

stringa="123456"
print(stringa+" Ha solo caratteri solo caratteri numerici ed >=1?")
print(stringa.isdigit())

stringa="abracadabra"
print(stringa+" Ha tutti i caratteri alfabetici in minuscolo ed >=1?")
print(stringa.islower())

stringa="ABRACADABRA"
print(stringa+" Ha tutti i caratteri alfabetici in MAIUSCOLO ed >=1?")
print(stringa.isupper())

stringa="  \n \t" #(spazio, \n,\t)
print(stringa+" Ha solo spazi ed >=1?") 
print(stringa.isspace())

print("\nModificare stringhe")
stringa="  Ciao Mondo  "

print(stringa.lower()+" - minuscolo")
print(stringa.upper()+" - MAIUSCOLO")
print(stringa.lstrip()+" - spazi iniziali rimossi")
print(stringa.rstrip()+" - spazi finali rimossi")

stringa="  Ciao Mondo \t "
print(stringa.strip()+" - spazi iniziali e finali rimossi")

print("Ricerca sottostringhe")
    #Ricerda sottostringe
stringa="Ciao mondo"
print("Finisce in ndo?")
print(stringa.endswith("ndo"))

print("Inizia per Cia?")
print(stringa.startswith("Cia"))

print("Prima occorenza di mondo?")
print(stringa.find("mondo")) #se non trova ritorna -1

print("Sostituisco mondo con bello")
print(stringa.replace("mondo","bello"))

print("MOLTIPLICARE I CARATTERI")
#MOLTIPLICARE I CARATTERI
for i in range(1,5):
    print(">"*i)
for i in range(5,0,-1):
    print(">"*i)

print("Da stringa a lista")
#Da stringa a lista
stringa="Nel mezzo del cammin di nostra vita"
print(stringa.split()) #per spazi
data="25/07/1991"
print(data.split("/")) #per /

print("Da lista a stringa con separatore")
#Da lista a stringa con separatore
lista=["ciao","mondo","mare","montagna"]
s=" , " #separatore
print(s.join(lista))

print("Rimuovo spazi indisiderati")
#Rimozione spazi indesiderati
stringa="Nel mezzo del cammin      di nostra vita  \t mi ritrovai \t  per una selva oscura"
s=" "
print(s.join(stringa.split()))
#crea una lista con ogni singolo elemento con split() 
# e poi converte in stringa con separatore " "





















