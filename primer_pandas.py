
import pandas as pd

datos = {
    'Nombre':['Lady','Edwin', 'Sebastian', 'Samantha'],
    'Edad':[35,18,19,15],
    'Ciudad':['Bogotá','Barbosa','Pauna','Chiquinquirá']
}
"""print(datos)

print(control)"""

control = pd.DataFrame(datos)
control.to_csv('dataframepython.csv', index=False)
print('Archivo creado satisfactoriamente.')


"""archivo = pd.read_csv('tips.csv')
print(archivo.head())
print('---------------------------------------------')
print(archivo.tail())"""