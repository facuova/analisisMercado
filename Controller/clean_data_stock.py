import pandas as pd

def cleanDataStock(lista_df):
    for df in lista_df:
        df.rename(
            columns={
                'fechaHora': 'fecha',
                'ultimoPrecio': 'precio',
            },
            inplace=True,
        )
