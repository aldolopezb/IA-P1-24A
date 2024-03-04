#Aldo López Barrios
#21310106   6E


class usuario:
    def __init__(self, nombre , edad):
        self.nombre = nombre
        self.edad = edad

    def muestraDatos(self):
        print('El nombre de usuario es:' + self.nombre, self.edad)

usuario1 = usuario("Alma", 36)
usuario1.muestraDatos()

#Tambien aunque ya le hayan declarado y se haya guardado, se pueden cambiar los valores
usuario1.edad = 38
usuario1.muestraDatos()