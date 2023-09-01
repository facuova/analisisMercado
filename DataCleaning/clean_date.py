import pandas as pd


def convertListDate(lista_df):
   
    for df in lista_df:
        #Convertimos el formato de fechaHora a datetine
        df['fecha'] = pd.to_datetime(df['fecha'])       
        
    return lista_df