#Aldo López Barrios
#21310106   6E

#Denstro de la clase declaramos la funcion init en donde guardamos el nombre y apellido en este caso
class Usuario:
	def __init__(self, nombre, apellidos):
		self.nombre = nombre
		self.apellidos = apellidos

	def imprime_datos(self):
		print('Nombre:', self.nombre, '\nApellidos:', self.apellidos)

#Se debe especificarse el nombre y apellido. Y se pueden poner tantos usuarios como queramos
usuario1 = Usuario("Esteban", "Quito")

#Pero debemos mandar a llamarlos
usuario1.imprime_datos()