import numpy as np
import matplotlib.pyplot as matplot
import statistics as s

voti=[4,8,8,8,9,6,9,7,9,8,3]
print(voti)

matplot.plot(voti)
matplot.show()

#METODI BUILD IN DI STATITCS
print("METODI STATITICS")

#mean() -> MEDIA -> somma dei valori diviso la numerosità
    #è influenzata dai valori OUTLIER -> valori estremi
print("Media -> s.mean()")
print(s.mean(voti))

#median() -> Mediana -> -> il valore dell'elemento centrale
    #scende di molto se si levono valori OUTLIER -> valori estremi
print("Mediana -> s.median()")
print(s.median(voti))

#variance() -> varianza
print("Varianza -> s.variance()")
print(s.variance(voti))

#stdev()  -> deviazione standard -> radice quadrata della varianza
print("Deviazione standard CAMPIONE-> s.stdev()")
print(s.stdev(voti))
#oppure con la radice quadrata
print(np.sqrt(s.variance(voti)))

#mode() -> moda
print("Moda -> mode()")
print(s.mode(voti))

print("METODI NUMPY")

#sum() -> somma tutti i valori
print("Somma valori -> np.sum()")
print(np.sum(voti))

#min() -> valore più basso della sequenza
print("Minimo -> np.min()")
print(np.min(voti))

#max() -> valore più alto della sequenza
print("Massimo -> np.max()")
print(np.max(voti))

print("Range -> np.max()-np.min")
print(np.max(voti)-np.min(voti))

#std()  -> deviazione standard -> radice quadrata della varianza
print("Deviazione standard POPOLAZIONE-> np.std(voti)")
print(np.std(voti))
print("Deviazione standard CAMPIONE-> np.std(voti, ddof=1)")
print(np.std(voti, ddof=1))

#cumsum() -> SOMMA COMULATIVA   
    #ritorna un array dove i valori sono via via sommati
print("Somma comulativa -> np.cumsum()")
print(np.cumsum(voti))

#cumprod() -> SOMMA COMULATIVA   
    #ritorna un array dove i valori sono via via moltiplicati
print("Prodotto comulativo -> np.cumprod()")
print(np.cumprod(voti))





