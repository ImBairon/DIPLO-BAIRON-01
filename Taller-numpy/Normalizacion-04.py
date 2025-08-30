import numpy as np

peso = np.array([50, 72, 65, 80, 90, 100])


peso_normalizado = (peso - np.min(peso)) / (np.max(peso) - np.min(peso))

print("Pesos originales:", peso)
print("Pesos normalizados:", peso_normalizado)
