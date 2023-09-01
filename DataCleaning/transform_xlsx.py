# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 00:09:02 2023

@author: Facu
"""

import pandas as pd
import openpyxl

def transformXlsx(lista_xlsx):
    lista_df = []
    
    for archivo in lista_xlsx:
        libro = openpyxl.load_workbook(archivo)
        hoja = libro.active
        titulos = next(hoja.values)[0:]
        df = pd.DataFrame(hoja.values, columns=titulos)
        df = df.drop(0)
        lista_df.append(df)
    
    return lista_df


