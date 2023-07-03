import os

ADD = 1
VIEW = 2
SEARCH = 3
MODIFY = 4
DELETE =5
QUIT = 6


def aggiungi(nomefile,descr,quant):

    try:
        outfile = open(nomefile,'a')
        outfile.write(descr+'\n')
        outfile.write(str(quant)+'\n')
        print(descr + " salvato nel file "+nomefile)
        outfile.close()

    except ValueError:
        print("Quantità di caffè non numerica")
        infile.close()

    except:
        print("Si è verificato un errore")
        infile.close()




def visualizza(nomefile):
    try:
        infile = open(nomefile,'r')
        descr = infile.readline()
        while descr!= '':
            quant = float(infile.readline())
            descr = descr.rstrip('\n')

            print("Descrizione: "+descr+" - quantità: "+str(quant)+" kg")
            descr = infile.readline()

    except FileNotFoundError:
        print("File non esistente. Controllare il nome del file")

    except ValueError:
        print("Quantità di caffè non numerica")
        infile.close()

    except:
        print("Si è verificato un errore")
        infile.close()

    else:
        infile.close()


        
def ricerca(nomefile,descr):
    #uso flag trovato
    trovato = False

    try:
        infile = open(nomefile,'r')

        d = infile.readline()
        while d!= '' and not trovato:
            quant = float(infile.readline())
            d = d.rstrip('\n')

            if descr == d:
                print("Caffè trovato - Descrizione: "+descr+" - quantità: "+str(quant)+" kg")
                trovato = True
                
            d = infile.readline()
     
        if not trovato:
            print(descr+" non trovato nel file")

    except FileNotFoundError:
        print("File non esistente. Controllare il nome del file")

    except ValueError:
        print("Quantità di caffè non numerica")
        infile.close()

    except:
        print("Si è verificato un errore")
        infile.close()

    else:
        infile.close()
    
    
def modifica(nomefile,descr,new_quant):
    #uso flag trovato
    trovato = False

    try:
        infile = open(nomefile,'r')
        tempfile = open('9.temp.txt','w')

        d = infile.readline()
        while d!= '':
            quant = float(infile.readline())
            d = d.rstrip('\n')

            if descr == d:
                tempfile.write(d+'\n')
                tempfile.write(str(new_quant)+'\n')
                trovato = True
            else:
                tempfile.write(d+'\n')
                tempfile.write(str(quant)+'\n')
                
            d = infile.readline()

        tempfile.close()

        os.remove(nomefile)
        os.rename('9.temp.txt',nomefile)

        if trovato:
            print(descr+" aggiornato nel file.")
        else:
            print(descr+" non trovato nel file. File non aggiornato")


    except FileNotFoundError:
        print("File non esistente. Controllare il nome del file")

    except ValueError:
        print("Quantità di caffè non numerica")
        infile.close()

    except:
        print("Si è verificato un errore")
        infile.close()

    else:
        infile.close()
    



def elimina(nomefile,descr):
    #uso flag trovato
    trovato = False
    try:
        infile = open(nomefile,'r')
        tempfile = open('9.temp.txt','w')

        d = infile.readline()
        while d!= '':
            quant = float(infile.readline())
            d = d.rstrip('\n')

            if descr != d:
                tempfile.write(d+'\n')
                tempfile.write(str(quant)+'\n')
                
            else:
                trovato = True
                
            d = infile.readline()

        
        tempfile.close()

        os.remove(nomefile)
        os.rename('9.temp.txt',nomefile)

        if trovato:
            print(descr+" eliminato dal file. File aggiornato")
        else:
            print(descr+" non trovato nel file. File non aggiornato")

    except FileNotFoundError:
        print("File non esistente. Controllare il nome del file")

    except ValueError:
        print("Quantità di caffè non numerica")
        infile.close()

    except:
        print("Si è verificato un errore")
        infile.close()

    else:
        infile.close()
    


def visualizza_menu():
    print("\n\tMENU")
    print("1. Aggiungi caffè")
    print("2. Visualizza magazzino caffè")
    print("3. Ricerca quantità di un caffè nel magazzino")
    print("4. Modifica quantità di un caffè nel magazzino")
    print("5. Elimina caffè")
    print("6. Uscire dal programma\n")



def main():

    scelta = 0
    nomefile = "9.caffè.txt"
        
    while scelta!=QUIT:
        visualizza_menu()
        
        try:
            scelta = int(input("Selezionare una delle opzioni (1-6):\t"))
        except ValueError:
            print("Inserire un valore numerico intero")
            scelta=0
            
        print()

        if scelta == ADD:
            try:
                descr = input("Descrizione caffè: ")
                quant = float(input("Quantità (in kg): "))
                aggiungi(nomefile,descr,quant)

            except ValueError:
                print("Inserire una quantità di caffè numerica. Ripetere l'operazione")
            print()
                       
        elif scelta == VIEW:
            visualizza(nomefile)
            print()
            
        elif scelta == SEARCH:
            descr = input("Descrizione caffè da ricercare: ")
            ricerca(nomefile,descr)
            print()
            
        elif scelta == MODIFY:
            try:
                descr = input("Descrizione caffè: ")
                quant = float(input("Inserire nuova quantità (in kg): "))
                modifica(nomefile,descr,quant)
            except ValueError:
                print("Inserire una quantità di caffè numerica. Ripetere l'operazione")
            print()

        elif scelta == DELETE:
            descr = input("Descrizione caffè: ")
            elimina(nomefile,descr)
            print()
            
        elif scelta == QUIT:
            print("Esco dal programma...")
            
        else:
            print("Errore, scelta non valida")



main()






    






