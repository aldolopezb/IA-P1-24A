#Aldo López Barrios
#21310106   6E

'''De esta manera, en lugar de pasar cada nombre y anotarlo en la funcion alumnos,
*args nos permite tomar solo los que necesitemos o pidamos'''

def alumnos(*args):
    print('El primer alumno es ' + args[0] + ' y el último es ' + args[3] + '.')

alumnos('Aquiles', 'Elmer', 'Pancracio', 'Petunia')