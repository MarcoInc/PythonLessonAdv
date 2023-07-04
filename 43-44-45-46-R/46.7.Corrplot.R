#corrplot -> corellogramma -> correlazioni tra variabili
  #pacchetto corrplot

#select -> selezionano le variabili d interesse solitamente numeriche

Cars93_num=Cars93 %>% dplyr::select(Min.Price:MPG.highway,
                                EngineSize:Rev.per.mile,
                                Fuel.tank.capacity:Luggage.room)

#Calcoliamo la matrice di correlazione
  #use -> coppie comlete
#corrplot 
  #type -> osservare solo sotto la diagonale
#La grandezza dei cerchi è direttamente proporzionale alla forza della relazione

library(corrplot)
cor(Cars93_num,use="pairwise.complete.obs") %>% corrplot(type="lower")
                                                         
                                                         