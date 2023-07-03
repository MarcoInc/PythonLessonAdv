import pandas as pd
import numpy as np

#MODI PER GENERARE UN DATAFRAME
print('VUOTO')
    #DATAFRAME VUOTO
dati_vuoto=pd.DataFrame()
print(dati_vuoto)

print('UNA COLONNA')
    #DATAFRAME FORMATI DA UNA SOLA COLONNA
dati_colonna=pd.DataFrame(['Luca','Matteo','Tommaso'])
print(dati_colonna)

print('PER RIGHE')
    #DATAFRAME PER RIGHE ASSEGNANDO NOMI ALLE COLONNE   
dati_righe=pd.DataFrame([['Luca',28,'Milano'],
                        ['Matteo',30,'Torino'],
                        ['Tommaso',25,'Roma']],
                        columns=['nome','eta','citta'])
print(dati_righe)

print('DA SERIES')
    #DATAFRAME DA SERIES
capitali=pd.Series(data=['Roma','Parigi','Madrid','Lisbona'],
                    index=['Italia','Francia','Spagna','Portogallo'])
popolazione=pd.Series(data=[6000000,400000,1000000,200000],
                    index=['Italia','Francia','Spagna','Portogallo'])
#Dataframe è dato dall'unione di due series ciascuna con colonne e righe
dataframe_series=pd.DataFrame({'capitale':capitali,'popolazione':popolazione})
print(dataframe_series)

print('DA FILE CSV -> read_csv(...csv)')
    #DATAFRAME DA FILE CSV
dataframe_file=pd.read_csv('persone.csv',delimiter=';')
print(dataframe_file)

print('DA FILE EXCEL -> read_excel(...xlsx)')
    #DATAFRAME DA FILE EXCE
dataframe_excel=pd.read_excel('persone.xlsx')
print(dataframe_excel)

print('DA UN DATABASE -> read_sql()')
    #DA UN DATABASE RELAZIONALE SQLITE -> visto nella 30.4
# query_SQL="""SELECT cognome, COUNT(*) AS quanti
# FROM persone
# GROUP BY cognome
# ORDER BY quanti DESC"""
# dati_sql=pd.read_sql(query_SQL,engine)
# print(type(dati_sql))
# print(dati_sql)