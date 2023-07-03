
#Ordinamento crescente e decrescente
    #confronto tra coppie adiacenti in sequenza
        #se il primo è più piccolo del secondo si va alla coppia successiva
        #altrimenti si invertono
    #termina 
        # se sono tutti elementi bolla -> da ordinare
        # assenze di scambi -> già ordinati
def bubble_sort(l):
    n = len(l)

    for i in range(n-1): #scorre il vettore
        for j in range(0, n-i-1): #coppie consecutive
            if l[j] > l[j + 1]: #confronto le coppie
                tmp = l[j]  #scambio i numeri
                l[j] = l[j+1]
                l[j+1] = tmp
                #forma alternativa per lo scambio in Python
                #l[j], l[j + 1] = l[j + 1], l[j]
    return l

def bubble_sort_ottimizzato(l): #usiamo un flag e un ciclo while
    n = len(l)
    i = 0
    scambio = True #per entrare nel while
    while i<n-1 and scambio: #si sta dentro se si è fatto uno scambio e se sto dentro
        scambio = False   #rimane false se non avviene nessun scambio
        for j in range(0, n-i-1):
            if l[j] > l[j + 1]: #confronto le coppie
                tmp = l[j]      #scambio i numeri
                l[j] = l[j+1]
                l[j+1] =tmp
                scambio = True #se viene fatto lo scambio
        i+=1 #vado al valore successivo
    return l

def main():
    print("Bubble sort ")
    l = list(range(10,0,-1)) #numeri da 10 a 1
    print("Lista originale:",l)
    l = bubble_sort(l)
    print("Lista ordinata in modo crescente:",l)
    
    print("Bubble sort ottimizzato")
    l = [3,15,8,6,1,4,12,9]
    print("Lista originale:",l)
    l = bubble_sort_ottimizzato(l)
    print("Lista ordinata in modo crescente:",l)

main()
