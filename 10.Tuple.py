#Una lista che non può essere modificata
    #PRO -> più veloci da processare rispetto alle liste
        #-> più sicure rispetto alle liste
tupla=(1,"Ciao",3.4) 
print(tupla)

print("Converto una tupla in una lista [.....]")
#Conversione in lista -> modificabile
lista=list(tupla)
print(lista)

print("Converto una lista in una tupla (.....)")
lista_mista=["Ciao","Mondo",5,"Sole",3.14]
tupla_convertita=tuple(lista_mista)
print(tupla_convertita)

#OPERAZIONI SULLE TUPLE -> tutte quelli delle lista ma senza modificarla
#NON SI USANO QUINDI
# append;
# remove;
# insert;
# reverse;
# sort.