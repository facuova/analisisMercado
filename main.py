import pandas as pd
import openpyxl

usd_blue = openpyxl.load_workbook('./Data/usd_blue.xlsx')
alua = openpyxl.load_workbook('C:/Users/Facu/Desktop/Facu/Proyecto_Mercado/accionesArgentinas/ALUA.xlsx')

usd_blue_hoja = usd_blue.active
alua_hoja = alua.active

usd_blue_titulos = next(usd_blue_hoja.values)[0:]
alua_titulos = next(alua_hoja.values)[0:]

usd_blue_df = pd.DataFrame(usd_blue_hoja.values, columns=usd_blue_titulos)
alua_df = pd.DataFrame(alua_hoja.values, columns=alua_titulos)

usd_blue_df = usd_blue_df.drop(0)
usd_blue_df.rename(columns={
    'Fecha': 'fecha', 
    'Venta': 'cierre'}, 
    inplace=True
    )

usd_blue_df = usd_blue_df[['fecha', 'cierre']]

alua_df.rename(columns={
    'fechaHora': 'fecha', 
    'ultimoPrecio': 'cierre'}, 
    inplace=True
    )

alua_df = alua_df.drop(0)

alua_df = alua_df[['fecha','cierre']]

print(usd_blue_df)