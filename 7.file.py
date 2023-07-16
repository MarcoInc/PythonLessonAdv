#file di testo -> caratteri codificati ASCII (0 a 255)
#file binario -> codifica del file in binario
#estensione -> indica il tipo di file
#APERTURA FILE -> open()
#ELABORAZIONE FILE
    #scrittura su un file -> output file ->open("file",'w')
    #lettura da un file -> input file  >open("file",'r')
#CHIUSURA FILE -> close()
#nome fisico del file -> nome.estensione
#nome logico -> nome del file associato nel programma per aprire il file

#APERTURA ->effettuo le operazioni in un oggetto di python
oggetto_file=open("7.file.txt", 'w')
#scriviamo nell'oggetto file
oggetto_file.write("ciao\n")  #usiamo un \n tra per creare righe nuove
oggetto_file.write("mondo. Sono le "+str(14)+"\n") #casting se abbiamo tipi numerici
oggetto_file.close() #chiudere sempre se si vuole leggere o fare altro

print('open()')
#RIAPRO
oggetto_file=open("7.file.txt", 'r')
contenuto=oggetto_file.read()   #leggo il file e metto tutto in contenuto
oggetto_file.close()    #chiudo lo stream
print(contenuto)    #stampo il contenuto letto

print('readline()')
#LETTURA RIGA PER RIGA
oggetto_file=open("7.file.txt", 'r')
riga1=oggetto_file.readline()  #salvo una riga in una variabile
riga2=oggetto_file.readline()
oggetto_file.close()
print(riga1)    #stampo riga per riga
print(riga2)

print('rstrip()')
oggetto_file=open("7.file.txt", 'r')
riga1=oggetto_file.readline() #readline legge anche il \n terminale"
riga2=oggetto_file.readline()
#RIMOZIONE CARATTERE TERMINALE \n
riga1=riga1.rstrip("\n")
riga2=riga2.rstrip("\n")

oggetto_file.close()
print(riga1)
print(riga2)

print('append->a')
#APPEND -> se voglio scrivere ulteriormente, non elimina il vecchio contenuto
oggetto_file=open("7.file.txt", 'a') #accodo nuovi dati
oggetto_file.write("Oggi il tempo e' bello\n") 
oggetto_file.write("E fa molto caldo\n")
oggetto_file.close()

oggetto_file=open("7.file.txt", 'r')
contenuto=oggetto_file.read()
oggetto_file.close()
print(contenuto) #vedrò le righe vecchie e quelle nuove

print('ITERARE RIGHE FILE')
#EOF -> End of file . File terminato. Se letto dalla read line ritorna una stringa vuota
print('-Tramite while\n')

oggetto_file=open("7.file.txt", 'r')
riga=oggetto_file.readline() #leggo la prima riga
riga=riga.rstrip("\n")
while riga !='': #stringa vuota quindi fine EOF
    print(riga)
    riga=oggetto_file.readline() #se arriva al EOF, esce dal while
    riga=riga.rstrip("\n")
oggetto_file.close()

print('\n-Tramite for\n')

oggetto_file=open("7.file.txt", 'r')
for riga in oggetto_file: #scorro riga per riga
    riga=riga.rstrip("\n")
    print(riga)
oggetto_file.close()