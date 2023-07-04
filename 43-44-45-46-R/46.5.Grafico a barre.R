#GRAFICO A BARRE -> Variabili di tipo qualitativo
  #studio delle frequenze
#Serve
  #distribuzione di frequenza -> funzione table
  #vettore con le osservazioni

#CREAZIONE GRAFICO A BARRE
tabella=table(whiteside$Insul)
  #Insul ha due categorie, After e Before
tabella
barplot(tabella) #-> grafico a barre

#Personalizzare barplot
barplot(tabella,las=1, cex.names = 1.2,horiz = TRUE,col="grey") #-> grafico a barre
  #horiz = TRUE -> ruotato orizzontale
  #las=1 -> etichettato con etichette perpendicolari agli assi
  #cex.names=1.2 -> etichette più grandi
  #col -> colore