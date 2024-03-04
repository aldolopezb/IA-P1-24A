#Aldo López Barrios
#21310106   6E


class usuario:
    def __init__(self, nombre , edad):
        self.nombre = nombre
        self.edad = edad

    def muestraDatos(self):
        print('El nombre de usuario es: ' + self.nombre, self.edad)

usuario1 = usuario("Alma", 36)
usuario1.muestraDatos()

#Para eliminar alguna propiedad se utiliza con la palabra reservada del
del usuario1.edad
#usuario1.muestraDatos()        #Ya no dejaría imprimir ya que no existe la propiedad 'edad'

'''De la misma manera utilizando "del usuario" por ejemplo, eliminaríamos completamente un objeto'''
