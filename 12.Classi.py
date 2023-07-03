import random;
#Classe
    #Privati -> __attributo___
    #Pubblico -> attributo
class Moneta: #Maiuscola
    #METODI STANDARD
        #COSTRUTTORE
        #self -> della classe stessa -> this
        #qua crea la classe stessa senza parametri
    def __init__(self):
        self.lato_su="Testa"
    
        #STATO DELL'OGGETTO QUANDO VIENE PASSATO AD UNA PRINT
    def __str__(self): #servirà poi una print
        return "Dopo l'ultimo lancio è uscito: "+self.lato_su
        #INTERFACCIA -> metodi che permette l'accesso agli attributi
            #GETTER
    def get_lato_su(self):
        return self.lato_su
            #SETTER -> parametro un valore
    def set_lato_su(self,lato):
        self.lato_su=lato

        
    #METODI CUSTOM    
    def lancia(self):
        if random.randint(0,1)==0:
            self.lato_su="Testa"
        else:
            self.lato_su="Croce"
    

def main():
    #OGGETTI
    moneta1=Moneta()
    moneta2=Moneta()
    
    print("moneta1")
    for i in range(5):
        moneta1.lancia()
        print(moneta1)     #print funziona grazie ad __str__
        
    print("moneta2")
    for i in range(5):
        moneta2.lancia()
        print(moneta2)
        
main()