#Aldo López Barrios
#21310106   6E


Lista = ['Atletismo', 'Natación', 'Futbol', 'Gimnasia', 'Tenis']

deporte = input('Introduce el deporte que quieras buscar:\n')

'''Utlizando 'in' en este caso, podemos saber si hay o no algún elemento en la lista
arrojandonos como resultado TRUE o FALSE. De esta manera podríamos con if else 
buscar e inclusive añadir nuevos elementos'''

if deporte in Lista:
    print('El deporte está en la lista')
else:
    print('El deporte NO está en la lista')