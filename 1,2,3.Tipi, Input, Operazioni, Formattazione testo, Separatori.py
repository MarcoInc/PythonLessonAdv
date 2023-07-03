print("Ciao")  #stampa

#TIPO -> ogni tipo è una classe!
print("TIPI") 
hello="ciao"
print(type(hello)) #ritorna il tipo
print(type(3)) 
virgola=3.14
print(type(virgola))
virgInt=virgola*3
print(type(virgInt)) #risulato è un float
print("") #rigo vuoto

#INPUT DA TASTIERA
nome=input('Come ti chiami?') #input torna una stringa
eta=int(input('Anni?')) #nested function call. facciamo un casting
print(nome," di ",eta," anni") #stampare più cose
print("") 

#OPERAZIONI 
print(3+5) #somma   ->priorità bassa
print(5-3) #sottrazione     ->priorità bassa
print(5*5) #moltiplicazione     ->priorità media
print(10/5) #divisione  ->priorità media
print(10//5) #divisione alternativa     ->priorità media
print(10%4) #resto  ->priorità media
print(10**2) #esponente     ->priorità alta
#le parentesi hanno più precedenza
saluta=hello+" "+nome #concatenazione stringhe
print(saluta)
print("")

#FORMATTAZIONE OUTPUT
print("ciao","mondo", sep=',') #separatore dei valori è ,
print("ciao","mondo", end=" fine") #cosa mettere alla fine della print

print("ciao","\tmondo") #tabulazione orrizontale
print("\'ciao","mondo\'")  #vigolette singole
print("\"ciao","mondo\"")  #vigolette doppie
print("""ciao "mondo" bello""")  #tripe virgolette->stampa virgolette interne
print("ciao \\mondo\\ bello")  #doppie backslash->stampa backslash
print("")


#FORMATTAZIONE NUMERI
print(format(123456789.00000009, ".3f")) #3 cifre decimali le altre saltano
print(format(123456789.00000009, "e")) #notazione scientifica
print(format(123456789.00000009, ".2e")) #notazione scientifica con 2 cifre decimali

#separatore centinaia, migliaia....
print(format(123456789.00000009, "15,.2f")) #usa 15 spazi in totale con separatore , incluso
print(format(123456789.00000009, "15.2f")) #usa 15 spazi in totale senza separatore

print(format(0.5, ".2%")) #formato percentuale con 2 cifre
print(format(123, "d")) #formato intero
print(format(123456789, ",d")) #formato intero con separatore ,
print(format(123456, "10d")) #interi in uno spazio da 10 senza separatore
print(format(123456, "10,d")) #10 interi e i rimanenti spazi con separatore











