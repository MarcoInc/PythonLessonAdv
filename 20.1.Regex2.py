import re


print("FINDALL")
#trova tutte le occorenze e non si ferma alla prima e mette in una lista
#findall(pattern, string,flags=0)
stringa="123456 Questa strinGa ha almeno 1234 nuMeri"
#cerca tutte le stringhe composta da almeno un carattere alfabetico
risultato=re.findall(r"[a-z]+",stringa, re.I)
print(risultato)
#Con distinsione maiuscolo e minuscolo
risultato=re.findall(r"[a-z]+",stringa)
print(risultato)

print("->Quantificatori GREEDY .* ")
#I quantificatori sono GREEDY->Golosi
    #cercano l'occorenza più grande possibile
stringa='class="pluto" id="pippo"'
        #cerca tutte le parole tra doppi apici " "
risultato=re.findall(r'".*"',stringa,re.I) #prende tra il primo " all'ultimo"
                                        #senza saltare id=
print(risultato) #manca class ma prende id=

print("->Fix a non GREEDY .*?")
#ora è NON GREEDY
    #il ? che ne cerca almeno ?
risultato=re.findall(r'".*?"',stringa,re.I) 
print(risultato) #manca class ma prende id=

print("FINDITER")
#come findall ma restituisce anche l'indice
    # finditer(pattern,stringa,flags=0)
    #funzioni
        # start() ->   ritorna l'indice dell'inizio del gruppo
        # end() ->   ritorna l'indice della fine del gruppo
        # group() -> framento trovato -> sottostringa
            #span=(8, 12), match='1231' 
            #span(start,end), match=group

stringa="Vado al mare 4 ore al giorno. Passeggio 2 ore al giorno"
pattern=r'[0-9]'
for risultato in re.finditer(pattern,stringa):
    start=risultato.start() #indice iniziale
    end=risultato.end()     #indice finale
    group=risultato.group() #sottostringa trovata
    print(group, " trovata in posizione [",start," , ",end," ]")

print("SUB")
#cerca il pattern in stringa e la sostituisce
    #sub(patter,stostituita, stringa, flags=0)
stringa="123456 Questa strinGa ha almeno 1234 nuMeri 12851 bello 7565 fa caldo"
#cerca tutte le sottostringe alfabetiche maiuscole o minuscole con uno spazio
#e sostituisce con [...]
risultato=re.sub(r"[A-zA-z ]+","[...]",stringa)
print(risultato)
print("SUB+Count")
    #limita le sostituzioni
                                            #al massimo 2 sostituzioni
risultato=re.sub(r"[A-zA-z ]+","[...]",stringa,count=2)
print(risultato)

print("SUBN") #come SUB ma ritorna quante occorenze ha incontrato
risultato=re.subn(r"[A-zA-z ]+","[...]",stringa)
print(risultato)


print("PATTERN PRE COMPILATI") #come SUB ma ritorna quante occorenze ha incontrato
#PATTERN -> vengono compilati e convertite in modelli
            # sono oggetti che contengono funzioni per far fare roba
    #Compilazione con compile()
#posso usare il pattern dove voglio
    #qualsiasi sequenza con almeno 1 numero e altri numeri a seguire
pattern_precompilato=re.compile(r"\d+")
#trova il primo \d+ che trova
risultato=pattern_precompilato.search("lalalal 1231 lalala 12316")
print(risultato)#trova il primo 1231 che trova
print(risultato.group())
risultato=pattern_precompilato.search("6677lalalal 1231 lalala 12316")
print(risultato)
print(risultato.group())

print("ASSERSIONI")
#ASSERZIONI -> regex più complesse
print("-> Lookahead positiva (?=pattern)")
    #Lookahed positiva -> (?=pattern)
        # è valido solo se quello a sinistra 
        # è preceduto da quello a destra
stringa="Paolo Rossi Paolo Verdi Paolo Bianchi"
                #prende solo Paolo se Paolo è seguito da Rossi
risultato=re.findall(r'Paolo (?=Rossi)',stringa,re.I)
print(risultato)

print("-> Lookahead negativa (?!pattern)")
    #Lookahed negativa -> (?!pattern)
        # è valido solo se quello a sinistra 
        # non è preceduto da quello a destra
stringa="Paolo Rossi Paolo Verdi Paolo Bianchi"
                #prende solo Paolo se non è seguito da Rossi
risultato=re.findall(r'Paolo (?!Rossi)',stringa,re.I)
print(risultato)

print("-> Lookanbehind positiva (?<=pattern)") #come lookahead positiva ma al contrario
    #Lookanbehind positiva -> (?<=pattern)
        # è valido solo se quello a destra 
        # è preceduto da quello a sinistra
stringa="cesto pasto fasto pesto costo"
    #prendo sto solo se è preceduto da a
print(re.findall(r'(\w+(?<=a)sto)',stringa))

print("-> Lookanbehind negativa (?<!pattern)") #come lookahead negativa ma al contrario
    #Lookanbehind negativa -> (?<!pattern)
        # è valido solo se quello a destra 
        # non è preceduto da quello a sinistra
stringa="cesto pasto fasto pesto costo"
    #prendo sto solo se non è preceduto da a
print(re.findall(r'(\w+(?<!a)sto)',stringa))




