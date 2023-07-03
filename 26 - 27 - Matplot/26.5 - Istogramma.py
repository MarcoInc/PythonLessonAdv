import matplotlib.pyplot as matplot
import random as rnd #rnd è un alias
#Un grafico con dei puntini in determinate coordinate
print('Istogramma -> hist')

#genera 20 numeri random da 1 a 10
valori=[rnd.randint(1,10) for x in range(20)]

#Inserisco i valori nell'istogramma
matplot.hist(valori)
print(valori)
matplot.show()

#altri grafici
    #barh() -> grafico a barre orrizontali
    #boxplot -> grafico a scatola e baffi
    #errorbar -> grafico a barre di errore
    # loglog()  -> grafico log-log
    # semilogx() -> grafico log in x
    # semilogy() -> grafico log in y
    # plot_dates() -> grafico per date
    # polar() -> grafico polare
    # step() -> grafico a passi
