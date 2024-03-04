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


class usuarioSecundario(usuario):
    def __init__(self, nombre , edad, nacionalidad):
        usuario.__init__(self, nombre, edad)            #De esta manera podemos heredar de la clase usuarios las propiedades que deseemos sin mezclarlas con otras clases
        self.nacionalidad = nacionalidad

    def muestraDatos(self):
        print('El nombre de usuario es: ' + self.nombre, self.edad, self.nacionalidad)

usuario2 = usuarioSecundario("Alan", 26, "Mexicano")
usuario2.muestraDatos()