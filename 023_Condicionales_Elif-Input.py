#Aldo López Barrios
#21310106   6E


'''La condicional elif se coloca despues de un if, no se puede colocar al inicio
y el metodo input() es para colocar un dato en la terminal. Este dato lo podremos 
guardar en una variable para usarla'''

edad = int(input("Cuál es tu edad?:\n"))

if edad >=1 and edad <=17:
    print('Eres menor de edad')

elif edad >= 18:
    print('Eres mayor de edad')

elif edad > 99:
    print('Edad inválida')