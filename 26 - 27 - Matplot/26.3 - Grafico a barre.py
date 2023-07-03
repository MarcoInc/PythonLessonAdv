
import matplotlib.pyplot as matplot

print('Grafico a barre -> bar')
#Etichette degli spicchi
risposte=['Compere', 'Riposo',
        'TV', 'Parenti',
        'Non so']
#valori inseriti nel grafico
    #il totale deve fare 100
valori=[12,30,38,12,8]  

#matplot.pie -> grafico a torta 
    #lista risposte
    #lista valori
    #stile -> nome colori per intero o abbreviati
matplot.bar(risposte, valori, color=['y','orange','r','blue','g']) 

matplot.show()