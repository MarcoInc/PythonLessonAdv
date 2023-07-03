lista=["casa","mare","mare","mare","montagna","casa","montagna"]
#associa ad ogni elemento dei numeri sequenziali
enumeratore=enumerate(lista)

#è un oggetto di tipo numerico
print("Risultato di enumerate(lista)",enumeratore)

#stampo elemento per elemento di enumerate
for elemento in enumeratore:
    print(elemento)

#salvo il risultato di enumerate(lista) in un dizionario
dizionario=dict(enumerate(lista))
#associo indice:valore lista -> chiave:valore
print("Contenuto del dizionario",dizionario)