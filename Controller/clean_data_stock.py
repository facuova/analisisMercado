import pandas as pd

def cleanDataStock(lista_df):
    for df in lista_df:
        df.rename(
            columns={
                'fechaHora': 'fecha',
                'ultimoPrecio': 'cierre',
            },
            inplace=True,
        )
        df = df[['fecha', 'cierre']]
