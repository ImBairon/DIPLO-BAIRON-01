import pandas as pd
import matplotlib.pyplot as plt

#Cargar datos 
ventas = pd.read_csv('data/ventas.csv', parse_dates=['fecha'])
clientes = pd.read_csv('data/clientes.csv', parse_dates=['fecha_registro'])
devoluciones = pd.read_csv('data/devoluciones.csv', parse_dates=['fecha'])

#Estandarizar textos
ventas['producto'] = ventas['producto'].astype(str).str.strip().str.upper()
ventas['region'] = ventas['region'].astype(str).str.strip().str.title()

#Tratar valores nulos
print("\nValores nulos antes de limpieza:")
print(ventas.isna().sum())
ventas['region'] = ventas['region'].fillna('Desconocida')

#Duplicados
print("\nDuplicados en VENTAS:", ventas.duplicated().sum())
ventas = ventas.drop_duplicates()

print("Duplicados en CLIENTES:", clientes.duplicated().sum())
clientes = clientes.drop_duplicates()

print("Duplicados en DEVOLUCIONES:", devoluciones.duplicated().sum())
devoluciones = devoluciones.drop_duplicates()


# normalizar las column
num_cols_ventas = ventas.select_dtypes(include='number').columns
num_cols_clientes = clientes.select_dtypes(include='number').columns

ventas_est = ventas.copy()
clientes_est = clientes.copy()

for col in num_cols_ventas:
    ventas_est[col] = (ventas[col] - ventas[col].mean()) / ventas[col].std()

for col in num_cols_clientes:
    clientes_est[col] = (clientes[col] - clientes[col].mean()) / clientes[col].std()

print("\nPrimeras filas con columnas estandarizadas (VENTAS):")
print(ventas_est[num_cols_ventas].head())

print("\nPrimeras filas con columnas estandarizadas (CLIENTES):")
print(clientes_est[num_cols_clientes].head())


def graficar_columnas(df, columnas, titulo_df):
    for col in columnas:
        plt.figure(figsize=(10,5))

        # Histograma
        plt.subplot(1,2,1)
        plt.hist(df[col], bins=20, edgecolor='black')
        plt.title(f"{titulo_df} - Histograma {col}")

        # Boxplot
        plt.subplot(1,2,2)
        plt.boxplot(df[col].dropna())
        plt.title(f"{titulo_df} - Boxplot {col}")

        plt.tight_layout()
        plt.show()

# Graficar
import matplotlib.pyplot as plt

# Detectar columnas numéricas
num_cols = ventas.select_dtypes(include=['int64', 'float64']).columns

for col in num_cols:
    plt.figure(figsize=(12,4))

    # Histograma
    plt.subplot(1,3,1)
    plt.hist(ventas[col], bins=20, edgecolor='black')
    plt.title(f"Histograma de {col}")

    # Boxplot
    plt.subplot(1,3,2)
    plt.boxplot(ventas[col].dropna())
    plt.title(f"Boxplot de {col}")

    # Serie temporal
    plt.subplot(1,3,3)
    plt.plot(ventas[col].values)
    plt.title(f"Serie de {col}")

    plt.tight_layout()
    plt.show()
