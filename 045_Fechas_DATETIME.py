#Aldo López Barrios
#21310106   6E


#Con este modulo podemos trabajar las fechas
import datetime
                          #Año, mes, dia, hora, min, seg, micseg
fecha = datetime.datetime(2024, 3, 3)
#fecha = datetime.datetime.now()    #Con esta linea de programacion podemos ver la fecha exacta del momento
print(fecha)

#tamben podemos mandar a imprimir la fecha solo con los datos que queramos
datetime.datetime.now()
print("Año: ", fecha.year, fecha.day)