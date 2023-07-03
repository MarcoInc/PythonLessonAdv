#FUNZIONI LAMBDA -> FUNZIONI SENZA NOME
#Usate nei DataFrame per creare nuove colonne/campi tramite apply()

print("FUNZIONE LAMBDA")
#funzione lamba che prende come parametro x
    #viene ritornato come x*x
    #passo come parametro il 7
quadrato=((lambda x : x*x) (7))

print(quadrato)

print("FUNZIONE LAMBDA ALTERNATIVA CON NOME")
#oppure
#la funzione lambda quadrato prende come parametro una x
    #viene ritornato x*x
quadrato=lambda x : x*x 
#richiamo quadrato passando il parametro 7
print(quadrato(7))


