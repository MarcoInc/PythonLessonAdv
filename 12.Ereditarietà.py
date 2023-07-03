#SPECIALIZZA UN OGGETTO
import math
class Figura:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
        
    def set_x(self,x):
        self.__x=x
    
    def set_y(self,y):
        self.__y=y
    
    def get_x(self):
        return x
    def get_y(self):
        return y

    def calcola_perimetro(self):
        return "Dati insufficenti per il calcolo del perimetro"
    def calcola_area(self):
        return "Dati insufficenti per il calcolo dell'area"
    def somma(self):
        return "Dati insufficenti"
    
    def __str__(self):
        return "x = "+str(self.__x)+" y= "+str(self.__y)

#SOTTOCLASSE
    #OVERRIDING DEL COSTRUTTORE -> Usa il costruttore della SUPERCLASSE e lo unisce
class Cerchio(Figura):
    #COSTRUTTORE -> passo x, y ed un raggio
    def __init__(self,x,y,raggio):
        #usa il costruttore della SUPERCLASSE
        Figura.__init__(self,x,y)
        #Aggiungo un attributo provato alla SOTTOCLASSE -> più specializzata
        self.__raggio=raggio
    
    def set_raggio(self,raggio):
        self.__raggio=raggio
    def get_raggio(self):
        return raggio
    
    #POLIMORFISMO -> Cambiare il comportamento di una classe
        #OVERRIDING DEI METODI -> Nome uguale alla superclasse ma comportamento diverso
    def calcola_perimetro(self):
        return 2*math.pi*self.__raggio
    def calcola_area(self):
        return self.__raggio*(math.pi**2)
        #OVERLOADING DEI METODI -> Nome uguale ma parametri diversi
    def somma(self,x,y):
        return x+y
    
    def __str__(self):
        return "Cerchio con raggio "+str(self.__raggio)+"\nCentrato in "+Figura.__str__(self)

def main():
    cerchio=Cerchio(5,6,10)
    print(cerchio)
    
    print("Area")
    print(cerchio.calcola_area()) #metodo overrrided
    print("Perimetro")
    print(cerchio.calcola_perimetro())
    
    figura=Figura(10,2)
    print(figura.calcola_perimetro())
    
    print(figura.somma())
    print(cerchio.somma(3,2)) #metodo overloaded
    
    print("L'oggetto cerchio è di classe Cerchio?")
    print(isinstance(cerchio,Cerchio)) #verifica se l'oggetto è istanza della classe
    #ECCEZIONE AttributeError
    cerchio.sort() #il metodo non è della classe/oggetto
main()

    

    
