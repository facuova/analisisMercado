import pandas as pd

def convertListFloat (lista_df):

    for df in lista_df:
        df['cierre'] = df['cierre'].astype(float)
    return lista_df