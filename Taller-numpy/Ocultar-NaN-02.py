import numpy as np

glucosa = np.array([90, 110, np.nan, 85, 100, 95, np.nan, 120, 105, 99])

glucosa_valida = glucosa[~np.isnan(glucosa)]

print("Valores válidos:", glucosa_valida)
print("Promedio:", np.mean(glucosa_valida))
print("Mínimo:", np.min(glucosa_valida))
print("Máximo:", np.max(glucosa_valida))

