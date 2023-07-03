from tkinter import *
from tkinter.ttk import * #WIDGET e migliora l'aspetto
    #se rimossa il programma funziona MA peggiora la grafica

#OGGETTO MASTER
root=Tk()
#rappresenta la finestra principale e il thread di esecuzione principale
    #ogni applicazione avrà la sua instanza di Tk()
    
#OGGETTO LABEL -> widget per visualizzazione di testo o immagini
label=Label(root, text="hello World!")
#label verrà contenuto in root e avrà un testo

#Disporre l'oggetto nel PARENT WIDGET -> gestione della geometria
label.pack() #Metto label nel contenitore master

#BUTTON -> pulsante cliccabile
button=Button(root,text="Clicca qui")
button.pack()

#ENTRY  -> campo di testo da riempire
entry=Entry(root,text="Inserisci testo qui")
entry.pack()

#Main Event Loop -> ciclo di eventi principale
    #responsabile dell'laborazione di tutti gli eventi
    #termina quando il programma non è chiuso
root.mainloop()