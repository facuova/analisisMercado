import pandas as pd
import numpy as np

def yieldsCalculate (lista_df):
    
    for df in lista_df:
        df['yields'] = np.log(df['cierre'] / df['cierre'].shift(1))
    