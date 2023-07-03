#ECCEZIONE -> errore in run-time composto tra un TRACEBACK-> messaggio di errore
#GIGO -> Garbage In, Garbage Out -> dati errati ottenuti
    #Validare input invalidi con degli if prima che siano processati
numeratore=int(input("Inserisci un numeratore\n"))
denominatore=int(input("Inserisci un denominatore\n"))
while(denominatore==0):
    denominatore=int(input("Inserisci un denominatore valido\n"))
print(numeratore/float(denominatore))


#GESTORE ECCEZIONE -> EXCEPTION HANDLER
numeratore=int(input("Inserisci un numeratore\n"))
denominatore=int(input("Inserisci un denominatore\n"))
#TEST SE UN'OPERAZIONE VA IN ERRORE
try:
    #blocco di codice che possono generare eccezioni
    print(numeratore/denominatore) #eseguito se non ci sono eccezioni
except:
    #istruzioni se si verifica un'eccezione in try
    print("ERRORE: Divisione per 0!")

#ECCEZIONI CON NOMI SPECIFICI  
try:
    print(numeratore/denominatore) #eseguito se non ci sono eccezioni
except ZeroDivisionError: #come quello di prima. divisione per zero
    print("ERRORE: Divisione per 0!")
    
#FILE NON TROVATO
try:
    oggetto_file=open("8.Eccezione.txt",'r')  
except FileNotFoundError:
    print("ERRORE Non c'è nessun file")

import math 
#TIPO INCOMPATIBILE CON L'OPERATORE
try:
    math.sqrt(-10)
except ValueError:
    print("ERRORE: Radice quadrata solo per valori non negativi")

#ESTRARRE L'ERRORE ORIGINALE
try:
    math.sqrt(-10)
except ValueError as errore:
    print(errore) #stampa l'errore dato da python
    
#CLAUSOLE
    #EXCEPT +  ELSE 
try:
    numero=math.sqrt(64)
except Exception as errore: #Exception -> un generico errore
    print(errore) #stampa l'errore dato da python
else: #eseguito se non ci sono eccezioni
    print(numero)

#FINALLY -> viene eseguito sempre e comunque
try:
    numero=math.sqrt(100)
    print(numero)
except Exception as errore: #Exception -> un generico errore
    print(errore) #stampa l'errore dato da python
finally: #eseguito in ogni caso sia se c'è o non c'è eccezione
    print("TENTATIVO RADICE QUADRATA TERMINATO")

