import pandas as pd
import numpy as np

def volatilityHistoric (lista, lenght):
    
    for df in lista:
        df[f"volatility{lenght}p"] = df['yields'].rolling(window=lenght).std() * np.sqrt(260)
    
    return lista
    
    


