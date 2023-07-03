import locale #usato per le valute
#In USA usano . al posto di , per i numeri decimali e usano , per separare le cifre
#In Europa . viene usato per separare le cifre e , per i numeri decimali

#Cambio il locale per un altro paese
locale.setlocale(locale.LC_ALL,'it_IT')
                                #fr_FR
                                #de_DE
                #atof-> formatta le stringhe per un determinato paese
numero_eu=locale.atof(input("Inserisci un numero\n"))

print("Formato europeo")
print(locale.format_string('%.2f',numero_eu))
                            #mostra il numero con due cifre decimali