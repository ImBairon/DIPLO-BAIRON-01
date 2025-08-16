#Ciclos condicional if
"""""
a=5
b=34

if a<b:
    print("Es mayor")
else:
    print("Es menor")"""

#Ciclos condicional if
"""""
calificacion = float(input("Digite su calificación:"))

if calificacion==5:
    print("Exelente")
elif calificacion>=4 and calificacion<5:
    print("Sobresaliente")
elif calificacion>=3 and calificacion<4:
    print("Aceptable")
elif calificacion>=2 and calificacion<3:
    print("Insuficiente")
elif calificacion>=1 and calificacion<2:
    print("Deficiente")
else:
    print("Calificacion equivocada")
"""""
#Bucle for
"""
lista = [1,2,3,4,5,6,7,8,9,7,6,5,0]
for i in lista:
    print(i)"""""""""


#Bucle for
"""""
lista = [1,2,3,4,5,6,7,8,9,7,6,5,0]
palabra = "Hola a todos"
"""""

#Range

"""""
num = int(input())
for i  in range(3,15):
    print(f"{num} x {i} = {num*1}")
"""""
#While

"""""
i=0
while i<5:
    print(i)
    i+=1
"""""
""""
while True:
    a= int(input("Digite un numero:"))
    if a>0:
        print("Numero positivo.")
        break
    else:   
        a= int(input("Digite un número:"))
    """
#Ejercicio Bairon Díaz
"""""
while True:
    num = int(input("Digite un número a multiplicar:"))
    if num == 0:
        print("No se puede multiplicar por cero Basura")
        continue
    for i in range(0,9):
        print(f"{num} x {i} = {num*i}")
    """""
        
   



#Funciones sin parametros
""""
def multiplicar(x,y):
    return x*y

    a=int(input('Digite un número:'))
    b=int(input('Digite un número:'))

print(multiplicar(a,b))
"""

#Calculadora Básica

