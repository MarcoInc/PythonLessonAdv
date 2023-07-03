
import matplotlib.pyplot as matplot

print('Grafico a torta -> pie')
#Etichette degli spicchi
risposte=['Faccio compere', 'Riposo',
        'Guardo la TV', 'Faccio visita ai parenti',
        'Non risponde']
#valori inseriti nel grafico
    #il totale deve fare 100
valori=[12,30,38,12,8]  
#explode -> è una tupla che determina la distanza tra gli spicchi
explode=(0,0.1,0.1,0,0)

#matplot.pie -> grafico a torta 
    #lista dei valori
    #stile
    #lista risposte
    #shadow=True -> effetto ombreggiatura
    #startangle -> angolo rotazione
matplot.pie(valori, explode, risposte, shadow=True, startangle=50) 

#RIQUADRO LEGENDA 
    #Singola etichetta è generata con 
        # list comprehensions 
        # formatted string literals -> uso di f e {variabile} <-String interpolation
            #a -> singola risposta
            #b -> singolo valore tra (PARENTESI)
            #title -> titolo legenda
            #bbox_to_anchor-> distanza dall'inizio dell'area del grafico
            #loc -> in basso a destra
matplot.legend([f'{a} ({b}%)' for a,b in zip(risposte, valori)],
            title="Risposte dei nostri ascoltatori",
            bbox_to_anchor=(1.8,0),
            loc='lower right')

matplot.show()

