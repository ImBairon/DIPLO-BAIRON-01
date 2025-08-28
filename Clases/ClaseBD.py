import sqlite3
import pandas as pd


con = sqlite3.connect('data/negocio.db')
ventas = pd.read_csv('data/ventas.csv', parse_dates=['fecha'])
clientes = pd.read_csv('data/clientes.csv', parse_dates=['fecha_registro'] )

#Guardar en tablas sql los datos anteriores
ventas.to_sql('ventas', con, if_exists='replace', index=False)
clientes.to_sql('clientes', con, if_exists='replace', index=False)

#Crear los indices utiles
cur = con.cursor()
cur.execute('CREATE INDEX IF NOT EXISTS idx_ventas_fecha ON ventas(fecha)')
cur.execute('CREATE INDEX IF NOT EXISTS idx_ventas_cliente ON ventas(id_cliente)')
con.commit()
