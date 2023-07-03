chiavi="abcdefg" #8 chiavi -> ciascun carattere sarà la chiave
lista=["casa","mare","mare","mare","montagna","casa","montagna"] #8 valori
#chiavi e lista hanno la stessa dimensione


#associo indice:valore lista -> chiave:valore   
    #zip unisce ad ogni chiave un valore della lista
dizionario=dict(zip(chiavi,lista))

print("Contenuto del dizionario",dizionario)