# matplot permette di realizzare rappresentazioni grafiche
    #con NumPy permette di calcolare meglio i dati da usare nei grafici
#%matplotlib inline
#IMPORTARE IL MODULO
import matplotlib.pyplot as matplot
# import matplot.pyplot as matplot
#Rapresenentiamo un grafico lineare p1(-10,12) , p2(-8,5)......
print('Grafico lineare')
    #sono 2 liste della stessa dimensione
matplot.plot([-10,-8,-3,-2,1,4,8],[12,5,9,14,16,21,8]) 
#dati mostrati sul grafico
matplot.title("Grafico zig zag") #titolo
matplot.xlabel("Ascisse")   #asse x
matplot.ylabel("Ordinate")  #asse y
#Mostra il grafico
matplot.show()

print('Grafico di una curva PARABOLA')
#Grafico di una parabola
matplot.plot([x**2 for x in range(-100,100)]) 
#label e title sono opzionali
matplot.show()

print('Grafico di una curva dritta -> RETTA DECRESCENTE')
#Grafico di una retta con coefficente angolare = -40
matplot.plot([-40*x+2000 for x in range(-100,100)]) 
matplot.show()

print('Grafico di una curva dritta -> RETTA CRESCENTE')
#Grafico di una retta con coefficente angolare = 40
matplot.plot([40*x+3000 for x in range(-100,100)]) 
matplot.show()

print('Uniamo i grafici')
matplot.plot(range(-100,100), [x**2 for x in range(-100,100)],
            range(-100,100),[-40*x+3000 for x in range(-100,100)],
            range(-100,100),[40*x+3000 for x in range(-100,100)]
            )
matplot.title("Grafico con tre curve")
matplot.xlabel("Ascisse")
matplot.ylabel("Risultati delle funzioni")

print('Salviamo il grafico -> gcf()')
figura=matplot.gcf() #
cm=1/2.54 #costante da pollici a centrimetri
figura.set_size_inches(10*cm,12*cm)
#Salva l'immagine dandogli un nome e un formato
matplot.savefig('26.1 - Matplot_grafico_salvato.jpg', format='jpg')

matplot.show()
