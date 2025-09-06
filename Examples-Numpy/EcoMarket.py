import numpy as np
import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker   


#Estilo Global
sns.set_theme(style="whitegrid", font_scale=1.08)

plt.rcParams["axes.titleweight"] = "bold" 

plt.rcParams["font.family"]="DejaVu Sans"

COLORS={
    "primary": "#138FED", #Series Principales
    "accent": "#EDC113", #Resaltar Anotaciones
    "muted": "#C4C4C4", #Elementos Secundarios
    "line2": "#866400", #Segundas Lineas
}

def read_csv_smart(path, parse_dates=None):
    try:
        return pd.read_csv(path, parse_dates=parse_dates)
    except Exception:
        return pd.read_csv(path, sep=";", decimal=",",parse_dates=parse_dates)

customers = read_csv_smart("Archivos CSV/customers.csv", parse_dates=["signup_date"])
orders = read_csv_smart("Archivos CSV/orders.csv", parse_dates=["order_date"])
items = read_csv_smart("Archivos CSV/items.csv")

print("Customers,", customers)
print("Orders", orders)
print("Items", items)

def clean_str(s):
    return s.strip().title() if isinstance (s,str) else s

for col in ["city", "channel"]:
    if col in orders.columns:
        orders[col] = orders [col].apply(clean_str)

for col in ["product", "category"]:
    if col in items.columns:
        items[col] = items [col].apply(clean_str)

customers ["signup_date"] = pd.to_datetime(customers.get("signup_date"), errors="coerce")
orders ["order_date"] = pd.to_datetime(orders.get("order_date"), errors="coerce")
items ["units"] = pd.to_numeric(items.get("units"), errors="coerce")
items ["unit_price"] = pd.to_numeric(items.get("unit_price"), errors="coerce")

orders_before = len(orders)
items_before = len (items)

orders = orders.dropna(subset=["order_id","customer_id","order_date"])
items = items.dropna(subset=["order_id","units","unit_price"])

orders = orders.drop_duplicates(subset=["order_id"])
items = items.drop_duplicates(subset=["order_id", "product", "category"])

items = items[(items["units"]>0) & (items["unit_price"]>0)]
items = items[items["order_id"].isin(orders["order_id"])]

print ("LIMPIEZA")
print (f"Pedidos:{orders_before} -> {len(orders)}")
print(f"Items: {items_before} -> {len(items)}")