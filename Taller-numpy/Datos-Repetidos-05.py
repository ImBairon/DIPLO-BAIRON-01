import numpy as np

comidas = np.array(["Pizza", "Pasta", "Pizza", "Sushi", "Hamburguesa", "Sushi", "Pizza"])

comidas_unicas = np.unique(comidas)

print("Comidas originales:", comidas)
print("Comidas únicas:", comidas_unicas)
