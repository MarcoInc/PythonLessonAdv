#Ordinamento per selezione crescente o decrescente
    #la sequenza viene divisa in:
        #sottoquenza ordinata -> prime posizione lista
        #sottosequenza da ordinare -> parte restante dell'lista
            # [2,3,10,15,11,1,2,5,4]
        # ->[ 2,3,10,15]    [11,1,2,5,4]
    #la parte ordinata cresce ogni volta, la restante decresce
    #seleziona di volta in volta il numero minore della sequenza di partenza
    # e lo sposa nella sequenza ordinata


def selection_sort(l):
    n = len(l)
    for i in range(n): #scorre l'lista
        ind_min = i   #memorizza l'indice del minimo
        for j in range(i+1, n):   #scorre la parte non ordinata a dx
            if l[ind_min] > l[j]:  #trova il più piccolo
                ind_min = j     #indice più piccolo
        if i!=ind_min:  #se c'è un elemento più piccolo in posizione i, quindi i non è ordinato
            l[i], l[ind_min] = l[ind_min], l[i] #scambio l[i] con l[ind_min] 
        print(l)
    return l

def main():
    l = [3,15,8,6,1,4,12,9]
    print("Lista originale:",l)
    l = selection_sort(l)
    print("Lista ordinata in modo crescente:",l)


main()
