#Permette l'uso delle regex
import re

#base per usare un pattern come regex
# pattern_compilato=re.compile(pattern,flags=0)
#FLAG
    # re.I -> ignora distinsione caratteri maiuscoli e minuscoli
    # re.L  -> interpreta le parole rispetto al locale corrente
    # re.M -> attiva la modalità multiriga e consente di usare ^ e $ per inizio e fine riga
    # re.U  -> interpreta i caratteri come set di caratteri Unicode
    # re.X  -> ignora gli spazi bianchi
#PATTERN
    # re.function(pattern_grezzo,..)
    # patterm_compilato.function(..)

print('SPLIT')
#SPLIT -> divide una stringa in base ad un pattern e lo mette in lista
    # split(pattern,stringa,maxplit=0,flags=0)
                            #split massimi -> se 0 illimitato
splitted=re.split(r"\W+","Ciao, mondo!")  #splitta se trova un carattere non alfanumerico
print(splitted)
print('->Split limitato')
stringa="Oggi è proprio una giornata molto calda"
#splitta al massimo 3 volte ad ogni spazio che incontra
risultato=re.split('\s+',stringa,3) #al terzo riporta tutta la stringa rimanente
print(risultato)


print('MATCH')
#MATCH -> controlla se l'inzio della stringa corrisponde al patter
# e ritorna l'oggetto corrispondente se lo trova, altrimenti None
    #se trovato si usano le funzioni 
    # start() ->   ritorna l'indice dell'inizio del gruppo
    # end() ->   ritorna l'indice della fine del gruppo
    # group() -> framento trovato -> sottostringa
        #usato ma senza corrispondenza -> Eccezione -> AttributeError
    #span=(8, 12), match='1231' 
    #span(start,end), match=group

print('->Un solo numero al inizio')
#cerca UN NUMERO ->\d all'inizio
stringa=re.match(r"\d","123 inizia con numero")
print(stringa) #ritorna un oggetto
#per stampare la stringa trovata
print(stringa.group())

print('->Uno o più numeri al inizio')
#cerca UN NUMERO O PIU' NUMERI->\d+ all'inizio
stringa=re.match(r"\d+","123 inizia con numero")
print(stringa) #ritorna un oggetto
print(stringa.group())

#Inizia con lettere
stringa=re.match(r"\d+","inizia con lettere")
print(stringa) #Non c'è match quindi non usiamo group

print('->Parola inizio stringa')
stringa="Espressioni regolari - Programmazione Python"
#cerca espressioni in stringa
    #flag-> re.I -> ignora minuscoli e maiuscoli
risultato=re.match(r"espressioni",stringa, re.I)
print(risultato.group())

print('->Almeno un carattere')
#Qualsiasi carattere, rappresentato da .(punto), ripetuto da 0 a N volte
risultato=re.match(r".*",stringa, re.I)
print(risultato.group()) #la stampa tutta

print('->Cerca almeno uno ad inizio')
#Trova almeno un carattere -> si ferma appena ne trova uno
risultato=re.match(r".?",stringa, re.I)
print(risultato.group()) #stampa il primo

print('->Sequenza numeri con simboli')
stringa="320/1256549 - numero di Mario Rossi"
#una qualsiasi sequenza di 3 numeri seguita da / o - seguita da 7 numeri
risultato=re.match(r"\d{3}[-/]\d{7}",stringa, re.I)
print(risultato.group()) #stampa solo il numero con /

print('SEARCH')
#SEARCH -> come match ma per qualunque parte della stringa
    #può risultatoessere usato in un if
stringa=("123 Questa inizia con numero e ha 1234 lettere")
#ritorna la prima occorenza di sequenza di caratteri da a-z minuscoli
print('->con flag re.I')
    #con il flag re.I
        #non c'è distinsione tra maiuscolo e minuscole
risultato=re.search(r"[a-z]+",stringa,re.I)
print(risultato)
print(risultato.group())
print('->senza flag re.I')
    #omettiamo il flag re.I
        #distinguiamo maiuscole e minuscole
risultato=re.search(r"[a-z]+",stringa) #ignora la Q maiuscola
print(risultato)
print(risultato.group())

print('->SEARCH vs MATCH')
stringa="Corso sulle Espressioni regolari - Programmazione Python"
#cerca programmazione in stringa senza distinsioni di minuscole e maiuscole
risultatoSearch=re.search(r"programmazione",stringa, re.I)
print(risultatoSearch)
print(risultatoSearch.group())
#vs match -> programmazione non sta all'inizio quindi non la trova
risultatoMatch=re.match(r"programmazione",stringa, re.I)
print(risultatoMatch)

print('->SEARCH + ^')
#Search all'inizio della stringa con -> ^
risultatoSearch=re.search(r"^programmazione",stringa, re.I)
print(risultatoSearch) #non lo trova, non sta all'inzio
risultatoSearch=re.search(r"^corso",stringa, re.I)
print(risultatoSearch) #lo trova, sta all'inizio
print(risultatoSearch.group())

print("PIU' FLAG INSIEME")
# re.I -> senza distinsione tra maiuscole e minuscole
# re.M -> ricerca dall'inizio
stringa=re.search('I',"^Ciao", re.I | re.M)
print(stringa) #lo trova, sta all'inizio
print(stringa.group())





