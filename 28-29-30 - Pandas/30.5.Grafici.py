import pandas as pd
import numpy as np
import matplotlib.pyplot as matplot

#Fare i grafici su Pandas è più semplice rispetto a NumPy
    #fa uso della libreria matplot
print("GRAFICO CON PANDAS + MATPLOT")
dati=pd.read_csv('persone.csv', delimiter=';')
dati['peso'].plot(kind='line')
#kind= ->tipo di grafico
    #line -> grafico lineare

#Una linea che si riferisce alla media mobile sul peso su 2 giorni
r=dati['peso'].rolling(window=2).mean() #è una series
r.plot(kind='line')

matplot.show() #mostra due grafici

