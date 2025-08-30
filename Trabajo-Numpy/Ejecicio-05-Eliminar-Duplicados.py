import numpy as np

nombres = np.array (["Bairon", "Daniel", "Brandon", "Ivan", "Mari", "Ivan", "Daniel"])

#Eliminar Duplicados

unique_name = np.unique(nombres)

print("Original:", nombres)
print("Sin duplicados:", unique_name)

