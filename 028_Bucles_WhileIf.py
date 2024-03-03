#Aldo López Barrios
#21310106   6E


#Podemos cortar o detener el ciclo while con 'break'

'''x = 1
while x < 10:
	print(x)
	if x == 6:
		break       #Esta condicion haría que el contador se detuviera en 6
	x += 1'''
	
#De la misma manera con 'continue' podemos saltar los números que programemos

x = 0
while x < 10:
	x += 1
	if x == 6:
		continue       #Esta condicion haría que el contador se saltara el 6
	print(x)
