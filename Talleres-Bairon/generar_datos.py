import numpy as np
import pandas as pd
from pathlib import Path
rng = np.random.default_rng(42)


# --- Generar ventas ---
N = 500
fechas = pd.date_range('2024-01-01', periods=200).to_series().sample(N, replace=True, random_state=42).sort_values().values
regiones = rng.choice(['Norte', 'Sur', 'Este', 'Oeste'], size=N)
productos = rng.choice(['Zapatos', 'Sombreros', 'Pantalones', 'Vestidos'], size=N, p=[0.4, 0.3, 0.2, 0.1])
canal = rng.choice(['Online', 'Tienda', 'Distribuidor'], size=N, p=[0.5, 0.3, 0.2])
unidades = rng.integers(1, 50, size=N)
precio = rng.normal(200000, 50000, size=N)
descuento = rng.choice([0, 0.05, 0.1, 0.15], size=N, p=[0.6, 0.2, 0.15, 0.05])
id_cliente = rng.integers(1, 151, size=N) # 150 clientes


ventas = pd.DataFrame({
'fecha': pd.to_datetime(fechas),
'region': regiones,
'producto': productos,
'canal': canal,
'unidades': unidades,
'precio': precio,
'descuento': descuento,
'id_cliente': id_cliente
})
ventas['ingreso_bruto'] = ventas['unidades'] * ventas['precio']
ventas['ingreso_neto'] = (ventas['unidades'] * ventas['precio']) * (1 - ventas['descuento'])


# Introducimos algunos valores faltantes y espacios para limpieza
ventas.loc[rng.integers(0, N, 10), 'region'] = None
ventas.loc[rng.integers(0, N, 10), 'producto'] = ' ' + ventas.loc[rng.integers(0, N, 10), 'producto'].astype(str) + ' '


# --- Generar clientes ---
M = 150
clientes = pd.DataFrame({
'id_cliente': range(1, M+1),
'nombre': [f'Cliente_{i}' for i in range(1, M+1)],
'edad': rng.integers(18, 70, size=M),
'ciudad': rng.choice(['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Bucaramanga'], size=M),
'fecha_registro': pd.to_datetime('2023-01-01') + pd.to_timedelta(rng.integers(0, 365, size=M), unit='D')
})


# --- Generar devoluciones ---
K = 60
devoluciones = ventas.sample(K, random_state=42)[['fecha', 'id_cliente', 'producto']].copy()
devoluciones['motivo'] = rng.choice(['Defecto', 'Talla', 'Retracto', 'Otro'], size=K, p=[0.4, 0.2, 0.2, 0.2])


# Guardar
Path('data').mkdir(exist_ok=True)
ventas.to_csv('data/ventas.csv', index=False)
clientes.to_csv('data/clientes.csv', index=False)
devoluciones.to_csv('data/devoluciones.csv', index=False)
print('Archivos creados en ./data: ventas.csv, clientes.csv, devoluciones.csv')