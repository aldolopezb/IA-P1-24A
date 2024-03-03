#Aldo López Barrios
#21310106   6E


Catalogo1 = {
    'Nombre': 'HELLDIVERS',
    'Genero': 'Accion',
    'Precio': '$699'
}

Catalogo2 = {
    'Nombre': 'RDR II',
    'Genero': 'Accion - Aventura',
    'Precio': '$1,299'
}

#Al hacer esto, el ciclo for solo imprime los elementos sin sus propiedades. Solo 'Nombre', 'Genero' y 'Precio'
'''for x in Catalogo1:
    print(x)'''

#De esta manera mostramos los valores ('HELLDIVERS', 'Accion' y '$699')
'''for x in Catalogo1.values():
    print(x)'''


#De esta manera podemos imprimir ambos datos
for x,y in Catalogo1.items():
    print(x,y)