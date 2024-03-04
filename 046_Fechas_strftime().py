#Aldo López Barrios
#21310106   6E

#strftime() (StringFormatTime)
import datetime
import locale

locale.setlocale(locale.LC_ALL, "es-ES")        #De esta manera podemos traducir al español 

fecha = datetime.datetime.now()
print(fecha.strftime("%M"))

#strftime() tiene muchas opciones de muestreo de fechas
#Que nos serviría para un codigo más profesional