import re
#GLOBBING
# Il globbing è l’operazione che consiste nel ricercare nomi di file e altre stringhe  tramite espressioni regolari semplificate
# * -> carattere Jolly che rappresenta zero o più caratteri
# ? rappresenta esattamente un carattere 
# (\ + . non sono codici speciali nel globbing)

#Glob permette l'uso dei caratteri jolly
import glob 

print("glob.glob('file')")
#tutti i file con estensione .txt che stanno nella cartella attuale
print(glob.glob("*.txt"))

print()
print("glob.iglob('percorso') -> cartelle")
#memorizza un iteratore usato per scorrere SOLO LE CARTELLE un dato path
risultato=glob.iglob('C:/*')
for a in risultato: #itero 
    print(a)   #stampo tutte le cartelle nel path

print()
print("glob.iglob('percorso')  -> file")
#scorrere SOLO I FILE un dato path
risultato=glob.iglob('C:/*.*')
for a in risultato: 
    print(a)   #stampo tutti i file nel path

print()
print("iglob -> ricorsivo")
#ricerca nella cartella attuale e anche nelle sottocartelle
risultato=glob.iglob('**/*.txt',recursive=True)
for a in risultato: #itero 
    print(a)   #stampo tutti i valor nel path attuale e sottopath
    
print()
print("Ricerca nei file txt")
ricerca=input("Cosa vuoi cercare?")
lista_file=glob.glob("*.txt")
for testo in lista_file:
    infile=open(testo,'r')
    risultato=re.findall(ricerca,infile.read(),re.I)
    print("risultati in ",testo)
    for a in risultato:
        print(a)
    infile.close
