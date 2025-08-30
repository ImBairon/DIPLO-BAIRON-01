import numpy as np

data = np.array([3,7, np.nan, 15, np.nan, 21])
print("Donde hay un NaN?",np.isnan(data))

cleaned = data[~np.isnan(data)]

print("Datos limpios", cleaned)

promedio = np.nanmean(data)
print ("Promedio calculado", promedio)

filled = np.nan_to_num(data,nan=promedio)
print("Nueva lista con reemplazados:" , filled)