import math 
import matplotlib.pyplot as plt
import re
from Analizador_De_Codigo import analizador_archivo


#esto es comentario
""" 
Funcion que suma 
dos numeros
"""

def suma(a,b):
    """
    Esta es una funcion que realiza y retorna una suma
    Parametros de entrada
    a (int), b (int)
    Salida
    a + b
    """

    return a + b

def resta(a,b):
    """
    Esta es una funcion que realiza y retorna una resta
    Parametros de entrada
    a (int), b (int)
    Salida
    a - b
    """
    return a - b

#comentario
numeros = 10
for i in numeros:
    if i<numeros: 
        print("a")
    elif i>numeros:
        print("numeros>>>")
    else:
        print("numeros")

# Este es un comentario
print("Hola, mundo")

# Otro comentario
x = 10  
y = 20

# Suma
z = x + y

val = 3
val = 3
val = 3
val = 3
val = 3

miMatriz = [
    1,
    3,
    4
]

# Fin del código

"""
Este es un comentario de multiples lineas
el sentido de su existencia se limita a servir unicamente 
como un comentario. 

Cualquier uso fuere de este no tendra sentido
"""

#Este es un comentario simple

"""
Este comentario simula que se tenga codigo dentro

numeros = 10

for i in numeros:
    if i<numeros: 
        print("a")
    elif i>numeros:
        print("numeros>>>")
    else:
        print("numeros")

"""