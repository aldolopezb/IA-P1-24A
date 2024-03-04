#Aldo López Barrios
#21310106   6E


#SCOPE el el alcanze de de las variables. Si es que son globales o locales

def funcion():
    variableLocal = "Dentro de la función"
    print(variableLocal)
    #print(variableAnidada)         #Al intentar imprimir esta variable nos arroja error porque la variable no pertenece a esta funcion

    def funcionAnidada():
        variableAnidada = "Dentro de la segunda funcion"
        print(variableAnidada)
    
    funcionAnidada()

funcion()

'''De la misma manera, pordía declarar las variables fuera de las funciones y cada función,
aunque sea anidada podría tomar la variable ya que sería una variable global'''