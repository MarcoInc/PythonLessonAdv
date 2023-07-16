#whiteside -> RICHIEDE PACCHETTO MASS
  #whiteside -> è un database di esempio 56 righe e 3 colonne
str(whiteside)
  #Insul -> fattore due livelli prima e dopo isolamento(BEFORE e AFTER)
  #Temp -> temperatura registrata
  #Gas -> consumo settimanale 

#GRAFICO A DISPERISIONE -> scatterplot -> adatta per 2 variabili numeriche
  #Tempo sull'asse x -> etichettata con Temperatura esterna
  #Gas sull'asse y  -> etichettata con Consumo di gas
plot(x=whiteside$Temp, y=whiteside$Gas,
     xlab = "Temperatura esterna",
     ylab="Consumo di gas")

#Cars93 -> è un database esempio 93x27
str(Cars93)
#Possiamo anche evitare di inserire x e y 
  #Max.Price -> Y massima sarà il Max di Price
plot(Cars93$Price,Cars93$Max.Price,
    pch=17,                #pch -> forma iconcine
    col="gray")            #col -> colore iconcine

#AGGIUNGERE PUNTINI -> points
  #Min.Price -> minimo Price rilevato come singolo point
points(Cars93$Price,Cars93$Min.Price,
    pch=16,                
    col="black")  

#RETTA DI TENDENZA -> abine(a,b,lty)
  #a -> intercetta
  #b -> coefficente di regressione
  #lty -> forma della retta
abline(a=0,b=1,lty=2)


#ISOLARE I DATI
wb=whiteside$Insul=="Before"
wb=whiteside[wb,]
wa=whiteside$Insul=="After"
wa=whiteside[wa,]

#Prima -> grigio
plot(x=wb$Temp,y=wb$Gas,pch=17,col="gray")
#Dopo -> nero
points(x=wa$Temp,y=wa$Gas,pch=16,col="black")


#VISUALIZZARE PIU' GRAFICI INSIEME->par(mfrow=c(RIGHE,COLONNE))
  #Visualizza i successivi grafici in 2 righe e 1 colonna
par(mfrow=c(2,1))
    #1 riga 2 colonne
par(mfrow=c(1,2))

plot(Cars93$Price,Cars93$Max.Price,pch=17,  col="gray")         
plot(Cars93$MPG.city,Cars93$Max.Price,pch=16,  col="black")   

  #per ripristinare la vista -> 1 riga 1 colonna
par(mfrow=c(1,1))

#Animals -> database esempio -> 25 animali
  #body -> peso corpo
  #brain -> peso cervello
str(Animals)

par(mfrow=c(1,2))
plot(Animals$body, Animals$brain)
title("Original plot") #etichetta grafico

plot(Animals$body, Animals$brain, log="xy") #log log plot
title("Log-Log plot")
par(mfrow=c(1,1))



