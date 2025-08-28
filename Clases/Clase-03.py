import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler

# --- Cargar los datos ---
ventas = pd.read_csv('data/ventas.csv', parse_dates=['fecha'])
clientes = pd.read_csv('data/clientes.csv', parse_dates=['fecha_registro'])
devoluciones = pd.read_csv('data/devoluciones.csv', parse_dates=['fecha'])

# ==============================
# 1. LIMPIEZA DE DATOS
# ==============================

# 1.1 Estandarizar textos
ventas['producto'] = ventas['producto'].astype(str).str.strip().str.upper()
ventas['region'] = ventas['region'].astype(str).str.strip().str.title()

# 1.2 Tratar valores nulos
ventas['region'] = ventas['region'].fillna('Desconocida')

# 1.3 Eliminar duplicados
print("Duplicados iniciales en VENTAS:", ventas.duplicated().sum())
ventas = ventas.drop_duplicates()

print("Duplicados iniciales en CLIENTES:", clientes.duplicated().sum())
clientes = clientes.drop_duplicates()

print("Duplicados iniciales en DEVOLUCIONES:", devoluciones.duplicated().sum())
devoluciones = devoluciones.drop_duplicates()

# ==============================
# 2. ESTANDARIZACIÓN NUMÉRICA
# ==============================
scaler = StandardScaler()

num_cols_ventas = ventas.select_dtypes(include='number').columns
num_cols_clientes = clientes.select_dtypes(include='number').columns

ventas_est = ventas.copy()
ventas_est[num_cols_ventas] = scaler.fit_transform(ventas[num_cols_ventas])

clientes_est = clientes.copy()
clientes_est[num_cols_clientes] = scaler.fit_transform(clientes[num_cols_clientes])

print("\nPrimeras columnas estandarizadas en VENTAS:")
print(ventas_est[num_cols_ventas].head())

print("\nPrimeras columnas estandarizadas en CLIENTES:")
print(clientes_est[num_cols_clientes].head())

# ==============================
# 3. VISUALIZACIÓN
# ==============================

def graficar_columnas(df, columnas, titulo_df):
    for col in columnas:
        plt.figure(figsize=(10,5))

        plt.subplot(1,2,1)
        sns.histplot(df[col], kde=True)
        plt.title(f"{titulo_df} - Histograma {col}")

        plt.subplot(1,2,2)
        sns.boxplot(x=df[col])
        plt.title(f"{titulo_df} - Boxplot {col}")

        plt.tight_layout()
        plt.show()

# Visualizar datos
graficar_columnas(ventas, num_cols_ventas, "VENTAS")
graficar_columnas(clientes, num_cols_clientes, "CLIENTES")
