#Aldo López Barrios
#21310106   6E


class Usuario:
	nombre = ''
	apellidos = ''

	def imprime_datos(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)       

usuario1 = Usuario()

usuario1.nombre = 'Aquiles'
usuario1.apellidos = 'Castro Fernández'

usuario1.imprime_datos()  #Hasta este momento se manda a llamar a la función