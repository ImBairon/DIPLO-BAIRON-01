import numpy as np

edades = np.array([15, 22, 19, 30, 25, 25, 40, 55, 45, 33])
print("Edades registradas:", edades)

print("Persona más joven:", np.min(edades), "años")
print("Persona más adulta:", np.max(edades), "años")

print("Rango de edades:", np.max(edades) - np.min(edades), "años")
