#Fattori -> vettori di tipo categorico che hanno un numero 
#limitato di livelli
#livelli -> valori unici che non si ripetono


sesso=c("Uomo","Donna","Uomo")
class(sesso)

#trasforma un vettore in un fattore
sesso=factor(sesso)
sesso
#mostra i livelli del fattore
levels(sesso) #due stringhe

#tabella di frequenza assolute
  #ordine alfabetico
table(sesso) 

#4 livelli
speed=c("lento","super",
        "veloce","veloce",
        "normale","normale")
table(speed) #tabella di frequenze -> in ordine alfabetico

#Ricreiamo il fattore ma con livelli in ordine logico
speed=factor(speed,
             ordered = TRUE,
             levels = c("lento","super",
                        "veloce","normale"))
#levels -> impostiamo un ordine dei livelli
speed #mostra l'ordinamento
table(speed) #mostra la le frequenze assolute nell'ordine impostato
class(speed)  #è "ordered" "factor"

#0-> respinto , 1 -> passato
risulati_test=c(0,0,0,1,1,1,1,0,1)
table(risulati_test)
#cambiamo le etichette
risulati_test=factor(risulati_test,
                     labels=c("Respinto","Passato"))
# labels -> specifichiamo le nuove etichette
  #etichette impostate per l'ordine dei valori
table(risulati_test)


assunzioni=c(0,0,0,1,1)
table(assunzioni)
#Ordiniamo ma specififichiamo l'etichette dei livelli
assunzioni=factor(assunzioni,
                     ordered=TRUE,
                     levels=c("1","0"),
                     labels=c("Assunto","Non assunto"))
#1 -> Assunto , 0 -> Non assunto
table(assunzioni)

#L'ordine impostato rimane salvato
primo=speed[1]
primo
quinto=speed[5]
quinto
#minore?
primo>quinto

