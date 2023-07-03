import pandas as pd
import numpy as np

print('SALVATAGGIO DATAFRAME')

print('SU FILE CSV -> .to_csv(...)')
dati=pd.DataFrame(['Luca','Matteo','Tommaso'])
print(dati)
dati.to_csv('30.4.file_creato.csv',index=None, sep=';', header=False)
#sep= -> se vogliamo un separatore nel file
#header=
    #True -> se vogliamo riportare le intestazioni/etichette
    #False -> altrimenti
#index=
    #True -> se vogliamo riportare gli indici
    #None -> altrimenti

print('SU FILE EXCEL -> ExcelWriter(...) + .to_excel(...)')
# Necessita di un oggetto della classe ExcelWriter con i parametri
    #file output
    #engine=xlsxwriter -> engine da usare -> va installato
writer=pd.ExcelWriter('30.4.dati_excel.xlsx',engine='xlsxwriter')
dati.to_excel(writer,index=False, sheet_name='Persone')
#writer -> nome dell'oggetto ExcelWriter
#index=
    #True -> se vogliamo riportare gli indici
    #False -> altrimenti
#sheet_name= -> Nome del foglio
writer.save() #crea il file con il writer specificato

print('SU UN DATABASE -> sqlalchemy + .create_engine(...)')
# frm sqlalchemy import create_engine
# engine=create_engine('sqlite:///database_nuovo.db')
# dati.to_sql('persone',engine,index=False)
