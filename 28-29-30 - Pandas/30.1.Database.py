import pandas as pd
import numpy as np

conti=pd.DataFrame({'conto':['1111000','113032','1114000','1115000'],\
                    'intestatario':['Paolo Verdi','Mario Rossi','Carlo Bianchi','Pluto Esposito']})
estinzioni=pd.DataFrame({'conto':['1111000','1114000'],\
                        'data':['2010-09-22','2004-11-12']})

saldi=pd.DataFrame({'conto':['113032','1115000'],\
                    'saldo':[120000,320500]})
print('Conti')
print(conti)
print('Estinzioni')
print(estinzioni)
print('Saldi')
print(saldi)


print('JOIN -> pd.merge(...)')
#JOIN -> Congiunzione tra le righe di DataFrame differenti che hanno dati in comune
    #merge() -> effettua il JOIN
        #dataframe da unire
        #quale campo joinare
        #eventuali modalita di join
join_conti_saldi=pd.merge(conti,saldi,on='conto')
#il DataFrame conterrà tutti quelli che hanno lo stesso conto in conti e saldi
print(join_conti_saldi)

print('LEFT OUTER JOIN -> pd.merge(...how=\'left\')')
joinLeft_conti_saldi=pd.merge(conti,saldi,on='conto',how='left')
#Verranno riportati tutti i conti(sinistra) e chi non ha un saldo ci sarà NaN
print(joinLeft_conti_saldi)

print('RIGHT OUTER JOIN -> pd.merge(...how=\'right\')')
joinRight_conti_saldi=pd.merge(conti,saldi,on='conto',how='right')
print(joinRight_conti_saldi)
#Verranno riportati tutti i saldi e chi non ha un conto(destra) ci sarà NaN




