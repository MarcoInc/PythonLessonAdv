#ISTOGRAMMA -> distribuzione di frequenza variabile continua
  #Necessario raggruppamento in classe

#Si basa sulla temperatura
  #Eticchetta il grafico
hist(whiteside$Temp, main="Temperatura")

#Personalizzare istogramma
  #breaks -> numero di classi
  #col -> colore 
  #main -> titolo grafico
hist(whiteside$Temp, main="Temperatura", breaks=30, col="red")

#FUNZIONE DI DENSITA'
  #Tramite colonne -> truehist
    #nbis -> numero colonne
truehist(whiteside$Temp, nbins=10, col="green")

  #Tramite grafico a linee density
    #lines ->crea la linea
density(whiteside$Temp) %>% lines()
density(whiteside$Temp) %>% class() #-> classe density



