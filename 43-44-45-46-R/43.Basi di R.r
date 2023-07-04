#creo un vettore
vettore=c("Mario","Impiegato")

# etichettare gli elementi del vettore

names(vettore)=c("Nome","Lavoro")

# a quale classe appartiene
    #numerica -> numeri
    #logical -> booleani
    #character -> letterali
class(vettore)

ore_lavoro=c(8,8,8,4,8)
settimana=c("Lun","Mar","Mer","Giov","Ven")

#etichetto le ore_lavoro con i giorni settimana
names(ore_lavoro)=settimana
ore_lavoro

#tipo dei valori di ore_lavoro
class(ore_lavoro)

#somma tutti i valori di ore_lavoro
ore_totali=sum(ore_lavoro)

#indexing [] parte da 1
ore_mercoledi=ore_lavoro[3] #terzo elemento
ore_mercoledi

#selezionare più elementi non contigui di un vettore
ore_lun_mart_ven=ore_lavoro[c(1,2,4)]
ore_lun_mart_ven

#slicing -> elementi contigui
ore_lun_mart=ore_lavoro[c(1:2)]
#oppure -> senza c()
ore_lun_mart=ore_lavoro[1:2]
ore_lun_mart

#indexing con le etichette al posto degli indici
ore_lun_mart_ven=ore_lavoro[c("Lun","Mar","Mer","Giov","Ven")]
ore_lun_mart_ven

#condizioni
ore_lavoro>4 #ritorna un bool

#tipo -> logical
ore_full=ore_lavoro>4
class(ore_full) #logical

#indicizzare il vettore secondo indici booleani
ore_lavoro[ore_full] #mostra solo i TRUE

#eliminare le etichette
ore_lavoro_noName=unname(ore_lavoro)
ore_lavoro_noName



