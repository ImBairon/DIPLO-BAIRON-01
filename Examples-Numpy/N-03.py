import pandas as pd, numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme()
df = pd.read_csv("Archivos CSV/tickets_soporte.csv")

fig, ax = plt.subplots(figsize=(8, 4))

# Histograma con KDE
sns.histplot(data=df, x="tiempo_respuesta_min", bins=10, kde=True, ax=ax)

# Personalización de etiquetas y título
ax.set_title("Detalle mesa de soporte (Tiempos de Respuesta)")
ax.set_xlabel("Minutos")
ax.set_ylabel("Cantidad de Casos")

# Mostrar leyenda
ax.legend()
plt.tight_layout()
plt.show()
