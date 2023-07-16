import re
#Aggiungendo GRUPPI ad un modello, si possono isolare le 
# parti del testo corrispondenti crando così un PARSER
#PARSER -> analizzatore mofologico sintattico di un testo

#Diversi sottogruppi corrispondono a differenti componenti
#Gruppi definiti con (   )

print("PARSER")
#gruppo -> qualunque sequenza di ab che parte dall'inizio
pattern=re.compile('(ab)*')
print(pattern.match('abababaabbaabb'))

print("-> Indici corrispondenti")
pattern=re.compile('(a)b')
        #indice 0 -> tutto il gruppo catturato (a)b  -> ovvero tutto
        #indice 1 -> il primo gruppo catturato (a)
m=pattern.match('ab')
print(m.group()) #tutta la cattura  (a)b
#sono uguali
print(m.group(0)) #tutta la cattura (a)b
print(m.group(1)) #la prima cattura (a)
print()

print("->Più gruppi")

pattern=re.compile('(a(b)c)d')
        #indice 0 -> tutto il gruppo catturato (a(b)c)d  
        #indice 1 ->  il primo  gruppo catturato (a(b)c)
        #indice 2 -> il secondo gruppo catturato (b) -> il più interno
m=pattern.match('abcd')
print(m.group(0)) #tutta la cattura (a(b)c)d  
print(m.group(1)) #la prima cattura (a(b)c)
print(m.group(2)) #la prima cattura (b)

print("->Più gruppi a tupla")
#posso passare più gruppi 
    # ottengo una tupla
print(m.group(2,1,2)) 

print("->Groups")
pattern=re.compile('(a(b)c)d')
m=pattern.match('abcd')
#ritorna una tupla con tutti i gruppi a partire dal primo in poi
print(m.groups()) #gruppo 1,2 -> manca lo 0

print("PARAMETRI DI UN MODELLO")
#trova tutte le parole doppie
    #GRUPPO 1
        #\b -> limite parola
        #\w+ -> 1 o più caratteri alfanumerici
    #GRUPPO 0
        #\s+ ->seguita da 1 o più spazi
        #\1 -> PARAMETRO
            #si riferisce al primo gruppo (\b\w+)
            #quindi stringhe catturate dal primo gruppo
pattern=re.compile(r'(\b\w+)\s+\1')
print(pattern.search('RE trovata nella nella stringa'))
print("NOMI AI GRUPPI ?P<parola>")
#?P<nome_grupp>.. -> da richiamare dopo
    #cerca parola con 1 o più caratteri seguito da un fine parola
pattern=re.compile(r'(?P<parola>\w+\b)') #nome -> parola
stringa=pattern.search('((( Molta punteggiatura)))')
print(stringa.group('parola')) #il nome del gruppo
print(stringa.group(1))

print("-> Ripresa gruppo dal nome ?P<NOME> -> (?P=NOME)")

#Do un nome ad un gruppo
    #al posto di \1
    #lo richiamo successivamente con (?P=parola)
pattern=re.compile(r'(?P<parola>\b\w+)\s+(?P=parola)') #nome -> parola
risultato=pattern.search('RE trovata nella nella stringa')
print(risultato) #il nome del gruppo
print(risultato.group())

print("-> Più gruppi con nome")

stringa = 'Questa è una porzione di testo -- con punteggiatura.'
for pattern in [ r'^(?P<prima_parola>\w+)', # ^ ->inizio \w+-> seguita da caratteri 
                r'(?P<ultima_parola>\w+)\S*$',  #\w->più caratteri 
                                                #\S seguito da non punteggiatura
                                                #$ -> fine
                r'(?P<parola_t>\bt\w+)\W+(?P<altra_parola>\w+)',#\b limite della parola
                                                                    #t-> che inizia per t
                                                                #\w+ seguita da più caratteri
                                                                #\W+ seguita da più non caratteri
                                                                #seguito da altra parola
                                                                #\w+ seguito da più caratteri
                r'(?P<finisce_con_o>\w+o)\b', #finisce per o
                ]:
    pattern_compilato = re.compile(pattern)
    match = pattern_compilato.search(stringa)
    print("Corrispondenza",pattern)
    print("Groups:",match.groups())
    print()
    
print("GRUPPO SENZA CATTURA ?:")
#come quelli catturati ma non avviene nessun recupero
print("->Con cattura")
#CON CATTURA -> una lettera tra abc 
stringa=re.match("([abc])+","abc")
print(stringa) #lo trova
print(stringa.groups()) #e lo prende -> ritorna l'ultimo gruppo -> c
print("-> Senza cattura ?:")
#SENZA CATTURA -> una lettera tra abc ma senza cattura
stringa=re.match("(?:[abc])+","abc")
print(stringa) #lo trova
print(stringa.groups()) #ma non lo prende



