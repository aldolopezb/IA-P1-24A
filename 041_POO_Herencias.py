#Aldo López Barrios
#21310106   6E


'''La herencia nos permite definir una clase que "Hereda" todos los metodos y propiedades
de otra clase de la clase principal'''

class usuario:
    def __init__(self, nombre , edad):
        self.nombre = nombre
        self.edad = edad

    def muestraDatos(self):
        print('El nombre de usuario es: ' + self.nombre, self.edad)

usuario1 = usuario("Alma", 36)
usuario1.muestraDatos()

class usuarioSecundario(usuario):
    pass                                #Solo con esto ya tendríamos las mismas propiedades que la clase principal

usuario2 = usuarioSecundario("Alan", 26)
usuario2.muestraDatos()

