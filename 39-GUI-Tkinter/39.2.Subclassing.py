import tkinter as tk
from tkinter import ttk

#SUBCLASSING dei widget Tkinter
    # sfrutta la ereditarietà dell'OOP con classi esistenti
    
#CLASSE FRAME -> OGGETTO-> contenitore di widget
    #verrà trattaco come se fosse un unico widget
    
#memorizza messaggio di saluto e nome  
class HelloWidget(tk.Frame):
    "Un piccolo modulo"
                #il costruttore può ricevere qualsiasi argomento
    def __init__(self,parent,*args,**kwargs):
        #RICHIAMO COSTRUTTORE SUPERCLASSE->Frame
        super().__init__(parent,*args,*kwargs)
        
        #CREO DUE ATTRIBUTI
        self.name=tk.StringVar() #TIPO STRINGA
        self.hello_string=tk.StringVar()
        
        #SET ->Cambia il valore di un attributo
        self.hello_string.set("Hello World")
        
        #OGGETTI DA MOSTRARE
        name_label=ttk.Label(self, text="Name:")
        
        #essa farà riferimento alla variabile name dell'oggetto
            #ad ogni inserimento di testo, verrò aggiornato in tempo reale

        name_entry=ttk.Entry(self, textvariable=self.name)

        #BOTTONE
        ch_button=ttk.Button(self, text="Cambia", command=self.on_change)
        #Argomenti -> text="ETICHETTA", command=RIFERIMENTO FUNZIONE
        
        #MESSAGGIO DI SALUTO
        hello_label=ttk.Label(self, textvariable=self.hello_string,
                            font=('TkDefaultFont,64'),wraplength=600)
                    #TUPLA->font(nome_font,dimensione font)
                    #wraplenght -> larghezza in pixel testo prima che
                        # lo stesso vada nella riga successiva
                        # se omesso, il testo verrà tagliato al limite della finestra
        
        #IMPOSTARE GLI WIDGET NELLA FINESTRA
        #grid()-> dispone gli oggetti come se ci fosse una tabella
            #sticky -> specifica a quale lato del container verà attaccato
                #N -> Nord
                #S -> Sud
                #E -> Est
                #W -> Ovest
        name_label.grid(row=0, column=0, sticky=tk.W) #lato ovest
        name_entry.grid(row=0, column=1, sticky=tk.W+tk.E) #riempie tutta la colonna
        ch_button.grid(row=0, column=2, sticky=tk.E) #lato est
        hello_label.grid(row=1, column=0, columnspan=3) #occupa 3 righe
        
        #columnconfigure -> sistema configurazione della griglia colonne
            #weight-> peso a 1
                #permette alla colonna di espanderi orizzontalmente 
                # e ridurre le colonne laterali alla loro minima larghezza
        #rowconfigure()-> uguale a columnconfigure ma per le righe
        self.columnconfigure(1, weight=1)
        
    # METODO CALLBACK per il pulsante ch_button
    def on_change(self):
        #GET-> prende un attributo
        if self.name.get().strip():
            #prende il testo inserito in name_entry e lo inserisce in hello_string
            self.hello_string.set('Ciao '+self.name.get())
        else:
            #se non ci sono nomi ci sarà un messagio di default
            self.hello_string.set("Ciao Mondo")

#CLASSE APPLICAZIONE -> sottoclasse da tk.Tk
    #Ci sarà UNA SOLA ISTANZA dell'applicazione
class MyApplication(tk.Tk): 
    
    def __init__(self,*args,**kwargs):
        super().__init__(*args,*kwargs)
        
        #Titolo finestra
        self.title('Hello Tkinter')
        #dimensione finestra in pixel
        self.geometry("800x600")
        #se è possibile ridimensionare la finestra
        self.resizable(width=False, height=False)
        
        #Aggiungo il widget HelloWidget alla finestra principale
        HelloWidget(self).grid(sticky=(tk.E+tk.W+tk.N+tk.S)) #a tutti i 4 lati della cella
        self.columnconfigure(0,weight=1) 
            #columnfigure() -> imposta la prima colonna all'espansione di tutto lo spazio della finestra
            
#ESEGUE L'APPLICAZIONE
if __name__=='__main__': #Controlla se l'applicazione è stata avviata correttamente
    app=MyApplication()
    app.mainloop()

    

