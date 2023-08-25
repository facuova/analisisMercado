from Controller.transformar_xlsx import transformarXlsx 
from Controller.clean_data_stock import cleanDataStock
import pandas 

#Importamos los archivos  y lo agregamos a una lista
usd_blue = './Data/usd_blue.xlsx'
alua = './Data/alua.xlsx'
bbar = './Data/bbar.xlsx'

lista_xlsx = [usd_blue, alua, bbar]

#Aplicamos una función para transformar la lista con arcvhivos xlsx en una lista con dataframes
lista_df = transformarXlsx(lista_xlsx)

#Armamos un subset, para mantener el original y modificar el subset
usd_blue_df = lista_df[0]

#Cambiamos los nombres de la columa en el usd_blue ya que se descargó 
# de una fuente de datos distinta a la de las acciones.
usd_blue_df.rename(columns={
    'Fecha': 'fecha', 
    'Venta': 'cierre'
    }, 
    inplace=True
)

usd_blue_df.drop("Compra", axis=1, inplace=True)
#print(usd_blue_df)

#Acá realizamos los subsets de las acciones y nos quedamos con las columas fechas y el cierre del día
""""
alua_df = lista_df[1][['fechaHora','ultimoPrecio']]
bbar_df = lista_df[2][['fechaHora','ultimoPrecio']]

alua_df.rename(columns={
    'fechaHora': 'fecha',
    'ultimoPrecio': 'precio',
    },
    inplace=True
)

bbar_df.rename(columns={
    'fechaHora': 'fecha',
    'ultimoPrecio': 'precio',
    },
    inplace=True
)
"""
lista_stock = lista_df 
lista_stock.pop(0)

cleanDataStock(lista_stock)

print(lista_stock)