#Calculadora básica
#Importar los archivos independientes creados con las funciones para el menú
from sumar import suma
from restar import resta
from multiplicar import multiplicacion
from dividir import division
from potenciar import potencia
from menup import menu
#Creamos una variable de control para el menú
control = 0
#Establecemos el ciclo while para repetir las acciones
while True:
    menu()
    control = int(input('Digite la opición deseada: '))
    #A través del if, validamos las opciones digitadas
    if control == 1:
        #f permite formatear el texto para usar sentencias dentro de
        #{}, se conoce como sentencias de Jinja2
        print(f'La suma es: {suma()}')
        continuar = input('Desea continuar? Presione S para continuar o N para salir.')
        #Lower se utilizar para convertir todo en minuscúla.
        continuar= continuar.lower()
        if continuar == 's':
            menu()
        else:
            #Break corta la ejecución del while
            break 
    elif control == 2:
        print(f'La resta es: {resta()}')
        continuar = input('Desea continuar? Presione S para continuar o N para salir.')
        continuar= continuar.lower()
        if continuar == 's':
            menu()
        else:
            break
    elif control == 3:
        print(f'La multiplicación es: {multiplicacion()}')
        continuar = input('Desea continuar? Presione S para continuar o N para salir.')
        continuar= continuar.lower()
        if continuar == 's':
            menu()
        else:
            break
    elif control == 4:
        print(f'La división es: {division()}')
        continuar = input('Desea continuar? Presione S para continuar o N para salir.')
        continuar= continuar.lower()
        if continuar == 's':
            menu()
        else:
            break
    elif control == 5:
        print(f'La potencia es: {potencia()}')
        continuar = input('Desea continuar? Presione S para continuar o N para salir.')
        continuar= continuar.lower()
        if continuar == 's':
            menu()
        else:
            break
    elif control == 6:
        print('Vuelva pronto.')
        break
    else:
        print('Opción erronea, intenta de nuevo')