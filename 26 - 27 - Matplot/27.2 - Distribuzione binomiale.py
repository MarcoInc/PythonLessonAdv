import numpy as np
import matplotlib.pyplot as matplot

print("Distribuzione normale binomiale di numeri random -> binomial()")
print("(discreta->assegna una probabilità un intervallo di numeri casuali)")

#Distribuzione delle probabilità di successi di una sequenza binarie indipendenti 
    #es esito positivo o negativo e non entrambi
#Vengono fatti un numero infinito di prove con probabilità di successo pari a 50%
    
#esempio lancio di una moneta lanciata 10 volte con probabilità per lato 50%
n, p = 10, .5  #n->prove, #p->probabilità

#risultato del lancio di una moneta per 10 volte, testato su 1000 ripetizioni
s = np.random.binomial(n, p, 1000)
# n-> numero di prove
# p -> probabilità della distribuzione
# size -> numero di ripetizioni da effettuare

print(sum(s)/10000)
#sum(s) -> somma di tutti i lanci effettuati
# 10000-> numero di lanci totali -> 1000x10

#crea l'istogramma di tutto s
matplot.hist(s)
matplot.show()

