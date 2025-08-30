import numpy as np

glucosa = np.array([90, 110, np.nan, 85, 100, 95, np.nan, 120, 105, 99])


promedio_valido = np.nanmean(glucosa)


glucosa_imputada = np.where(np.isnan(glucosa), promedio_valido, glucosa)

print("Promedio de valores válidos:", promedio_valido)
print("Arreglo con NaN reemplazados:", glucosa_imputada)
