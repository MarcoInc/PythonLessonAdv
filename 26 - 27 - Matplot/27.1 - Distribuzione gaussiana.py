import matplotlib.pyplot as matplot
import numpy as np
import seaborn as sb

import random as rnd #rnd è un alias
#FUNZIONE DI MASSA DELLA PROBABILITA' ->PMF -> DISTRIBUZIONI DISCRETE
#FUNZIONE DI DENSITA' DELLA PROBABILITA' ->PDF -> DISTRIBUZIONI CONTINUE


print("Distribuzione normale gaussiana di numeri random -> normal()")
print("(continua->assegna una probabilità a ogni possibile numero casuale)")
#Cosidetto grafico a campana

sb.set()
rnd.seed(2) #seed

mu, sigma=0.0,0.1  #media=0 e deviazione standard=0.0

# genera 1000 numeri secondo una distribuzione normale con media e sigma
s=np.random.normal(mu,sigma,1000)

#Alternativa -> randn -> genera random secondo una distribuzione gaussiana
#s=np.random.randn(1000)   #ne genera 1000
#essa equivale a normal() ma con i seguenti paramentri
    #loc=0.0 -> MEDIA . di default è 0.0
    # scale=1.0 -> DEVIAZIONE STANDARD (Spread) -> deve essere NON NEGATIVO
    # shape=size -> Numero di numeri da generare
      
#s conterrà tutti e 1000 numeri random 

print("Media della sequenza di numeri (no.means(s))", np.mean(s))
print("Deviazione standard della sequenza (np.std(s,ddof=1))", np.std(s,ddof=1))


count,bins,ignored=matplot.hist(s,30,density=True)
    #count -> conterrà 30 intervalli dati dai 1000 numeri estratti
    #bins=30 -> numero di intervalli da generare
    #density=True ogni intervallo visualizzerar il conteggio grezzo 
        #del bin diviso per il numero totale di conteggi e la larghezza del bin 
        #in modo tale che l'area sotto l'istogramma si integri a 1
        
#Funzione di densità della probabilità (Linea rossa)
matplot.plot(bins,1/(sigma*np.sqrt(2*np.pi))*
    np.exp(-(bins-mu)**2 /(2*sigma**2)),
    linewidth=2,color='r')

matplot.show()