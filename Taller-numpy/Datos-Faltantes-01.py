import numpy as np

data = np.array([90,110, np.nan, 85,100,95, np.nan, 120,105,99])
print("Donde hay un NaN?",np.isnan(data))