#Importar las bibliotecas

import pandas as pd
#Series

#Crear una serie

lista = [10, 20,30,40,50]
serie = pd.Series(lista)

#DataFrame

datos = {
    "Nombres":["Cesar","Edwin","Ivan","Brandon","Cristian"],
    "Edad": [19,20,21,22,23],
    "Asignatura": ["Bases de datos", "Arquitectura","Programación","Estadistica", "Gestion"]
}

gato = pd.DataFrame(datos)

#Leer archivos desde pandas
#Cargar archivo csv

datos_csv = pd.read_csv('tips.csv')


#Head muestra las primeras 5 filas y encabezados de las columna.

"""print(datos_csv.head())"""

#Cargar un Archivo excel

datos_excel = pd.read_excel("ventas_limpio.xlsx", sheet_name="copia")

#Métodos para trabjo con archivos y pandas
#Ver columnas del archivo usamos metodo column

print(datos_excel.columns)

#Mostrar columnas en especifico.

print(datos_excel[['categoria','producto','precio',]])