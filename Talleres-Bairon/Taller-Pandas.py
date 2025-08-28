#Importar las bibliotecas

import pandas as pd

datos = {
    "Nombre": ["Ana", "Luis", "María", "Carlos", "Sofía"],
    "Edad": [20, 22, 19, 21, 23],
    "Nota1": [4.5, 3.8, 4.9, 3.5, 4.2],
    "Nota2": [4.0, 3.9, 4.7, 3.6, 4.3]
}

df = pd.DataFrame(datos)
df["Promedio"] = (df["Nota1"] + df["Nota2"]) / 2
aprobados = df[df["Promedio"] >= 3.0]

print("Estudiantes aprobados:\n", aprobados)

aprobados.to_csv("aprobados.csv", index=False)
datos_csv = pd.read_csv("aprobados.csv")
