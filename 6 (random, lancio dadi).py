import random; #modulo per il random

def lancia():
    return random.randint(1,6) #random tra 1 a 6

def lancia_dadi(n_dadi,n_lanci):
    acc=0 #contiene il valori dei dadi lanciati
    for i in range(n_lanci):
        print("Lancio #",i+1)
        for j in range(n_dadi):
            risultato=lancia();
            print("Il dado ",j+1," ha effettuato ",risultato)
            acc+=risultato
        print("Totale lancio ", acc)
    print()
    print("TOTALE FINALE ", acc,"\n")
    return acc

#crea una nuova iterazione. evita 3 for dentro lancia_dadi
def sessione_lanci(n_ripetizioni,n_dadi,n_lanci):
    acc=0
    for i in range(n_ripetizioni):
        print("Sessione #",i+1)
        acc+=lancia_dadi(n_dadi,n_lanci)
    print("TOTALE SESSIONI", acc)
    return acc

def media_lanci(totale, numero): #calcola la media
    return float(totale/numero)

#costanti globali per il menù
LANCIO=1  #se scelgo 1 ho LANCIO
SESSIONE=2
MEDIA=3
ESCI=4

#stampa la scelte possibili
def visualizza_menu():
    print("1. LANCIO DADI")
    print("2. SESSIONE DI LANCIO DADI")
    print("3. CALCOLO MEDIA")
    print("4. ESCI")

def main():
    acc=0 #contiene il risultato totale
    num_lanci_tot=0 #i lanci totali
    scelta=0 #contiene la scelta dell'utente
    
    while scelta!=ESCI: #se non selezione ESCI
        visualizza_menu()
        scelta=int(input("Fai una scelta\n"))
        if scelta==LANCIO:
            num=int(input("Inserire il numero di dadi\n"))
            lanci=int(input("Inserire il numero di lanci\n"))
            print()
            num_lanci_tot=num*lanci
            acc=lancia_dadi(num,lanci)
        elif scelta==SESSIONE:
            sessioni=int(input("Inserire il numero di sessioni\n"))
            num=int(input("Inserire il numero di dadi\n"))
            lanci=int(input("Inserire il numero di lanci\n"))
            print()
            num_lanci_tot=num*lanci*sessioni
            acc=sessione_lanci(sessioni,num,lanci)
        elif scelta==MEDIA:
            if acc>0:
                print("La media è ", format(media_lanci(acc, num_lanci_tot),".2f"))
                print()
            else:
                print("Non hai effettuato nessuna partita\n")
        elif scelta==ESCI:
            print("Esco dal programma...\n")
        else:
            print("Scelta non valida")    
    
main()

