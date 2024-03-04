#Aldo López Barrios
#21310106   6E


#Funciones LAMBDA o funciones anónimas
#Nos sirven para crear funciones con sintaxis más corta y simplificada

import math

'''Funcion sin uso de LAMBDA'''
def area(radio):
    resultado = round(math.pi * radio**2, 4)
    print(resultado)
area(2)

'''Funcion con uso de LAMBDA'''
#Se pueden simplificar funciones cortas que solo ocupen una linea
area2 = lambda radio: round(math.pi * radio**2, 4)
print(area(3))