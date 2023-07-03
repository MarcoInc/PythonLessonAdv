import matplotlib.pyplot as matplot
import random as rnd #rnd è un alias
#Un grafico con dei puntini in determinate coordinate
print('Grafico scatter -> scatter')

# 30 coordinate [X] e [Y] sono generate a random
    #valori da 0 a 10 
matplot.scatter([rnd.random()*10 for x in range(30)],
                [rnd.random()*10 for x in range(30)]) 

matplot.show()

