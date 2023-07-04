#BOXPLOT -> verifica la dispersione di una determinata variabile numrica

boxplot(Cars93$Price)

#Price può essere suddivisa in una seconda variabile fattoriale AirBags
boxplot(Price ~ AirBags, data=Cars93)

#Personalizzare
  #varwith -> TRUE -> tiene conto della larghezza 
    #tiene conto ci della grandezza di Cylinders
boxplot(Price ~ Cylinders, data=Cars93 varwidth=TRUE)

