import matplotlib.pyplot as matplot
import numpy as np
import random as rnd #rnd è un alias
# Ogni grafico ha vari elementi grafici
    #grafico -> rappresenta i dati
    #asse -> contiene gli i dati e imposta il sistema di coordinate
    #titolo -> nome del grafico
    #etichetta asse x e asse y nell'asse x e y
    #legenda -> descrizione del grafico
    #COMPONENTI COMUNI EDITABILI:
        #segni ed etichette dei segni -> punti di riferimento
        #linee del grafico -> le line tracciate con i dati
        #indicatori -> pittogrammi che contrassegnano i dati
        #cornici -> linee che delimitano l'area del grafico
# PYPLOT può modificare aspetti del grafico
    #xscale(scala) e yscale(scala) ->scala degli assi x e y
    #xlim(xmin,xmax) e ylim(ymin,ymax) >- limiti degli assi x e y
    #aggiungere
        ##annotate -> note
        #arrow() ->frecce
        #legend() -> legenda
    #grid() -> imposta una griglia

#Leggo i dati da un file
dati1 = np.genfromtxt('26.7 - dati_finanziari.txt')
x = range(len(dati1))
rumore = 500 * np.random.normal(size = len(dati1))
dati2 = dati1-2000-rumore
dati3 = dati1+2000+rumore

#è la lista contiene i 3 dati ottenuti
d = [dati1, dati2, dati3]

giorni = ["Giorno 1", "Giorno 2", "Giorno 3"]
matplot.plot(x,dati1,x,dati2,x,dati3)
for dati in d:
    #annotate -> annotazioni
    matplot.annotate(text="Picco", xy=(dati.argmax(), dati.max()),  #picco valore massimo
                    xytext =(dati.argmax()+1, dati.max()+1000),  #posizione del testo
                    arrowprops= {"facecolor":"black", "shrink":0.2}) #frecce
#Legenda dei giorni
matplot.legend(giorni)
#Altri dati
matplot.title("Andamento del titolo") #
matplot.xlabel("Ora")
matplot.ylabel("Valore")

#linee per aumentare la leggibilità del grafico
    #axhline -> linea orrizontale
matplot.axhline(y=3000, color = 'orange', linestyle ='--')
    #axvline -> linea verticale
matplot.axvline(x=5, color = 'black', linestyle ='-')

matplot.show()
