#FUNZIONI
#funzione void -> non ritorna nulla
def saluta(): 
    print("ciao ")

#funzione con passaggio di parametro per valore
def incrementa(num): #parametro formale diverso dal quello del main
    #num è VARIABILE LOCALE alla funzione -> vista solo nella funzione
    return num+1   #ritorna un valore

#APPROCCIO TOP DOWN -> divido problema grande in sottoproblemi
    #moltiplicazione custom
def moltiplicazione(a,b):
    c=0
    for i in range(b):
        c=c+a
    return c
    #potenza custom
def potenza(a,b):
    c=1
    for i in range(b):
        c=moltiplicazione(c,a)
    return c
#VARIABILE GLOBALE -> scope globale
ciao="CIAO MONDO" 


#LIBRERIE della standard library di python
import math #importo un modulo con funzioni aggiuntive
PI_GRECO=3.14
def seno():
    a=math.sin(PI_GRECO) #sin è una funzione della libreria math
    print(a)

#FUNZIONE MAIN -> esegue tutte le altre
def main():
    global ciao #usato per modificare una variabile globale

    saluta() #invocazione funzione
    
    num=int(input("inserisci numero\n"))
    print(incrementa(num))
    
    saluta()
    
    print(potenza(2,5))
    
    print(ciao) #accedo ad una variabile globale
    ciao="non ti saluto più" #modifico la variabile globale
    print(ciao)

    seno()

main() #eseguo il main



    

