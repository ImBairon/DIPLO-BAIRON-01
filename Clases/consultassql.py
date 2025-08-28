"""
CRUD
Create, read, update, delete
"""

import sqlite3
import pandas as pd
from ClaseBD import con
consulta = '''
SELECT fecha, region, producto, unidades, ingreso_neto
FROM ventas
WHERE region <> 'Desconocida' AND producto IN ('A', 'B')
ORDER BY fecha DESC
LIMIT 20

'''

consulta_ventas = pd.read_sql_query(consulta, con)

print(consulta_ventas)

#Consultar multitabla

clientes_ventas = '''
SELECT c.id_cliente, c.nombre, c.ciudad, v.producto, v.precio
SUM(v.ingreso_neto) AS ingreso_total
FROM clientes AS c JOIN ventas AS v ON c.id_cliente = v.id_cliente 
GROUP BY c.id_cliente, c.nombre, c.ciudad
LIMIT 10
'''
#c.id_cliente = v.id_cliente para hacer la llave de la bd


resumen_clientes = pd.read_sql_query(clientes_ventas, con)
print(resumen_clientes)

#Exportar los resultados a un csv

consulta_ventas.to_csv('data/consulta_ventas.csv', index = False)
resumen_clientes.to_csv('data/clientes_ventas.csv', index = False)
print('Datos exportados correctamente en la carpeta data.')