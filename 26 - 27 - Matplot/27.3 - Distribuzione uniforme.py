import numpy as np
import matplotlib.pyplot as matplot
import random as rnd #rnd è un alias

print("Distribuzione normale uniforme di numeri random -> uniform()")
print("(discreta e continua)")

#Tutti i risultati sono ugualmente probabli
#rappresentano variabili casuali numerici solo se si conosce il loro intervallo
rnd.seed(1) #seed

print("Size = None")
uniforme1=np.random.uniform(low=0.0, high=10.0, size=None)
    #low->estermo inferiore dell'intervallo
    #high->estermo superiore dell'intervallo
    #size->numero dei numeri da generare
        #None -> ne estrae 1
print("Numeri estratti -> size=None")
print(uniforme1)  #unico numero estratto
matplot.plot(uniforme1)
matplot.show()

print("Size = 100")
uniforme100=np.random.uniform(low=0.0, high=10.0, size=100)
#ne estrae 100
print("Numeri estratti")
print(uniforme100)

print("Grafico lineare")
#Grafico lineare
matplot.plot(uniforme100)
matplot.show()

print("Istogramma")
#Istogramma
matplot.hist(uniforme100)
matplot.show()

print("Size = 1000000")
uniforme1000=np.random.uniform(low=0.0, high=10.0, size=1000000)
#ne estrae 1000
#Più è grande il numero e più si avvicina all'onda quadra
matplot.hist(uniforme1000)
matplot.show()

print("Con randint -> interi")
print("Size = 100")

rnd.seed(2) #seed
x=range(100)
#randint estrae solo numeri interi
numeri=[rnd.randint(0,10) for x in range(100)]
matplot.scatter(x,numeri)
matplot.show()

print("Size = 1000000")

#diventa più lineare/quadratica
x=range(1000000)
#randint estrae solo numeri interi
numeri=[rnd.randint(0,10) for x in range(1000000)]
matplot.scatter(x,numeri)
matplot.show()